from django import forms
from new.models import New


class NewForm(forms.ModelForm):
    title = forms.CharField(label='標題', max_length=128)
    content = forms.CharField(label='內容', widget=forms.Textarea)

    class Meta:
        model = New
        fields = ['title', 'content']