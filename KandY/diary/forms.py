from django import forms
from .models import White,Question
from django.contrib.auth.models import User


class WhiteForm(forms.ModelForm):
    class Meta:
        model = White
        fields =['owner','update','content','image']
        

class ViewForm(forms.Form):
    find = forms.CharField(label='キーワード:', required=False, \
        widget=forms.TextInput(attrs={'class':'form-control'}))

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['owner','text']


#create
#create
#1125

