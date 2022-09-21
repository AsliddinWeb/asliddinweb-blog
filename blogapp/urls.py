from django.urls import path
from .views import Blog_Page, blog_detailView, aloqa_page



urlpatterns = [
    path('', Blog_Page.as_view(), name='index'),
    path('contact/', aloqa_page, name='aloqa_page'),
    path('blog/<str:slug>', blog_detailView, name='blog_page'),
]