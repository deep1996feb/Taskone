from django.urls import path

from cart.models import OrderDetails
from .views import CartItemView, CartUpdateView, CartDeleteView, CartItemAddView, OrderDetails
urlpatterns = [
    path('cartitemsadd/', CartItemAddView.as_view()),
    path('cartitems/<int:id>', CartItemView.as_view()),
    path('cartupdate/<int:id>', CartUpdateView.as_view()),
    path('cartdelete/<int:id>', CartDeleteView.as_view()),
    path('cartitems/', CartItemView.as_view()),
    path('cartitems/order/', OrderDetails.as_view()),
]
