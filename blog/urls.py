from django.urls import path
from .views import BlogView, DetailView

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='bloglist'),
    path('details/<int:pk>', DetailView.as_view(), name='detailview'),
    ]