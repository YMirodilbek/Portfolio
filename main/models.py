from argparse import _MutuallyExclusiveGroup
from os import truncate
from tkinter import CASCADE
from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Info(models.Model):
    fi = models.CharField(max_length=50)
    staff = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='info')
    gmail = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    birthday = models.DateField()
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.fi
    

class SMedia(models.Model):
    cls = (
        ("fac", "fac"),
        ("twi", "twi"),
        ("dri", "dri"),
        ("ins", "ins"),
    )
    name = models.CharField(max_length=25)
    icon = models.CharField(max_length=25)
    color = models.CharField(choices=cls, max_length=3)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Skills(models.Model):
    tech = models.CharField(max_length=50)
    percent = models.IntegerField()

    def __str__(self):
        return self.tech

class Bio(models.Model):
    text = models.TextField()
    text2 = models.TextField()
    text3= models.CharField(max_length=10000)

    def __str__(self):
        return self.text   

class Slider(models.Model):
    icon = models.CharField(max_length=80)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=60)
    site = models.CharField(max_length=60)
    text = models.TextField(null=True)

    def __str__(self):
        return self.name

class Price(models.Model):
    icon = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    text = models.TextField()
    price= models.FloatField()


    def __str__(self):
        return self.title

class Love(models.Model):
    icon = models.CharField(max_length=60)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Languages(models.Model):
    language = models.CharField(max_length=60)
    span = models.CharField(max_length=60)
    level = models.CharField(max_length=60)
    score = models.CharField(max_length=60)

    def  __str__(self):
        return self.language

class Fact(models.Model):
    int = models.IntegerField()
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title

class Resume(models.Model):
    icon=models.CharField(max_length=60)
    title = models.CharField(max_length=90)
    begin = models.DateField()
    end=models.DateField(null=True)
    grade = models.CharField(max_length=70)
    is_education = models.BooleanField()
    text=models.TextField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title    

    def views_count(self):
        self.viewers += 1
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Port(models.Model):
    image=  models.ImageField(upload_to='media/')
    title = models.CharField(max_length=60)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Messages(models.Model):
    name = models.CharField(max_length=60,null=True,blank=True)
    subject = models.CharField(max_length=60,null=True,blank=True)
    email = models.CharField(max_length=60,null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)
    msg = models.TextField()

    def __str__(self):
        return self.name

class Portfolios(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='port_cat',null=True,blank=True)
    title = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True)
    date = models.DateField()
    text = models.TextField(null=True)
    image = models.ImageField(upload_to='media')
    viewers = models.IntegerField(default=0,null=True)
    ips = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.city

    def views_count(self):
        self.viewers += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.city)
        super(Portfolios, self).save(*args, **kwargs)

class CommentOfPortfolio(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    # portfolios = models.ForeignKey(Portfolios, on_delete=models.CASCADE, related_name='com_port',null=True,blank=True)
    text = models.TextField(null=True)
    reply = models.CharField(max_length=900,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)


    def __str__(self):
        return self.text


class Reply(models.Model): 
    name = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    # portfolios = models.ForeignKey(Portfolios, on_delete=models.CASCADE, related_name='com_port',null=True,blank=True)
    text = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)


    def __str__(self):
        return self.text
    


    
    
    
    
