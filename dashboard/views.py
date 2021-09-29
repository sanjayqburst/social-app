from django.contrib.auth.models import User
from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.forms import ContentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView
from dashboard.models import Comments, Content
# Create your views here.

# @login_required()
# def dashboard(request):
#     current_user=request.user
#     print(current_user)
#     contents=Content.objects
#     return render(request,'dashboard/content.html',{'contents':contents})


# @method_decorator(login_required, name='dispatch')
class DashboardView(LoginRequiredMixin, TemplateView):
    """
    Method for creating dashboard; (login-required)

    Params:
        TemplateView View: Generate view from template
        template_name: path to template
        extra_context dict: passes data for template to render
    """
    template_name = 'dashboard/dashboard.html'
    extra_context = {'contents': Content.objects.all(
    ), 'comments': Comments.objects.all(), 'user_data': User.objects.all()}


class AddPost(LoginRequiredMixin, CreateView):
    """
    Method for adding new post.

    Parms:
        LoginRequiredMixin Mixin: To confirm user is loged in to post content.
        CreateView View: A view that displays a form for creating an object.

    Returns:
        form: Validates form
    """
    model = Content
    template_name = 'add_post/addpost.html'
    form_class = ContentForm
    # print(Comments.objects.all())
    extra_context = {'comments': Comments.objects.all(),
                     'contents': Content.objects.all()}
    success_url = reverse_lazy('dashboard')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['contents'] = Content.objects.all()
    #     return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)
