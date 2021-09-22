from django.http import response
from django.shortcuts import redirect, render
from . import forms
from social import settings
# Create your views here.




def register_view(request):
    form=forms.CreatedUserForm()
    print(forms)
    if request.method=='POST':
        form=forms.CreatedUserForm(request.POST)
        if form.is_valid():
            form.save()
            print('saved')
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request,'signup.html',{'form':form})

