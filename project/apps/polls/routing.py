
from django.urls import path

from project.apps.polls import consumers

websocket_urlpatterns = [
    path('ws/<roomid>/', consumers.Consumer),
]