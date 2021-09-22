from dashboard.models import Content
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# Create your views here.

@login_required()
def dashboard(request):
    current_user=request.user
    print(current_user)
    contents=Content.objects
    return render(request,'dashboard/content.html',{'contents':contents,'user':current_user})