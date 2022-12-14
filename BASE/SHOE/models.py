from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.contrib.auth.models import User
import uuid
fs = FileSystemStorage(location='/media/photos')

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Category(models.Model):
    SHOE_TYPES=(
        ('ATHL', 'Athletic'),
        ('DRSS','Dress'),
        ('WORK','Work'),
        ('CASL','Casual'),
    )
    type = models.CharField(max_length=4,choices=SHOE_TYPES)

    @staticmethod
    def get_all_types():
        return Category.objects.all()

    def __str__(self):
        return self.type


class Gender(models.Model):
    GENDER_TYPES=(
        ('M','Male'),
        ('F','Female'),
    )
    gender = models.CharField(max_length=1,choices=GENDER_TYPES)
    
    @staticmethod
    def get_all_genders():
        return Gender.objects.all()

    def __str__(self):
        return self.gender

class Shoe(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=100,null=True)
    description = models.TextField()
    price = models.FloatField(default=39.99)
    size = models.CharField(max_length=200)
    type = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE,default=1)
    image = models.ImageField(upload_to='pictures/')

    @staticmethod
    def get_shoes_by_id(ids):
        return Shoe.objects.filter (id__in=ids)

    @staticmethod
    def get_all_shoes():
        return Shoe.objects.all()

    def __str__(self):
        return self.name

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    completed = models.BooleanField(default=False)

    @property
    def get_cart_total(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.get_total for item in cartitems])
        return total
    
    @property
    def get_itemtotal(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.quantity for item in cartitems])
        return total

    def __str__(self):
        return str(self.id)

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shoe =  models.ForeignKey(Shoe, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    @property
    def get_total(self):
        total = self.quantity * self.shoe.price
        if total == 0.00:
            self.delete()
        return total

    def __str__(self):
        return self.shoe.name