from django.urls import path
from .views import *

urlpatterns = [
    path('', CardView.as_view(), name='home'),
    path('add_card', AddCardView.as_view(), name='add_card'),
    path('buy_page', BuyItemsView.as_view(), name='buy_item'),
    path('detail_card/<int:card_pk>/', ShowDetailCard.as_view(), name='show_card'),
    path('detail_card/<int:card_pk>/', ShowDetailCard.as_view(), name='show_card'),
    path('detail_card/change_status/<int:card_pk>/', ChangeView.as_view(), name='change_status'),
    path('detail_card/delete_card/<int:card_pk>/', DeleteView.as_view(), name='delete_card'),
]

status()