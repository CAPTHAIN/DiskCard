from django import forms
from .models import *


class CardForm(forms.ModelForm):
    series = forms.IntegerField(label='Серия', widget=forms.TextInput())
    amount = forms.IntegerField(label='Номер', widget=forms.TextInput())
    end_date = forms.DateField(label='Дата окончания', widget=forms.DateInput(), initial='yyyy-mm-dd')

    class Meta:
        model = Card
        fields = ('series', 'amount', 'end_date')


class ItemForm(forms.ModelForm):
    card = forms.ModelChoiceField(queryset=Card.objects.filter(is_active='Активна'))

    class Meta:
        model = Item
        fields = ('name', 'price', 'card')
