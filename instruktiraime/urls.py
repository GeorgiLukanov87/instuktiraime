from django.contrib import admin
from django.urls import path, include

from .instruktiraime_web.views import chatbot_view

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('instruktiraime.instruktiraime_web.urls')),
    path("chatbot/", chatbot_view, name="chatbot"),
)
