from django import forms
from .models import Post

class BasicForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text','image')
