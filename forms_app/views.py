from django.shortcuts import render
from forms_app import forms
# Create your views here.

def form(request):
    if request.method == 'POST':
        form = forms.ExampleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = forms.ExampleForm()
        
    return render(request,'model_form.html',{"form":form})