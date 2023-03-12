from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView
from .models import *
from .forms import * 
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

import random



class Index(LoginRequiredMixin,ListView):
    
    login_url = '/accounts/login/'
    paginate_by = 5
    model = Post
    template_name = "index.html"
    context_object_name = "posts"
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        random_idx = random.randint(0, CUser.objects.count() - 1)
        random_object = CUser.objects.order_by('?')[0]
        data['random_user'] = random_object
        return data

class ProfileEdit(UpdateView):
    model = CUser
    template_name = "profileedit.html"
    form_class = ProfileChange

    def dispatch(self, request, *args, **kwargs):
        if self.request.user != self.get_object():
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)
    
def postadd(request):
    if request.method == "POST":
        print(request.POST["name"])
        post = Post(name=request.POST["name"],text=request.POST["text"],author=request.user)
        post.save() # save the post instance 
        # loop over the list of images and save each one to the database
        for img in request.FILES.getlist('images'):
            imgs = Images(img=img)
            imgs.save()
            post.images.add(imgs)
        post.save() # save the post instance again after adding the images
        return redirect("")

    return render(request,"addpost.html")

def parent_comment(request,id):
    comment = Comment.objects.get(pk=int(id))
    print(comment)

    return redirect("/post/"+str(id))

def commentadd(request,id):

    if request.method == "POST":
        comment = Comment(post=Post.objects.filter(pk=int(id))[0],author=request.user,content=request.POST['content'])
        comment.save()

    return redirect("/post/"+str(id))


class PostView(LoginRequiredMixin, DetailView):
    template_name="post.html"
    model=Post
    context_object_name="post"


class Profile(LoginRequiredMixin,DetailView):
    model = CUser
    template_name = "profile.html"
    context_object_name = "userp"
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        user = self.get_object()
        post = Post.objects.filter(author=user)
        data['posts'] = post
        if self.request.user==self.get_object():
            data['edit'] = 1
        return data
    
    
@login_required(login_url='/accounts/login/')
def quest(request):
    return redirect("/feed")







def signup(request):
    if request.user.is_authenticated==False:
        if request.method == 'POST':

            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.refresh_from_db()  
                # load the profile instance created by the signal
                user.save()
                raw_password = form.cleaned_data.get('password1')

                # login user after signing up
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)

                # redirect user to home page
                return redirect('index')
        else:
            form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return redirect("/")
