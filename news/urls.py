from django.urls import path
from  django.views.generic import  ListView, DeleteView
from news.models import Articles
from . import views



urlpatterns = [
    path(
        '', ListView.as_view(
            queryset=Articles.objects.all().order_by('-date')[:20],
            template_name='news/posts.html'
        )
    ),
]