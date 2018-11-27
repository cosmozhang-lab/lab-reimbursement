# -*- coding: utf-8 -*-
 
from django.http import JsonResponse
from mainapp.models.auth import User, LoginToken
from mainapp.utils.auth import add_token
from urllib.parse import quote as escape
from django.conf import settings

from mainapp.models.person import Person
 
def register(request):
    username = request.jsondata["username"]
    password = request.jsondata["password"]
    if User.objects.filter(username=username).count() > 0:
        return JsonResponse({"success": False, "reason": "User already exists"})
    user = User(username=username, password=password)
    user.save()
    request.session["username"] = username
    return JsonResponse({"success": True})

def login(request):
    username = request.jsondata["username"]
    password = request.jsondata["password"]
    user = User.objects.filter(username=username).first()
    if user is None:
        return JsonResponse({"success": False, "reason": "user-not-exist"})
    if not user.test_password(password):
        return JsonResponse({"success": False, "reason": "incorrect-password"})
    token = add_token(user, int(request.jsondata["expiresecs"]) if "expiresecs" in request.jsondata else settings.DEFAULT_LOGIN_EXPIRE_SECS)
    retdata = {}
    retdata["token"] = str(token)
    retdata["user"] = {
        "username": user.username,
        "nickname": user.nickname
    }
    return JsonResponse({"success": True, "data": retdata})

def logout(request):
    token = request.token
    if token:
        token.delete()
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False, "reason": "not-login"})

apis = [
    ("login", login),
    ("logout", logout),
    ("register", register)
]