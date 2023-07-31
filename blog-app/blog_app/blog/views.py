from django.shortcuts import render

posts = [
    {
        'author': 'Eklal Budhathoki',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2023'
    },
    {
        'author': 'Aziz Hussen',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 27, 2023'
    },
    {
        'author': 'Dhoni Sharma',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'August 27, 2023'
    },
    {
        'author': 'Virat Kohli',
        'title': 'Blog Post 4',
        'content': 'Fourth post content',
        'date_posted': 'August 27, 2023'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})
