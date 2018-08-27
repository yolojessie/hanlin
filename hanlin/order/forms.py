from django import forms
from order.models import Order
from cProfile import label


PAYMETHOD = [('ATM','ATM'), ('貨到付款','貨到付款'), ('PChome','PChome')]
class OrderForm(forms.ModelForm):
    name = forms.CharField(label='姓名', max_length=128)
    phone = forms.CharField(label='手機', max_length=128)
    address = forms.CharField(label='地址', max_length=128)
    email = forms.EmailField(label='信箱')
    payMethod = forms.ChoiceField(label='付款方式', choices=PAYMETHOD, widget=forms.RadioSelect())
    
    class Meta:
        model = Order
        exclude = ['customer','pubDateTime','plant','totalPrice']