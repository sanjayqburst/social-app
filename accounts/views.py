from django.http import response
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from . import forms

from social import settings
# Create your views here.


class RegisterView(CreateView):
    """
    Method to create new user

    Params:
        CreateView View: [description]
    """
    template_name = 'signup.html'
    success_url = reverse_lazy('dashboard')
    form_class = forms.CreatedUserForm
    success_message = "Your profile was created successfully"
    


# def register_view(request):
#     form = forms.CreatedUserForm()
#     print(forms)
#     if request.method == 'POST':
#         form = forms.CreatedUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print('saved')
#             return redirect(settings.LOGIN_REDIRECT_URL)
#     return render(request, 'signup.html', {'form': form})
