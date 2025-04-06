from asgiref.sync import sync_to_async
import anthropic
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.conf import settings
import httpx
from random import shuffle, randint


def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/homepage.html')


# @login_required(login_url=settings.LOGIN_URL)
def initiatives(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/initiatives.html')


@sync_to_async
# @login_required(login_url=settings.LOGIN_URL)
def pears(request: HttpRequest) -> HttpResponse:
    def get_ai_response(messages, word):
        PROXIES = {}

        if settings.AI_PROXY:
            PROXIES['all://'] = settings.AI_PROXY

        client = anthropic.Anthropic(
            api_key=settings.ANTHROPIC_API_KEY,
            http_client=httpx.Client(proxies=PROXIES),
        )
        
        response = client.messages.create(
            model='claude-3-haiku-20240307',
            max_tokens=200,
            temperature=0.7,
            system=(
                'You are a children\'s story generator for ages 2-5. Rules:\n\n'
                '1. Use very small sentences (about 4 words)\n'
                '2. MINIMAL STORY LENGHT: 10 sentences!!!!!!!\n'
                f'3. Include "{word}" word 4 times!!\n'
                '4. One using of word mathes one ID'
                f'5. REPLACE 2 uses of "{word}" and 2 RANDOM WORDS from story with format: "%[ID]%" like this: "%1%"!!!\n'
                '6. Use only Russian language!!'
                '7. EVERY USING OF REPLACED WORD SHOULD BE ADDED TO ANSWER LIST USING THAT FORMAT: '
                '   ^ [ID]. [correct word] [6-8 completely different simple words separated by ";"]"\\n"\n\n'
                '   Example: "^ 1. [поезд] [мяч; слон; яблоко; гулять; банан; лампа; чай; солнце]"\n'
                '   DO NOT USE EXAMPLED WORDS!!! FOLLOW FORMATTING!!! USE WORDS IN LIST, NO IDs\n\n'
                '8. REMOVE TITLE BEFORE ANSWERS AND STORY!!! ONLY TEXT!!!'
                '9. CHECK AND FIX IF ANY WORDS ARE MISSING: EVERY ID IN TEXT MUST HAVE ANSWER WITH THAT ID IN LIST!!! DO NOT STRIP WORDS!!\n\n'
            ),
            messages=[{'role': 'user', 'content': f'Short plot: {messages}'}],
        )
        return response.content[0].text.strip()

    def parse_ai(response: str) -> None | dict:
        text, answers = '', {}
        for line in response.split('\n'):
            line = line.strip()
            if not line:
                continue
            if line.startswith('^'):
                try:
                    components = [i.strip('.[];') for i in line.strip(' ^').split(" ") if i]
                    _id = int(components[0])
                    correct_word = components[1]
                    alternative_words = components[2:][:randint(2, 4)]
                    options = alternative_words + [correct_word]
                    shuffle(options)
                    answers[_id] = {'correct_word': correct_word, 'options': options}
                    if not correct_word or not alternative_words:
                        answers[_id] = answers[0]
                except:
                    return
            else:
                text += f'{line} '
        p_text = []
        for sentence in text.split('. '):
            s_info = []
            was = False
            for i in sentence.split('%'):
                if not i.isdigit():
                    if i:
                        s_info += [i]
                else:
                    if was:
                        return None
                    was = True
                    if int(i) not in answers:
                        return None
                    s_info += [int(i)]
            if s_info:
                p_text += [s_info]
        return {'text': p_text, 'answers': answers}


    messages = request.GET.get('messages', '').strip()
    word = request.GET.get('word', '').strip()
    
    if not (messages and word):
        return render(request, 'main/pears.html')
    
    for _i in range(1, 6):
        response = get_ai_response(messages, word)
        data = parse_ai(response)
        if data is not None:
            return render(request, 'main/pears-generate.html', context={
                'data': data,
                'debug_i': _i,
            })

    return render(request, 'main/pears.html', {'error': True})


@login_required(login_url=settings.LOGIN_URL)
def diagnostic_test(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/diagnostic-test.html')


@login_required(login_url=settings.LOGIN_URL)
def test_question(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/test-question.html', {
        'question_title': '2 + 2 = ?',
        'answers': ['2', '4', '22', '5'],
    })
