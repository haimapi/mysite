from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogPost


# Create your views here.
def index(request):
    blog_list = BlogPost.objects.all()
    cont_dict = {}
    cont_dict['all_blog'] = blog_list
    return render(request, 'blog/index.html', cont_dict)


def view_blog(request, slug_title):
    each_list = BlogPost.objects.filter(slug=slug_title)
    cont_dict = {}
    cont_dict['each_blog'] = each_list
    return render(request, 'blog/read.html', cont_dict)