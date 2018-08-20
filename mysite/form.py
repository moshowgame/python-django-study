# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response

# 表单
def form_view(request):
    return render_to_response('form.html')

# 接收请求数据
def form_submit(request):  
    request.encoding='utf-8'
    
    # 如果GET方法里面有'name'
    if 'name' in request.GET:
        message = '接收到GET请求: ' + request.GET['name']
    elif 'name' in request.POST:
        message = '接收到POST请求: ' + request.POST['name']
    else:
        message = '接收不到name属性'
    return HttpResponse(message)