
from django.urls import path
from . import views

# app_name = 'blog'

urlpatterns = [
    # path('january/', views.january,name='january'),
    # path('february/', views.february,name='february'),
    path('', views.starting_page, name='starting_page'),
    path('posts/',views.posts,name='post-page' ),
    path('posts/<slug:slug>',views.post_detail,name='post-detail-page' ),

]
