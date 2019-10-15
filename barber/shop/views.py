from django.shortcuts import render

def post_list(request):
    return render(request, 'shop/post_list.html', {})