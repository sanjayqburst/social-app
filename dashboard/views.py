from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from dashboard.models import Content
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
# Create your views here.

# @login_required()
# def dashboard(request):
#     current_user=request.user
#     print(current_user)
#     contents=Content.objects
#     return render(request,'dashboard/content.html',{'contents':contents})

@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name='dashboard/content.html'
    extra_context={'contents': Content.objects.all()}

