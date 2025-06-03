from django.urls import path

from instruktiraime.instruktiraime_web.views import index

urlpatterns = (
    path('', index, name='index'),
)
