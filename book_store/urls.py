
from django.urls import path
from . import views

# app_name = 'book_store'

urlpatterns = [

     path('list', views.list_book, name='list'),
     path('list/<int:id>',views.book_detail,name='book' ),
     path('list/<slug:slug>',views.book_detail_slug,name='book_slug' ),
]
