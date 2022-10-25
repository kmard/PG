
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review

# Create your views here.
def review(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     if username == '':
    #         return render(request, 'reviews/review.html', {'has_error':True})
    #     return HttpResponseRedirect('thank-you')
    # else:
    #     return render(request,'reviews/review.html',{'has_error':False})

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
           # form.cleaned_data
           review = Review(user_name=form.cleaned_data['user_name'],
                           review_text = form.cleaned_data['review_text'],
                           raiting = form.cleaned_data['raiting']
                           )
           review.save()
           return HttpResponseRedirect('thank-you')
    else:
        form = ReviewForm()
        return render(request,'reviews/review.html',{'form':form,'has_error':False})


def thank_you(request):
    return render(request, 'reviews/thanks.html', {})
