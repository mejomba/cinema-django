from django.db import models


class User(models.Model):
    username = models.CharField()
    password = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.CharField()
    

class Product(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    inventory = models.IntegerField()

    def increase_inventory(self, amount):
        pass

    def decrease_inventory(self, amount):
        pass


class Customer(models.Model):
    user = User
    phone = models.CharField(max_length=20)
    address = models.TextField()
    balance = models.IntegerField()

    def deposit(self, amount):
        pass

    def spend(self, amount):
        pass


class OrderRow(models.Model):
    product = Product
    order = Order
    amount = models.IntegerField()


class Order(models.Model):
    # Status values. DO NOT EDIT
    STATUS_SHOPPING = 1
    STATUS_SUBMITTED = 2
    STATUS_CANCELED = 3
    STATUS_SENT = 4
    
    customer = Customer
    order_time = models.DateTimeField()
    total_price = models.IntegerField()
    status = (
        (STATUS_SHOPPING, 'در حال خرید'),
        (STATUS_SUBMITTED, 'ثبت شده'),
        (STATUS_CANCELED, 'لغو شده'),
        (STATUS_SENT, 'ارسال شده')
    )

    @staticmethod
    def initiate(customer):
        pass

    def add_product(self, product, amount):
        pass

    def remove_product(self, product, amount=None):
        pass

    def submit(self):
        pass

    def cancel(self):
        pass

    def send(self):
        pass
