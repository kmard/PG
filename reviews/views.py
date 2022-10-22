
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm

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
           return HttpResponseRedirect('thank-you')


    form = ReviewForm()
    return render(request,'reviews/review.html',{'form':form,'has_error':False})


def thank_you(request):
    return render(request, 'reviews/thanks.html', {})
