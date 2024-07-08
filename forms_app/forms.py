from django import forms
import datetime
# Create your forms here.

class ExampleForm(forms.Form):
    
    name= forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    about = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    check = forms.BooleanField()
    date = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    day = forms.DateField(initial=datetime.date.today)
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES,widget=forms.RadioSelect)
    multi_color = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES,widget=forms.CheckboxSelectMultiple)
