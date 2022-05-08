from django.db.models import fields
from rest_framework import serializers
from .models import Guest

class GuestSerializer(serializers.ModelSerializer):
	class Meta:
		model = Guest
		fields = ('name', 'email', 'relation')
