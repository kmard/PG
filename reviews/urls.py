
from django.urls import path
from . import views

urlpatterns = [

     path('', views.review, name='feedback_page'),
     path('thank-you',views.thank_you ),
     # path('list/<slug:slug>',views.book_detail_slug,name='book_slug' ),
]
