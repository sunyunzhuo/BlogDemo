# -*- coding: utf-8 -*-
import markdown
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.http import HttpResponse
from .models import Article, Category
from comments.forms import CommentForm
# def index(request):
#     return render(request, 'article\index.html', context={
#                       'title': '我的博客首页',
#                       'welcome': '欢迎访问我的博客首页'
#                   })


def index(request):
    article_list = Article.objects.all()
    return render(request, 'article/index.html', context={'article_list': article_list})


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.body = markdown.markdown(article.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = article.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': article,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'article/detail.html', context=context)


def archives(request, year, month):
    article_list = Article.objects.filter(created_time__year=year, created_time__month=month)
    return render(request, 'article/index.html', context={'article_list': article_list})


def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    article_list = Article.objects.filter(category=cate)
    return render(request, 'article/index.html', context={'article_list': article_list})