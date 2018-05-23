from django.shortcuts import render

def index(request):
    return render(request, 'dahmooingcow/home.html')

def videos(request):
	return render(request, 'dahmooingcow/videos.html')
