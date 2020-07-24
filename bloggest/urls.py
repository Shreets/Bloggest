"""bloggest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from portfolio import views
from portfolio.views import UpdateBlog,DisplayHome, AuthorPageView,CreateBlog,DeleteBlog,DisplayAuthors,PersonalProfile, CreateProfile,UpdateProfile
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('', DisplayHome.as_view(), name='home'),
    path('authors/', DisplayAuthors.as_view(), name='authors'),
    path('personalprofile/', login_required(PersonalProfile.as_view()), name='personalprofile'),
    path('authorpage/', login_required(cache_page(60*60)(AuthorPageView.as_view())), name='authorpage'),
    path('create/', login_required(CreateBlog.as_view()), name='create'),
    path('createprofile/', login_required(CreateProfile.as_view()), name='createprofile'),
    path('update/<int:pk>', login_required(UpdateBlog.as_view()), name='updateblog'),
    path('updateprofile/<int:pk>', login_required(UpdateProfile.as_view()), name='updateprofile'),
    path('delete/<int:pk>', login_required(DeleteBlog.as_view()), name='deleteblog'),
    path('blog/', include('blog.urls', namespace='blog')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)