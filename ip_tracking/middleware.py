from .models import RequestLog, BlockedIP
from django.http import HttpResponseForbidden

class IPLoggingMiddleware:
    """
    Middleware to log the IP address of each request.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = request.META.get('REMOTE_ADDR', 'unknown')
        path = request.path
        print(f"Request from IP: {ip_address}")
        print(f"Request path: {path}")
        RequestLog.objects.create(ip_address=ip_address, path=path)

        if BlockedIP.objects.filter(ip_address=ip_address).exists():
            print(f"Blocked IP: {ip_address}")
            return HttpResponseForbidden("Your IP address is blocked.")

            
        # Call the next middleware or view
        response = self.get_response(request)
        return response
