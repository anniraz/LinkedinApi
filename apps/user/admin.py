from django.contrib import admin

from apps.user.models import User,Position,Skills,EducationInformation


admin.site.register(User)
admin.site.register(Position)
admin.site.register(Skills)
admin.site.register(EducationInformation)