from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['name', 'age', 'title', 'hometown']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'hometown': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Name',
            'age': 'Age',
            'title': 'Title',
            'hometown': 'Hometown',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['title'].required = True