# myapp/middleware.py
from django.http import HttpResponseForbidden

class APIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request path starts with '/api/'
        if request.path.startswith('/api/v1/'):
            api_key = request.headers.get('X-API-Key')

            if not api_key or api_key != 'secret-api-key': # seceret x-api-key for our /api/v1/ routes
                return HttpResponseForbidden("Invalid API Key")

        response = self.get_response(request)
        return response
