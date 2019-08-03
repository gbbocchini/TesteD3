from rest_auth.models import TokenModel
from rest_framework.serializers import ModelSerializer
from accounts.models import Usuario


class UserSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'password']



class TokenSerializer(ModelSerializer):
    """
    Serializer for Token model.
    """

    class Meta:
        model = TokenModel
        fields = ('key',)
