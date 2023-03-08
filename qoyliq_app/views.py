from rest_framework import status
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CartGetView(ListAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def get_queryset(self):
        tg_id = self.kwargs['tg_id']
        user = User.objects.get(tg_id=tg_id)
        return Cart.objects.filter(user=user)


class CartUpdateView(APIView):
    def post(self, request):
        tg_id, option = request.data['tg_id'], request.data['option']
        prod_id, quan = request.data['prod_id'], request.data['quan']
        user = User.objects.get(tg_id=tg_id)
        if option:
            cart, created = Cart.objects.get_or_create(user=user, product_id=prod_id, defaults={'quantity': quan})
            if not created:
                cart.quantity += quan
                cart.save()
        else:
            Cart.objects.get(user=user, product_id=prod_id).delete()
        return Response(data={"status": "Updated"}, status=status.HTTP_200_OK)


class UserUpdateView(RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer
    lookup_field = 'tg_id'
    queryset = User.objects.all()


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        cat_id, prod_id = self.request.query_params.get('cat_id'), self.request.query_params.get('prod_id')
        if prod_id:
            return Product.objects.filter(id=prod_id)
        else:
            return Product.objects.filter(cat=cat_id)


class OrderCreateView(APIView):
    def post(self, request):
        tg_id = request.data['tg_id']
        pay_type = request.data['pay_type']
        address = request.data['address']
        longitude = request.data['longitude']
        latitude = request.data['latitude']
        total_price = request.data['total_price']
        order_items = request.data['order_items']
        user = User.objects.get(tg_id=tg_id)
        new_order = Order.objects.create(user=user, pay_type=pay_type, address=address, longitude=longitude,
                                         latitude=latitude, total_price=total_price)
        for i in order_items:
            OrderItem.objects.create(order=new_order, product_id=i['prod_id'], quan=i['quan'])
        return Response(data={"status": "Created"}, status=status.HTTP_200_OK)


class OrderGetView(ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        tg_id = self.request.query_params.get("tg_id")
        user = User.objects.get(tg_id=tg_id)
        return Order.objects.filter(user=user)


class CallsGetView(ListAPIView):
    serializer_class = CallsSerializer
    queryset = Calls.objects.all()

    def has_delete_permission(self, request, obj=None):
        return False


class DeliveryGetView(ListAPIView):
    serializer_class = DeliverySerializer
    queryset = DeliveryPrice.objects.all()

    def has_delete_permission(self, request, obj=None):
        return False

    # def has_add_permission(self, request):
    #     return False