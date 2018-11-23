from mainapp.models.auth import LoginToken
from datetime import datetime, timedelta
from utilities.randomstring import randomstring
from utilities.localtime import timezone as lctz

def clear_expired_tokens(user=None):
    queryset = LoginToken.objects.filter(expiretime__lt=datetime.now().astimezone(lctz))
    if user: queryset = queryset.filter(user=user)
    queryset.delete()

def add_token(user, expiresecs):
    clear_expired_tokens()
    createtime = datetime.now().astimezone(lctz)
    expiretime = createtime + timedelta(seconds=expiresecs)
    tokenstr = randomstring()
    while LoginToken.objects.filter(expiretime__lte=datetime.now().astimezone(lctz), token=tokenstr).count() > 0:
        tokenstr = randomstring()
    token = LoginToken(user=user, token=tokenstr, createtime=createtime, updatetime=createtime, expiretime=expiretime, expiresecs=expiresecs)
    token.save()
    return token

def update_token(token):
    expiresecs = token.expiresecs
    updatetime = datetime.now().astimezone(lctz)
    expiretime = updatetime + timedelta(seconds=expiresecs)
    token.updatetime = updatetime
    token.expiretime = expiretime
    token.save()
    return token

def gettoken(request):
    if "HTTP_AUTHORIZATION" in request.META:
        token = request.META["HTTP_AUTHORIZATION"]
        if token:
            token = LoginToken.objects.filter(token=token, expiretime__gte=datetime.now().astimezone(lctz)).first()
            if token:
                return token
    else:
        return None

def getuser(request):
    token = gettoken(request)
    if token:
        return token.user
    else:
        return None
