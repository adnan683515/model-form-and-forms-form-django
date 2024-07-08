from django import forms
from model_form_app.models import form


class model_form (forms.ModelForm):
    class Meta:
        model = form
        fields = "__all__"
