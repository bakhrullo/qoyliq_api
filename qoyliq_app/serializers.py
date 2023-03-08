from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_lang']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    product = ProductSerializer()

    class Meta:
        model = Cart
        fields = '__all__'


class CallsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calls
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryPrice
        fields = '__all__'

