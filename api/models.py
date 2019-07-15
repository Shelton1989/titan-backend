from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=20)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=5)
    photo = models.ImageField(upload_to='uploads', blank=True)
    employee_number = models.CharField(max_length=10)
    date_joined = models.DateField(blank=True, null=True)

class Garage(models.Model):
    title = models.CharField(max_length=50, unique=True)
    manager_title = models.CharField(max_length=5)
    manager_name = models.CharField(max_length=50)
    email_address = models.EmailField(unique=True)
    contact_number = models.IntegerField()
    street_address = models.CharField(max_length=100)
    suburb = models.CharField(max_length=50)
    ext = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return "{}".format(self.title)

class Asset(models.Model):
    garage = models.OneToOneField(Garage, on_delete=models.CASCADE, related_name='asset', blank=True, null=True)
    asset_serial_number = models.CharField(max_length=100)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    receiver_size = models.CharField(max_length=20)
    receiver_serial_number = models.CharField(max_length=100)
    receiver_manufacturer = models.CharField(max_length=100)
    belt_size = models.CharField(max_length=20)
    belt_section = models.CharField(max_length=20)
    block_serial_number = models.CharField(max_length=50)
    block_model = models.CharField(max_length=50)
    motor_size = models.CharField(max_length=4)
    motor_amps = models.CharField(max_length=10)
    pressure_switch_details = models.CharField(max_length=150)
    water_trap = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    installation_date = models.DateField()
    last_service = models.DateField()

    def __str__(self):
        return "{}".format(self.asset_serial_number)