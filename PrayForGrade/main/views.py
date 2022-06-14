from django.shortcuts import render, redirect
from .models import Post
# Create your views here.
def home(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'main/home.html', {'postlist':postlist})

# blog의 게시글(detail)을 부르는 detail 함수
def detail(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # detail.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/detail.html', {'post':post})

def new_post(request):
    if request.method == 'POST':
        new_article=Post.objects.create(
            username=request.POST['username'],
            subject=request.POST['subject'],
            grade=request.POST['grade'],
            term=request.POST['term'],
        )
        return redirect('/')
    return render(request, 'main/new_post.html')