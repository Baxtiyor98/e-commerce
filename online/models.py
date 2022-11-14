from django.db import models
from user.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="Products/%d/%m/%Y")
    price = models.FloatField()
    discount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    @property
    def discount_price(self):
        return self.price*(1-(self.discount/100))

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, related_name="user_cart", on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, null=True, blank=True)
    total_price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_summa(self):
        self.total_price = sum(self.order_product.values_list('order_price', flat=True))
        self.save()
        return self.total_price

    def __str__(self):
        return self.user.username


class Order_Product(models.Model):
    cart = models.ForeignKey(Cart, related_name="order_product", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def summa(self):
        self.order_price = self.product.discount_price * self.quantity
        self.save()

    def __str__(self):
        return self.product.name