from django.contrib.auth.models import User
from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.forms import CommentForm, ContentForm
from django.views.generic import CreateView
from dashboard.models import Comment, Content
# Create your views here.




class DashboardView(LoginRequiredMixin, CreateView):
    """
    Method for creating dashboard; (login-required)

    Params:
        template_name: path to template
        extra_context dict: passes data for template to render
    """

    model=Comment
    form_class=CommentForm
    template_name = 'dashboard/dashboard.html'
    success_url=reverse_lazy('dashboard')
    my_model_content=Content.objects.all()
    extra_context = {'contents': Content.objects, 'comments': Comment.objects, 'user_data': User.objects.all()}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.commented_by = self.request.user
        # print(self.request.POST.get('post_id'))
        content_id=self.request.POST.get('post_id')
        self.object.post_id = Content.objects.get(id=content_id)
        self.object.save()
        # print(form)
        return super().form_valid(form)





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
    commented=Comment.objects.all()
    contents_is=Content.objects.all()
    # print(Comments.objects.all())
    extra_context = {'comments': commented,
                     'contents': contents_is}
    success_url = reverse_lazy('dashboard')


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)



# def createComment(request):
#     """
#     Method for creating comment using ajax

#     """
#     if request=="POST":
#         post_id=request.POST['post_id']
#         commnet_body=request.POST['comment']
#         commented_by=request.user

#         Comments.objects.create(
#             post_id=post_id,
#             comment=commnet_body,
#             commented_by=commented_by
#         )

#     return HttpResponse("Response added")