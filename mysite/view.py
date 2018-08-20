# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response


def hello(request):  
    request.encoding='utf-8'
    return HttpResponse('hello world')