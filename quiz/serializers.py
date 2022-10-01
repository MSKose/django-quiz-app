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


# we're defining OptionSerializer before QuestionSerializer since we'll not send this to 
# views.py, rather we'll use this below in QuestionSerializers
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = (
            'id',
            'option_text',
            'is_right'
        )

# the reason we defined OptionSerializer before QuestionSerializer is beacuse we want to 
# use pass QuestionSerializer to our views and urls and have a nested JSON where our 
# related options would be nested into our Question JSON and be accessed from there
class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True) # here options is no random variable. we have defined a related_name in our Option model to refer it in Question model
    quiz = serializers.StringRelatedField()

    class Meta:
        model = Question
        fields = (
            'id',
            'quiz',
            'title',
            'difficulty',
            'options'
        )