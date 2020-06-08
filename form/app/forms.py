from django import forms

from .models import Snippet

class RegisterForm(forms.Form):
    name = forms.CharField()
    email = forms. CharField(label='E-mail')
class Snippetform(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('name','email')
