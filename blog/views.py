from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

# 매개변수 request(사용자가 요청하는 모든 것)와 'blog/post_list.html' 템플릿
def post_list(request):
    # 뷰가 템플릿에서 모델을 선택하도록
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})