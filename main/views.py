from email import message
from pyexpat import model
from django.shortcuts import render,redirect
from pytz import timezone
from .models import *
from django.views.generic import DetailView
# from django import Response

def HomeView(request):
    
    c_id = request.GET.get('c_id')
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

class ResumeDetail(DetailView):
    model = Resume
    template_name = 'index.html'
    context_object_name = 'Resume'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = Info.objects.first(),

        ip = self.request.META.get('REMOTE_ADDR')
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

def Message(request):
    r = request.POST
    name = r['full_name']
    email = r['email']
    subject = r['subject']
    phone = r['phone']
    msg = r['message']
    Messages.objects.create(name=name, email=email, subject=subject,phone=phone ,msg=msg)
    return redirect('/#contact')

class PortfolioDetail(DetailView):
    model = Portfolios
    template_name = 'index.html'
    context_object_name = 'portfolio'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = Info.objects.first(),

        ip = self.request.META.get('REMOTE_ADDR')
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