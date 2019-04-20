from django.urls import include, path
from rest_framework import routers

from apps.membership.rest_api.views import (SessionView, SetPasswordView)

rest_router = routers.DefaultRouter()
rest_router.trailing_slash = "/?"  # added to support both / and slashless
rest_router.register(r'session', SessionView, basename='session')

app_name = 'membership'
urlpatterns = [
    path('', include(rest_router.urls)),
    path('me/password', SetPasswordView.as_view()),
]
