from django import forms
from django.forms import ModelForm, fields
from .models import Content


class ContentForm(ModelForm):
    """
    Form for creating new content.
    """

    class Meta:
        model = Content
        
        fields = ['image', 'summary']
    def form_valid(self, form):
        """
        Method for validating form and adding current user.

        return validated_form form: return validated form data.
        """
        form.instance.created_by = self.request.user
        return super().form_valid(form)