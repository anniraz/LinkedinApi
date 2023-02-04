from django.utils import timezone
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.authentication import JWTAuthentication

User=get_user_model()


class UsersPremium:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            request_user = JWTAuthentication().authenticate(request)[0]
            if request_user.is_premium==True:
                if (timezone.now() - request_user.premium_date) > timezone.timedelta(month=1):
                    request_user.is_premium=False
                    request_user.premium_date=None
                    request_user.save()
        
        except:
            pass

        return self.get_response(request)
