from rest_framework import serializers
from .models import Charity,Donor,Donations,CustomUser

# GET METHOD
class CharitySerializer(serializers.ModelSerializer):
  class Meta:
    model = Charity
    fields = ('id','charity')

class DonorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Donor
    fields = ('id','donor')

class DonationsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Donations
    fields = ('id','donor','charity')

class UsersSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ('id','user_name','email','last_name','first_name','is_staff','is_admin','is_active','is_superuser','date_joined')


