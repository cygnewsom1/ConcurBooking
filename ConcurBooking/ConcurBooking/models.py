from django.db import models

class UserInfo(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    user_name = models.CharField(max_length=20)

class ItemInfo(models.Model):
    item_id = models.CharField(max_length=20, primary_key=True)
    item_quantity = models.IntegerField(default=0)

class Checkout(models.Model):
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    item_id = models.ForeignKey(ItemInfo, on_delete=models.CASCADE)
    time = models.DateTimeField('Checkout time')