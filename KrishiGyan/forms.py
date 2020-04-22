from django import forms

from .models import Question

class Upload(forms.ModelForm):
    class Meta:
        model = Question
        fields =('CropName','Questions','image','Email','date') 
        
        