from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from blog.models import Blog
from .forms import SignUpForm, LogInForm, CreateBlogForm, AuthorProfileForm
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from portfolio.models import Author


class DisplayHome(TemplateView):
    template_name = 'portfolio/home.html'


class AuthorPageView(ListView):
    template_name = 'portfolio/author_page.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'blogs'
    paginate_by = 2

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user).order_by('-date_created')


class DisplayAuthors(ListView):
    template_name = 'portfolio/authors_list.html'
    context_object_name = 'authors'

    def get_queryset(self):
        return Author.objects.all().order_by('Name')


class PersonalProfile(ListView):
    template_name = 'portfolio/author_profile.html'
    context_object_name = 'authors'

    def get_queryset(self):
        return Author.objects.filter(username=self.request.user)


class CreateProfile(CreateView):
    form_class = AuthorProfileForm
    template_name = 'portfolio/author_create.html'
    success_url = reverse_lazy('personalprofile')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.username = self.request.user
        self.object.save()
        return super().form_valid(form)


class UpdateProfile(UpdateView):
    form_class = AuthorProfileForm
    pk_url_kwarg = 'pk'
    model = Author
    template_name = 'portfolio/author_update.html'
    success_url = '/personalprofile/'


class CreateBlog(CreateView):
    form_class = CreateBlogForm
    template_name = 'portfolio/create.html'
    success_url = reverse_lazy('authorpage')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class UpdateBlog(UpdateView):
    form_class = CreateBlogForm
    pk_url_kwarg = 'pk'
    model = Blog
    template_name = 'portfolio/update.html'
    success_url = '/authorpage/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.date_updated = timezone.now()
        self.object.save()
        return super().form_valid(form)


class DeleteBlog(DeleteView):
    pk_url_kwarg = 'pk'
    model = Blog
    success_url = '/authorpage/'


def signupuser(request):
    context = {'form': SignUpForm()}
    if request.method == 'GET':
        return render(request, 'portfolio/signup.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'],
                                                email=request.POST['email'])
                user.save()
                ##### uncomment this to send mail#######
                # subject = 'Welcome To Bloggest Family!'
                # message = 'Thank you for joining Bloggest.! you can immedietely log in and start writing blogs. Happy Writing!'
                # from_email = settings.EMAIL_HOST_USER
                # to_list = [request.POST['email'],]
                # send_mail(subject=subject, message=message, from_email=from_email, recipient_list=to_list, fail_silently=True)
                login(request, user)
                return redirect('blog:bloglist')
            except IntegrityError:
                context = {'form': SignUpForm(), 'error': ' The username already exists. Please try again!'}
                return render(request, 'portfolio/signup.html', context)
        else:
            context = {'form': SignUpForm(), 'error': ' The passwords do not match. Try again!'}
            return render(request, 'portfolio/signup.html', context)


def loginuser(request):
    context = {'form': LogInForm()}
    if request.method == 'GET':
        return render(request, 'portfolio/login.html', context)
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            context = {'form': LogInForm(), 'error': 'The username or password did not match'}
            return render(request, 'portfolio/login.html', context)
        else:
            login(request, user)
            return redirect('authorpage')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
