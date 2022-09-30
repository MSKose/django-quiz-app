from rest_framework import serializers
from .models import (
    Category,
    Quiz,
    Question,
    Option
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'quiz_count' # added this is see the total count of Quizzes for each Category
        )


class QuizSerializer(serializers.ModelSerializer):

    # the following line is important since we don't want to see integers as categories. Instead we want to see something
    # more human-readable. Make sure you have defined a str methon in your Category model, it won't make sense otherwise
    category = serializers.StringRelatedField()

    class Meta:
        model = Quiz
        fields = (
            'id',
            'title',
            'category',
            'question_count'
        )


# we're defining OptionSerializer first since we'll not send this to views.py, rather 
# we'll use this below in QuestionSerializers
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = (
            'id',
            'option_text',
            'is_right'
        )

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True) # here options is no random variable. we have defined a related_name

    class Meta:
        model = Question
        fields = (
            'id',
            'quiz',
            'title',
            'options',
            'difficulty'
        )