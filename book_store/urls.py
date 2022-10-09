
from django.urls import path
from . import views

# app_name = 'book_store'

urlpatterns = [

     path('list', views.list_book, name='list'),
     path('list/<int:id>',views.book_detail,name='book' ),
    # path('posts/',views.posts,name='post-page' ),
    # path('posts/<slug:slug>',views.post_detail,name='post-detail-page' ),

]
