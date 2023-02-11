from django.utils import timezone
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.authentication import JWTAuthentication

User=get_user_model()


class UserStatus:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            request_user = JWTAuthentication().authenticate(request)[0]
            for user in User.objects.all():
                if (timezone.now() - user.last_action) > timezone.timedelta(minutes=1):
                    user.is_online=False
                    user.save()
        
            if request_user:
                user = User.objects.get(id=request_user.id)
                user.is_online=True
                user.last_action = timezone.now()
                user.save()
        except:
            pass

        return self.get_response(request)