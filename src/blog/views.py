from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import CreatePostModelForm
#from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def blogpost(request, slug):
    template_name = 'blog/blogpost.html'
    blogpost_obj = get_object_or_404(BlogPost,slug=slug)
    context = {"object": blogpost_obj}
    return render(request, template_name, context)

def post_list(request):
    template_name = 'blog/post_list.html'
    post_list = BlogPost.objects.all()
    context = {"objects": post_list}
    return render(request, template_name, context)

@staff_member_required
def create_post(request):
    template_name = "blog/blogpost_form.html"
    form = CreatePostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        form = CreatePostModelForm()
    context = {
        "form": form,
        "title": "Create New Post",
        "button_text": "Create Post",
        "button_class": "btn btn-primary"
        }
    return render(request,template_name,context)

@staff_member_required
def update_post(request, slug):
    template_name = "blog/blogpost_form.html"
    blogpost_obj = get_object_or_404(BlogPost, slug=slug)
    form = CreatePostModelForm(request.POST or None, instance=blogpost_obj)
    if form.is_valid():
        form.save()
    context = {
        "title": f"Update {blogpost_obj.title}",
        "form": form,
        "button_text": "Update",
        "button_class": "btn btn-primary"
        }
    return render(request, template_name, context)

@staff_member_required
def delete_post(request, slug):
    template_name = "blog/blogpost_form.html"
    blogpost_obj = get_object_or_404(BlogPost, slug=slug)
    form = CreatePostModelForm(request.POST or None, instance=blogpost_obj)
    if request.method == "POST":
        blogpost_obj.delete()
        return redirect('/blog')
    context = {
        "title": "Do you want to delete this post?" ,
        "form": form,
        "button_text": "Delete Post",
        "button_class": "btn btn-danger"
        }
    return render(request, template_name, context)