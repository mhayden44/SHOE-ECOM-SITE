from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.contrib.auth.models import User
import uuid
fs = FileSystemStorage(location='/media/photos')

# Create your models here.
# Customer model that has a one-to-one relationship with User.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

# Category model so shoes can be split up and filtered depending on what type of shoe they are.
class Category(models.Model):
    SHOE_TYPES=(
        ('ATHL', 'Athletic'),
        ('DRSS','Dress'),
        ('WORK','Work'),
        ('CASL','Casual'),
    )
    type = models.CharField(max_length=4,choices=SHOE_TYPES)

    # Returns all four category types that are available
    @staticmethod
    def get_all_types():
        return Category.objects.all()

    def __str__(self):
        return self.type

# Gender model so shoes can be split up and filtered depending on what gender they are for.
class Gender(models.Model):
    GENDER_TYPES=(
        ('M','Male'),
        ('F','Female'),
    )
    gender = models.CharField(max_length=1,choices=GENDER_TYPES)
    
    # Returns both gender types that are available
    @staticmethod
    def get_all_genders():
        return Gender.objects.all()

    def __str__(self):
        return self.gender

# Shoe model which has various attributes which can be used to define each shoe. Also has two foreign keys, 
# one to Category and one to Gender so that each shoe may be filtered depending on category and gender.
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

    # Filters shoes by ID
    @staticmethod
    def get_shoes_by_id(ids):
        return Shoe.objects.filter (id__in=ids)

    # Returns all shoes
    @staticmethod
    def get_all_shoes():
        return Shoe.objects.all()

    def __str__(self):
        return self.name

# Cart model which has a foreign key corresponding to each customer as well as a universal unique identifier that uniquely identifies each cart.
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    completed = models.BooleanField(default=False)

    # Returns the total price of the shoes that are in a user's cart.
    @property
    def get_cart_total(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.get_total for item in cartitems])
        return total
    
    # Returns the total amount of shoes that are in a user's cart.
    @property
    def get_itemtotal(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.quantity for item in cartitems])
        return total

    def __str__(self):
        return str(self.id)

# CartItems model which has a foreign key corresponding to each Cart as well as each Shoe.
# Keeps track of what shoes (and the quantity of each) that are in each unique cart (each cart is unique to each customer as defined by the Cart model)
class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shoe =  models.ForeignKey(Shoe, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    # Returns the the total price of each shoe by multiplying its' price by its' quantity.
    @property
    def get_total(self):
        total = self.quantity * self.shoe.price
        if total == 0.00:
            self.delete()
        return total

    def __str__(self):
        return self.shoe.name