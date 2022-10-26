
from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name",max_length=100)
#     review_text = forms.CharField(label="Your Feedback",
#                                   widget=forms.Textarea,
#                                   max_length=200)
#     raiting = forms.IntegerField(label="Your rating",
#                                  min_value=1,
#                                  max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields= '__all__'