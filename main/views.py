from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import *
from .models import *
from datetime import date


def status():
    cards = Card.objects.all()
    for card in cards:
        if card.end_date < date.today():
            Card.objects.filter(pk=card.id).update(is_active='Просрочена')


class CardView(ListView):
    model = Card
    template_name = 'main/cards.html'
    context_object_name = 'cards'

    def get_queryset(self):
        if self.request.GET.get('q'):
            query = self.request.GET.get('q')
            cards = Card.objects.filter(
                Q(series__icontains=query) | Q(amount__icontains=query) | Q(end_date__icontains=query)
                | Q(is_active__icontains=query)
            )
        else:
            cards = Card.objects.all()
        return cards


class AddCardView(CreateView):
    form_class = CardForm
    template_name = 'main/add_card.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()

        return redirect('home')


class BuyItemsView(CreateView):
    form_class = ItemForm
    template_name = 'main/items.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save(commit=False)
        card_pk = int(form['card'].value())
        card = Card.objects.get(pk=card_pk)
        card.use_date = Card.objects.filter(pk=card_pk).update(use_date=date.today())
        card_sum = int(card.card_sum) + int(form['price'].value())
        card.card_sum = Card.objects.filter(pk=card_pk).update(card_sum=card_sum)
        form.save()
        return redirect('home')


class ShowDetailCard(DetailView):
    model = Card
    template_name = 'main/show_card.html'
    pk_url_kwarg = 'card_pk'
    context_object_name = 'card'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        card = Card.objects.get(pk=self.kwargs['card_pk'])
        context['card'] = card
        context['items'] = Item.objects.filter(card=Card.objects.get(pk=self.kwargs['card_pk']))
        if card.end_date < date.today():
            Card.objects.filter(pk=self.kwargs['card_pk']).update(is_active='Просрочена')

        return context


class ChangeView(UpdateView):
    model = Card
    template_name = 'main/update_page.html'
    pk_url_kwarg = 'card_pk'
    success_url = reverse_lazy('home')
    fields = ['is_active']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DeleteView(DeleteView):
    model = Card
    pk_url_kwarg = 'card_pk'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
