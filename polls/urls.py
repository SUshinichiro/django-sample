from django.urls import path, include
from . import views

from rest_framework import routers, views
from polls.views import *
router = routers.DefaultRouter()
router.register(r'polls', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
