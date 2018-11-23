from mainapp.utils.auth import gettoken, update_token
    
def AuthenticationMiddleware(get_response):
    def middleware(request):
        request.token = gettoken(request)
        if request.token: update_token(request.token)
        request.user = request.token.user if request.token else None
        return get_response(request)
    return middleware
