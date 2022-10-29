from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import Profileform
from .models import UserProfile


def store_file(file):
    with open(f'temp/{file}','wb+') as dest:
        for chunk in file.chunks():
           dest.write(chunk)

class CreateProfileView(View):
    def get(self,request):
        form = Profileform()
        return render(request, 'profiles/create_profile.html',{'form':form})

    def post(self, request):
        # store_file(request.FILES['image'])
        submitted_form = Profileform(request.POST,request.FILES)
        if submitted_form.is_valid():
          # store_file(request.FILES['user_image'])
          profile = UserProfile(image=request.FILES['user_image'])
          profile.save()
          return HttpResponseRedirect('/profiles',{'form':submitted_form})

