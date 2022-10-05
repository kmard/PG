from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

all_posts= [
    {
        'slug':'hike-in-the-mountains',
        'image':'1.jpg',
        'author':'Konst',
        'date':date(2022,10,1),
        'title':'Mountain Hiking',
        'excert':'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
        'content':'''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.        
        ''',
    },
    {
        'slug': 'coding',
        'image': 'coding.jpg',
        'author': 'Konst',
        'date': date(2022, 10, 2),
        'title': 'Coding',
        'excert': 'Excepteur sint occaecat cupidatat non proident',
        'content': '''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.        
        ''',
    },
    {
        'slug': 'coding_ok',
        'image': 'coding.jpg',
        'author': 'Konst',
        'date': date(2022, 10, 3),
        'title': 'Coding Ok',
        'excert': 'consectetur adipiscing elit',
        'content': '''
           Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
           quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.        
       ''',
    },
]

def sort_date(all_posts):
    return all_posts['date']

def starting_page(request):

    posts = sorted(all_posts,key=sort_date)[-3:]
    return render(request, 'blog/index.html',{'posts':posts})

def posts(request):
    return render(request, 'blog/all-posts.html',{'all_posts':all_posts})

def post_detail(request,slug):
    identified_post = next(i for i in all_posts if i['slug'] == slug )
    return render(request, 'blog/post-detail.html',{'post':identified_post})

