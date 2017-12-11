# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="类别名称")

    # python2使用__unicode__, python3使用__str__
    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="标签名称")

    # python2使用__unicode__, python3使用__str__
    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name="文章标题")

    # 文章正文，我们使用了 TextField。
    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    body = models.TextField(verbose_name="文章内容", default='')

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField(verbose_name="创建时间")
    modified_time = models.DateTimeField(verbose_name="修改时间")

    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField(max_length=200, blank=True, verbose_name="摘要")
    '''
    这是分类与标签，分类与标签的模型我们已经定义在上面。
    我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一对多的关联关系。
    而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
    如果你对 ForeignKey、ManyToManyField 不了解，请看教程中的解释，亦可参考官方文档：
    https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
    '''
    category = models.ForeignKey(Category, verbose_name="分类")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u"标签")
    '''
    文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    这里我们通过 ForeignKey 把文章和 User 关联了起来。
    因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    '''
    author = models.ForeignKey(User, verbose_name="作者")
    # 浏览量
    # views = models.PositiveIntegerField(default=0, verbose_name="浏览量")

    # python2使用__unicode__, python3使用__str__
    def __unicode__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('article:detail', kwargs={'pk': self.pk})  # reverse的第一个参数是urls.py的url中的name, blogdetail

    class Meta:
        ordering = ['-created_time']  # 列表中可以用多个项，比如 ordering = ['-created_time', 'title'] ，那么首先依据 created_time 排序
