from django.db import models


class Category(models.Model):
    name = models.CharField(unique=True, blank=False, max_length=200, verbose_name='Kategoriya nomi',
                            help_text='Kategoriya nomini kiriting')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriyalar"
        verbose_name_plural = "Kategoriyalar"


class Product(models.Model):
    measure_choice_option = [
        ('dona', 'dona'),
        ('kg', 'kg'),
    ]

    name = models.CharField(max_length=500, verbose_name='Nomi', help_text='Tovar nomini kiriting')
    descr = models.TextField(blank=False, help_text='Tovar haqida qo\'shimcha ma\'lumot', verbose_name='Tavsif')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoriya',
                            help_text='Tovar kategoriyasini tanlang')
    price = models.PositiveBigIntegerField(blank=False, default=0, help_text='Tovar narxini kiriting',
                                           verbose_name='Narx')
    measure = models.CharField(choices=measure_choice_option, max_length=20, null=False, blank=False,
                               verbose_name='O\'lchov, birlig', help_text='1 dona non, yoki 1 kg olma')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tovarlar"
        verbose_name_plural = "Tovarlar"


class User(models.Model):
    user_name = models.CharField(max_length=200, verbose_name='Nickname')
    tg_id = models.PositiveBigIntegerField(unique=True, null=False, verbose_name='Telegram id')
    user_lang = models.CharField(max_length=5, verbose_name='Tili')
    user_phone = models.CharField(max_length=20, unique=True, verbose_name='Raqam')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "Foydalanuvchilar"
        verbose_name_plural = "Foydalanuvchilar"


class Order(models.Model):
    pay_choice_option = [
        ('Naqd pul', 'cash'),
        ('Click', 'click'),
        ('Payme', 'payme'),
    ]

    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Xaridor')
    pay_type = models.CharField(choices=pay_choice_option, max_length=20, verbose_name='To\'lov turi')
    address = models.TextField(null=True, blank=True, verbose_name='Adres')
    longitude = models.CharField(max_length=20, null=True, blank=True)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    total_price = models.CharField(max_length=50, verbose_name='Umumiy narx')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    # def __str__(self):
    #     return self.user.user_name

    class Meta:
        verbose_name = "Buyurtmalar"
        verbose_name_plural = "Buyurtmalar"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items', verbose_name='Buyurtma')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Tovar')
    quantity = models.IntegerField(verbose_name='Soni')

    def __str__(self):
        return self.product.descr

    class Meta:
        verbose_name = "Buyurtma tovarlar"
        verbose_name_plural = "Buyurtma tovarlar"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class DeliveryPrice(models.Model):
    price = models.PositiveBigIntegerField(null=False, blank=False, verbose_name='Yetkazib berish narxi',
                                           help_text='Yetkazib berish narxini kiriting')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Ohirgi martta o\'zgartirilgan sana')

    class Meta:
        verbose_name = 'Yetkazib berish naxi'
        verbose_name_plural = 'Yetkazib berish naxi'


class Calls(models.Model):
    phone = models.CharField(max_length=100, verbose_name='Aloqa uchun raqamlar')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    class Meta:
        verbose_name = 'Bog\'lanish uchun'
        verbose_name_plural = 'Bog\'lanish uchun'
