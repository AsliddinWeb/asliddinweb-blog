from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog_Post, Comment

# Create your views here.
class Blog_Page(ListView):
    queryset = Blog_Post.objects.all()
    context_object_name = 'blogs'
    paginate_by = 4
    template_name = 'blogs.html'

def blog_detailView(request, slug):
    blogs = Blog_Post.objects.all()
    blog = Blog_Post.objects.get(slug = slug)
    print(blog)
    comments = blog.comments.filter(active=True)
    print(comments)
    new_comment = None

    if request.method == "POST":
        comment = Comment()
        comment.name = request.POST['name']
        comment.body = request.POST['body']
        comment.blog_id = blog.id
        print(comment.name, comment.body, comment.blog_id)
        comment.save()
    len_comments = len(comments)

    ctx = {
        'blogs': blogs,
        'blog': blog,
        'comments': comments,
        'len_comments': len_comments
    }

    return render(request, 'blog_page.html', ctx)

def aloqa_page(request):
    blogs = Blog_Post.objects.all()
    ctx = {
        'blogs': blogs
    }

    return render(request, 'aloqa.html', ctx)