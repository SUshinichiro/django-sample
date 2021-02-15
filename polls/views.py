from django.shortcuts import render
import django_filters

# Create your views here.
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework import viewsets
from .models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']


class QuestionFilter(django_filters.FilterSet):
    class Meta:
        model = Question
        fields = {'pub_date': ['gte', ], }


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()

    serializer_class = QuestionSerializer
    filter_class = QuestionFilter

    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = [IsAuthenticated | HasAPIKey]


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['question', 'choice_text', 'votes']


class ChoiceFilter(django_filters.FilterSet):
    class Meta:
        model = Question
        fields = []


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()

    serializer_class = ChoiceSerializer
    filter_class = ChoiceFilter
