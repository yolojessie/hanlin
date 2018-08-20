from django import forms
from shop.models import Branch, Plant
from cProfile import label

class BranchForm(forms.ModelForm):
    branchName = forms.CharField(label='種類名', max_length=128)
    url = forms.CharField(label='圖片檔名', max_length=128)
    
    class Meta:
        model = Branch
        fields = ['branchName','url']
        

class PlantForm(forms.ModelForm):
    plantName = forms.CharField(label='品名', max_length=128)
    code = forms.CharField(label='編號', max_length=128)
    price = forms.IntegerField(label='價格',)
    inventory = forms.IntegerField(label='庫存')
    url = forms.CharField(label='圖片檔名', max_length=128)
    
#     def save(self, commit=True):
#         plant = super(PlantForm, self).save(commit=False)
    
    class Meta:
        model = Plant
        exclude = ['branch', 'pubDateTime']
        
        