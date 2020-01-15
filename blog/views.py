from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# <<매개변수 request(사용자가 요청하는 모든 것)와 'blog/post_list.html' 템플릿>>
def post_list(request):
    # 뷰가 템플릿에서 모델을 선택하도록
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
# <<다른 페이지로 넘어가게 하는 것>>
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
# <<폼 작성 -> 폼 데이터 저장(새로운 글 작성)>>
def post_new(request):
    # 폼에 입력된 데이터를 가지고 오기
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)   # commit=False란 넘겨진 데이터를 바로 Post 모델에 저장하지는 말라는 뜻
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)   # post_detail페이지로 이동
    # 빈 칸 폼
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
# <<폼 수정하기>>
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})