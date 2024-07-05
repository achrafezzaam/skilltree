''' Define the Course models, Detail and Message '''
from django.contrib.auth.models import User
from django.db import models


class Detail(models.Model):
    ''' Define the Course Detail object '''
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    img_path = models.CharField(max_length=150)
    votes = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    active = models.BooleanField(default=False)

    class Meta:
        permissions = [
                ("get_courses", "Can get courses"),
                ("member_courses", "Can get member courses"),
                ("create_courses", "Can create courses"),
                ("update_courses", "Can update courses"),
                ("delete_courses", "Can delete courses"),
                ]

    def __str__(self):
        ''' Create a visual representation when the object is created '''
        return self.title

    def change_activity(self):
        ''' Change the active status of the course '''
        self.active = not self.active

    def up_vote(self):
        ''' Increment the votes value by one '''
        self.votes += 1

    def down_vote(self):
        ''' Decrement the votes value by one '''
        self.votes -= 1

    def set_price(self, price):
        ''' Set the course price

            Args:
                price [int, float]: The new price for the course
            Return:
                Return the message: The price should be a number.
                If a non int or float value is given
        '''
        if (isintance(price, (int, float))):
            self.price = price
        else:
            return "The price should be a number"


class Message(models.Model):
    ''' Define the Message object '''
    author = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            )
    course = models.ForeignKey(
            Detail,
            on_delete=models.CASCADE,
            )
    content = models.CharField(max_length=200)

    def __str__(self):
        ''' Create a visual representation when the object is created '''
        return self.content


class Question(models.Model):
    ''' Create the Question object '''
    course = models.ForeignKey(
            Detail,
            on_delete=models.CASCADE,
            )
    content = models.CharField(max_length=255)

    class Meta:
        permissions = [
                ("create_questions", "Can create questions"),
                ]

    def __str__(self):
        ''' Create a visual representation when the object is created '''
        return self.content


class Choice(models.Model):
    ''' Create the Choice object '''
    question = models.ForeignKey(
            Question,
            on_delete=models.CASCADE,
            )
    choice_text = models.CharField(max_length=200)
    right_answer = models.BooleanField(default=False)

    class Meta:
        permissions = [
                ("create_choices", "Can create choices"),
                ]

    def __str__(self):
        ''' Create a visual representation when the object is created '''
        return self.choice_text


class Answer(models.Model):
    ''' Create the Answer object '''
    question = models.ForeignKey(
            Question,
            on_delete=models.CASCADE,
            )
    choice = models.ForeignKey(
            Choice,
            on_delete=models.CASCADE,
            )

    def __str__(self):
        ''' Create a visual representation when the object is created '''
        return self.choice
