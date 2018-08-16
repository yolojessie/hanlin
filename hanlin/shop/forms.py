from django import forms
from shop.models import Branch, Plant
from cProfile import label

class BranchForm(forms.ModelForm):
    branchName = forms.CharField(label='種類名', max_length=128)
    url = forms.CharField(label='圖片檔名', max_length=128)
    
    class Meta:
        model = Branch
        fields = ['branchName','url']