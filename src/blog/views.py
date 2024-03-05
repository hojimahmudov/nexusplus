from django.db.models import Count, F
from django.shortcuts import render
from blog.models import Post, Comments
from .forms import CommentForm


def blog_list(request):
    posts = Post.objects.annotate(
        comment_count=Count("comments"),
        author_name=F("author__username")
    ).values('id', 'title', 'contents', 'image', 'post_date', 'comment_count', 'author_name')

    context = {
        "posts": posts
    }

    return render(request, 'blog.html', context)


def blog_content(request, pk):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.post = Post.objects.get(id=pk)
            comment.author = request.user
            comment.save()
    form = CommentForm()
    posts = Post.objects.annotate(
        comment_count=Count("comments"),
        author_name=F("author__username")
    ).filter(pk=pk).values('id', 'title', 'contents', 'image', 'post_date', 'comment_count', 'author_name')

    comments = Comments.objects.filter(post_id=pk).select_related('author').order_by('-comment_date')
    context = {
        "posts": posts[0],
        "comments": comments,
        "form": form
    }
    return render(request, 'blog_detail.html', context)
