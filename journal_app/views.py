from django.shortcuts import render, redirect

from .models import Post
from .forms import CommentForm

# Create your views here.


def frontpage(request):
    print('    -> frontpage')
    posts = Post.objects.all()

    return render(request, 'journal_app/frontpage.html', {'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    print('    -> post_detail')
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'journal_app/post_detail.html', {'post': post, 'form': form})
