from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Blog, About, History, How_it_works, Our_Team, Comment, Category, Tag
from .forms import CommentForm


def blog_page(reqs):
    blogs = Blog.objects.all().order_by('-id')
    hiw = How_it_works.objects.all()
    page_number = reqs.GET.get('page')
    p = Paginator(blogs, 1)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {
        'blogs': blogs,
        'hiws': hiw,
        'page_obj': page_obj
    }
    return render(reqs, 'blog.html', context)


def about_page(req):
    abouts = About.objects.all().order_by('-id')[:1]
    teams = Our_Team.objects.all().order_by('-id')[:6]
    history = History.objects.all().order_by('-id')[:1]
    hiw = How_it_works.objects.all()
    context = {
        'abouts': abouts,
        'teams': teams,
        'historyies': history,
        'hiws': hiw
    }
    return render(req, 'about.html', context)


def blog_single(req, pk=None):
    obj = Blog.objects.get(id=pk)
    cat = Category.objects.all()
    # tag = Tag.objects.get('tag')
    form = CommentForm(req.POST or None, req.FILES)
    if form.is_valid():
        com = form.save(commit=False)
        com.blog = obj
        com.save()
    context = {
        'obj': obj,
        'cat': cat,
        # 'tag': tag
        'form': form
    }
    return render(req, 'single.html', context)
