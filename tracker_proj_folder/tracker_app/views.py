from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'tracker_app/home.html', {'user': request.user})

# # Create your views here.
# def about(request):
#     return render(request, 'tracker_app/about.html', {'title': 'About', 'user': request.user})