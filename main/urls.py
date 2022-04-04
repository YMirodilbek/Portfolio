from django.urls import path
from .views import *

urlpatterns = [
    # path('',Align),
    path('', HomeView),
    path('singleBlog',SingleBlog),
    # path('portfolio/<int:day>/<int:month>/<int:year>/<slug:slug>/',PortfolioDetail.as_view),
    # path('portfolio/',PortfolioDetail.as_view()),
    path('Views/<int:pk>',BlogDetail.as_view()),
    path('add-message/',Message),
    path('add-comment/',AddComment),
    path('Batafsil/',Batafsil),

]