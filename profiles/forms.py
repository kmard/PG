from django import forms

class Profileform(forms.Form):
    user_image = forms.FileField()