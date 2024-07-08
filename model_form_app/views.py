from django.shortcuts import render
from model_form_app import forms
# Create your views here.
def model_form(request):
    if request.method == 'POST':
        form = forms.model_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = forms.model_form()
        
    return render(request,'model_form.html',{"form":form})