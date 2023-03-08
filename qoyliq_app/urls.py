from django.urls import path

from .views import *


urlpatterns = [
    path('api/v1/user/create', UserCreateView.as_view()),
    path('api/v1/user/update/<int:tg_id>', UserUpdateView.as_view()),
    path('api/v1/category/', CategoryListView.as_view()),
    path('api/v1/calls/', CallsGetView.as_view()),
    path('api/v1/product/', ProductListView.as_view()),
    path('api/v1/order/', OrderCreateView.as_view()),
    path('api/v1/order/get/', OrderGetView.as_view()),
    path('api/v1/cart/<int:tg_id>', CartGetView.as_view()),
    path('api/v1/cart/update', CartUpdateView.as_view()),
    path('api/v1/delivery', DeliveryGetView.as_view()),
]
