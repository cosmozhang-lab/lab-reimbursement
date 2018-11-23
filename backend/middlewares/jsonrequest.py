import json
from django.conf import settings
    
def JsonRequestMiddleware(get_response):
    def middleware(request):
        if request.content_type.lower() == "application/json":
            try:
                encoding = request.encoding or settings.DEFAULT_CHARSET
                request.jsondata = json.loads(request.body.decode(encoding))
            except Exception:
                request.jsondata = None
        return get_response(request)
    return middleware
