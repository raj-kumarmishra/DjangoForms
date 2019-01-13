from django import forms

class RgistrationForm(forms.Form):
    fname = forms.CharField(max_length=255)
    lname = forms.CharField(max_length=255)
    email = forms.EmailField()