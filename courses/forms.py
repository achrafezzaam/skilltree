''' Define the Course forms '''
from django.core.exceptions import ValidationError
from django import forms


class DetailForm(forms.Form):
    ''' Define the course details forms '''
    title = forms.CharField(label="Title", max_length=100)
    description = forms.CharField(label="Description", max_length=255)
    price = forms.FloatField(label="Price")
    active = forms.BooleanField(label="Activate")


class CommentForm(forms.Form):
    ''' Define the course comments forms '''
    content = forms.CharField(label="Comment", max_length=200)

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise ValidationError('No entry. Please write something before submitting')
        return content
