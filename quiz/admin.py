from django.contrib import admin
from .models import (
    Category,
    Quiz,
    Question,
    Option
)

# using the third-party nested admin to have a better organized Admin panel so that we don't
# have to hop on different model fields to form a full question with options. We have added 
# installed nested_admin, added it to settings.py and urls.py. see more on nested_admin here:
# https://django-nested-admin.readthedocs.io/en/latest/quickstart.html
import nested_admin


# NestedTabularInline is used for childs, while NestedModelAdmin is used for parents

class OptionAdmin(nested_admin.NestedTabularInline): # NestedTabularInline, since this is child to Question
    model = Option
    extra = 5 # default is 3 for extra. Determines how many options we'll see on the admin panel


class QuestionAdmin(nested_admin.NestedTabularInline): # NestedTabularInline, since this is child to QuizAdmin
    model = Question
    inlines = [OptionAdmin] # inlines here mean this field will also include OptionAdmin
    extra = 5
    max_num = 20


class QuizAdmin(nested_admin.NestedModelAdmin): # NestedModelAdmin, since this is the parent.
    model = Quiz
    inlines = [QuestionAdmin]



admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin) # passing QuizAdmin here, we'll see all three fields, namely, Quiz, Question, and Option in Quiz Admin panel page
admin.site.register(Question)
admin.site.register(Option)