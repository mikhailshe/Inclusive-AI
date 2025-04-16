from random import shuffle, randint

import httpx
from anthropic import Anthropic, DefaultHttpxClient
from asgiref.sync import sync_to_async
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


@sync_to_async
# @login_required(login_url=settings.LOGIN_URL)
def pears(request: HttpRequest) -> HttpResponse:
    def get_ai_response(messages, word):
        if settings.AI_PROXY:
            print(settings.AI_PROXY)
            client = Anthropic(
                api_key=settings.ANTHROPIC_API_KEY,
                http_client=DefaultHttpxClient(
                    proxy=settings.AI_PROXY,
                    transport=httpx.HTTPTransport(local_address="0.0.0.0"),
                )
            )
        else:
            client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)



        system_prompt = (
            'Ты — генератор обучающих сказок для детей начальной школы (6–9 лет). Правила:\n\n'
            '1. История должна быть ПОЛНОЙ, с началом, развитием, кульминацией и концом.\n'
            '2. Используй простые, но не примитивные фразы. Средняя длина предложения — 6–8 слов.\n'
            '3. Длина: минимум 15 предложений, максимум — 25.\n'
            f'4. Используй слово "{word}" РОВНО 4 раза в тексте.\n'
            '5. ЗАМЕНИ два вхождения этого слова и два других случайных слова в тексте на маркеры вида: "%[ID]%" (например "%1%")!!!.\n'
            '6. Каждый ID должен быть сопоставлен с правильным словом и 6–8 случайными отвлекающими словами. Пример строки:\n'
            '   ^ 1. [яблоко] [каша; робот; весна; бегать; тетрадь; море; мыло]\n'
            '   Используй только русский язык. НЕ повторяй слова из примера!\n'
            '7. НЕ используй такие слова, как "добрый", "злой", "хороший", "плохой" — пусть мораль передаётся через действия.\n'
            '8. История должна обучать: подчёркивать важные ценности (честность, дружба, труд, безопасность, забота и т.д.).\n'
            '9. Удали заголовок. Выводи только историю и ответы.\n'
            f'10. Слово "{word}" должно склоняться в зависимости от контекста и правил русского языка\n'
            '11. ОБЯЗАТЕЛЬНО проверь, что для каждого %ID% есть строка ответа. НЕ ИСПОЛЬЗУЙ ID в списке слов.\n'
        )
        
        response = client.messages.create(
            model=settings.ANTHROPIC_MODEL,
            max_tokens=settings.ANTHROPIC_MAX_TOKENS,
            temperature=settings.ANTHROPIC_TEMPERATURE,
            system=system_prompt,
            messages=[{"role": "user", "content": f"Short plot: {messages}"}]
        )
        return response.content[0].text

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
        return render(request, 'pears/pears.html')
    
    for _i in range(1, 6):
        response = get_ai_response(messages, word)
        data = parse_ai(response)
        if data is not None:
            return render(request, 'pears/pears-generate.html', context={
                'data': data,
                'debug_i': _i,
            })

    return render(request, 'pears/pears.html', {'error': True})
