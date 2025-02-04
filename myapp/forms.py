from myapp.models import Question
from django import forms

class RegistrationForms(forms.Form):
    class meta:
        model=Question
        fields=["name","contact","address"]
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'contact':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'})
        }