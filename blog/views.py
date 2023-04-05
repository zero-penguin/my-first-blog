from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

#post_detailのビューの追加
def post_detail(request, pk):
    #page not foundに対して
    post = get_object_or_404(Post, pk=pk)
    #post_detail.htmlのテンプレートを返す。。
    return render(request, 'blog/post_detail.html', {'post': post})