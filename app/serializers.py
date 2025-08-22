from rest_framework import serializers

from account.models import CustomUser


class UserSerailzers(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields = ['id','username', 'role']
