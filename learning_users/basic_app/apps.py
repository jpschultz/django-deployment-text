from django.apps import AppConfig
from basic_app.models import UserProfileInfo

admin.site.register(UserProfileInfo)

class BasicAppConfig(AppConfig):
    name = 'basic_app'
