from asgiref.sync import sync_to_async
import anthropic
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.conf import settings
import httpx
from random import shuffle, randint


def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, 'pages/homepage.html')


# @login_required(login_url=settings.LOGIN_URL)
def initiatives(request: HttpRequest) -> HttpResponse:
    return render(request, 'pages/initiatives.html')


@login_required(login_url=settings.LOGIN_URL)
def diagnostic_test(request: HttpRequest) -> HttpResponse:
    return render(request, 'pages/diagnostic-test.html')


@login_required(login_url=settings.LOGIN_URL)
def test_question(request: HttpRequest) -> HttpResponse:
    return render(request, 'pages/test-question.html', {
        'question_title': '2 + 2 = ?',
        'answers': ['2', '4', '22', '5'],
    })
