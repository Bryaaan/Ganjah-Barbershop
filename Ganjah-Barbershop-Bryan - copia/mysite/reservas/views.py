from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import reservform
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(fecha_reserva__lte=timezone.now()).order_by('fecha_reserva')
    return render(request, 'reservas/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'reservas/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = reservform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = reservform()
    return render(request, 'reservas/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = reservform(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = reservform(instance=post)
    return render(request, 'reservas/post_edit.html', {'form': form})