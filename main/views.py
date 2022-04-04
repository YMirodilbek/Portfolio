from email import message
from pyexpat import model
from pyexpat.errors import messages
from django.contrib import messages
from urllib.request import HTTPRedirectHandler
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from pytz import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .models import *
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required





def Align(request):
    return render(request,'base.html')
def HomeView(request):
    
    c_id = request.GET.get('c_id')
    ip=request.META.get('REMOTE_ADDR')
    print(ip)
    context = {
        'info':Info.objects.first(),
        'smedia':SMedia.objects.all(),
        'skills':Skills.objects.all(),
        'bio':Bio.objects.first(),
        'slide':Slider.objects.all(),
        'post':Post.objects.all(),
        'price':Price.objects.all(),
        'love':Love.objects.all(),
        'lang':Languages.objects.all(),
        'fact':Fact.objects.all(),
        'edu':Resume.objects.filter(is_education = True),
        'exp':Resume.objects.filter(is_education = False),
        'category':Category.objects.all(),
        'portfolio':Port.objects.all(),
        'blogs':Portfolios.objects.all(),
        'comment':CommentOfPortfolio.objects.all().order_by('id'),
        "reply":Reply.objects.all().order_by('-id'),
        'c_id':c_id,
    }
    return render(request, 'index.html', context)

# class PortfoliofDetail(DetailView):
#     model = Portfolios
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context= super().get_context_data(self, **kwargs)
#         context['NOW'] = timezone.now()

#         ip = self.request.META.get('REMOTE_ADDR ')
#         print(ip)
#         if self.objects.ips is not None:

#             if ip in self.objects.ips:
#                 pass

#             else:
#                 self.objects.ips += ip + " "
#                 self.objects.views_count()
#         else:
#             self.objects.ips += ip + " "
#             self.objects.views_count()

#         return context
         


def SingleBlog(request):
    return render(request,'single_blog.html')


def e404(request):
    return render(request,'404.html')

class BlogDetail(DetailView):

    model = Portfolios
    template_name = 'index.html'
    context_object_name = 'Portfolios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = Info.objects.first(),

        ip = self.request.META.get('REMOTE_ADDR')
        print(ip)
        if self.object.ips is not None:
            if ip in self.object.ips:
                pass
            else:
                self.object.ips += ip + ' '
                self.object.views_count()
        else:
            self.object.ips = ip + ' '
            self.object.views_count()
        
        print(ip)

        return context
@login_required
def Message(request):
    r = request.POST
    name = r['full_name']
    email = r['email']
    subject = r['subject']
    phone = r['phone']
    msg = r['message']
    Messages.objects.create(name=name, email=email, subject=subject,phone=phone ,msg=msg)

    info = '<strong>{}</strong>. Xabaringiz Yuborildi! , Tez orada aloqaga chiqamiz'.format(name)
    messages.success(request,info)
    return redirect('/#contact')

# class PortfolioDetail(DetailView):
    # model = Portfolios
    # template_name = 'index.html'
    # context_object_name = 'portfolio'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['info'] = Info.objects.first(),

    #     ip = self.request.META.get('REMOTE_ADDR')
    #     if self.object.ips is not None:
    #         if ip in self.object.ips:
    #             pass
    #         else:
    #             self.object.ips += ip + ' '
    #             self.object.views_count()
    #     else:
    #         self.object.ips = ip + ' '
    #         self.object.views_count()
        
    #     print(ip)

    #     return context


@login_required()
def AddComment(request):
    r=request.POST
    # portfolio =r['portfolio']
    comment = r['comment']
    CommentOfPortfolio.objects.create( text=comment)
    
    
    # port = Portfolios.objects.get(id=portfolio)
    return redirect("/#Batafsil")

    # return redirect(f'/portfolio/{port.date.strftime("%d")}/{port.date.strftime("%m")}/{port.date.strftime("%Y")}/{port.slug}/')

# @property
# def children(self):
#     return CommentOfPortfolio.objects.filter(parent=self).reverse()

def Batafsil(request):
    ip = request.META.get('REMOTE_ADDR')
    print(ip)
    r=request.POST
    return redirect("/#Batafsil")

def customhandler404(request, exception, template_name='404.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print("this user is not authenticated")
            return redirect('/login/')
            

    return render(request, 'login.html')

def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user = authenticate(request, username=username, password=password)
        if user is None:
            user = User.objects.create(username=username, password=make_password(password), first_name=first_name, last_name=last_name)
            login(request, user)
            return redirect('/')
        else:
            return redirect('/register/')

    return render(request, 'register.html')


def Logout(request):
    logout(request)
    return redirect('/login/')