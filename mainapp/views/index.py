# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .login import authbar, getuser, redirectLogin
 
def index(request):
    user = getuser(request)
    if user is None:
        return redirectLogin(request)
    context = {}
    authbar(request, context)
    return render(request, 'pages/index.html', context)

apis = [
]