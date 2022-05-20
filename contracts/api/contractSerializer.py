from rest_framework import serializers
from ..models import Contract


class ContractSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contract
		fields = ('user', 'name', 'email', 'status', 'createdTime')
