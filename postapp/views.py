from django.shortcuts import render
from .models import Post, Comment,About
from .forms import CommentForm
from skillapp.models import Skill
# Create your views here.

def for_all_pages(request):
    about = About.objects.all()
    context = {
        'about':about
    }
    return (context)

def PostView(request):
    template_name = 'postapp/list.html'
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, template_name=template_name, context=context)

def getPost(request, pk):
    template_name = 'postapp/detail.html'
    post = Post.objects.get(pk=pk)
    comments = post.comments.all()
    comment_form = CommentForm()
    tags = post.tags.all()

    if request.method=='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            cf = comment_form.save(commit=False)
            cf.post = post
            cf.save()
            comment_form = CommentForm()
            parent_obj = None
            try:
                parent_id = request.POST.get('parentId')
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comment.objects.get(pk=parent_id)
            if parent_obj:
                cr = comment_form.save(commit=False)
                cr.parent = parent_obj
                cr.post = post
                cr.save()
                comment_form = CommentForm()
    context = {'post':post, 'comment_form':comment_form, 'comments':comments, 'tags':tags}
    return render(request, template_name=template_name, context=context)

def getPostsByTag(request, tagName):
    filter = True
    posts = Post.objects.filter(tags__name=tagName).all()
    context = {'postf':posts, 'filter':filter}
    return render(request=request, template_name='postapp/list.html', context=context)


def about(request):
    # about = About.objects.all()
    skills = Skill.objects.all()
    context = {'skills':skills}
    template_name = 'about.html'
    return render(request=request, template_name=template_name, context=context)