from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post, RePost
from .forms import PostForm, RePostForm, UserForm, NewForm

# Create your views here.

@login_required
def post_list(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': post})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    repost = RePost.objects.filter(post=post).order_by('-published_date')
    return render(request, 'blog/post_detail.html', {'post': post, 'repost': repost})

@login_required
def post_new(request):
    if request.method == 'POST':
        # with open('./1.txt', 'a') as f:
        #     f.write(str(request.POST))
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_reply(request, pk):
    if request.method == 'POST':
        reform = RePostForm(request.POST)
        post = get_object_or_404(Post, pk=pk)
        if reform.is_valid():
            repost = reform.save(commit=False)
            repost.post = post
            repost.author = request.user
            repost.published_date = timezone.now()
            repost.save()
            return redirect('post_detail', pk=pk)
    else:
        reform = RePostForm()
    return render(request, 'blog/post_reply.html', {'reform': reform})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
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

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

#注册
def regist(requset):
    if requset.method == 'POST':
        form = NewForm(requset.POST)
        if form.is_valid():
            # 获取用户名,密码,邮箱
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            #查询数据库是否有相同用户
            user = auth.authenticate(username = username, password = password)
            if user:
                return redirect('regist')
            user = User.objects.create_user(username = username, password = password, email = email)
            user.save()
            # requset.session['username'] = username
            # auth.login(requset, user)
            return redirect('login')
    else:
        form = NewForm()
    return render(requset, 'online/regist.html', {'form': form})

#登陆
def login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            #获取用户名和密码
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #将获取用户名和密码与数据库比较
            user = auth.authenticate(username = username, password = password)
            if user:
                auth.login(request, user)
                request.session['username'] = username
                return redirect('post_list')
            else:
                return redirect('login')
    else:
        form = UserForm()
    return render(request, 'online/login.html', {'form': form})

#登出
def logout(request):
    auth.logout(request)
    return redirect('login')
