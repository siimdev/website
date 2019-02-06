from django.shortcuts import render
from .models import Post

# posts = [
#     {
#         'author': 'Siim',
#         'title': 'Esimene postitus',
#         'content': 'Esimese postituse sisu',
#         'date_posted': '1. Jaanuar 2019'
#     },
#     {
#         'author': 'Siim',
#         'title': 'Teine postitus',
#         'content': 'Teise postituse sisu',
#         'date_posted': '10. Jaanuar 2019'
#     }
# ]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'Meist'})
