from django.db import models

# we're creating an abstract model named UpdateCreateDate to use created and updated in the 
# models that share these properties. The only thing you have to do is inherit this model
# where you want to use created and updated. See how it's done in Quiz, Question and Option
class UpdateCreateDate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # to present your abstract model you add abstract = True


class Category(models.Model): 
    name = models.CharField(max_length=50, verbose_name='Category Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories' # we if hadn't defined this, django would present us with Categorys in our Admin Panel

    # you can either defined quiz_count like self.quiz_set.count() cuz <modelName>_set refers to the child Quiz model or you 
    # give a related_name to the field you join the fields together. Which is our case here. We have given the related_name 
    # of quizz in our Quiz model and used it here to refer that child Model with self.quizz.count() 
    @property
    def quiz_count(self):
        return self.quizz.count() 


class Quiz(UpdateCreateDate):
    title = models.CharField(max_length=50, verbose_name='Quiz title')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quizz')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Quizzes'

    @property
    def question_count(self):
        return self.question_set.count()


class Question(UpdateCreateDate):

    SCALE = (
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    )

    title = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=1, choices=SCALE)

    def __str__(self):
        return self.title


class Option(UpdateCreateDate):
    option_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.option_text