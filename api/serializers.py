from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ValeurAjouteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValeurAjoutee
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
   
    def to_representation(self, obj):
        rep = super().to_representation(obj)
        valeurs = ValeurAjoutee.objects.filter(hotel=obj)
        rep["valeurs"] = ValeurAjouteeSerializer(valeurs,many=True).data
        return rep

    class Meta:
        model = Hotel
        fields = '__all__'
        

class ChambreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chambre
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    class Meta:
        model = Reservation
        fields = '__all__'


    def create(self, validated_data):
        client = Client.objects.create(**validated_data.pop('client'))
        instance = Reservation.objects.create(client= client,**validated_data)
        return instance

    def to_representation(self, obj):
        rep = super().to_representation(obj)
        rep["chambre"] = ChambreSerializer(obj.chambre).data
        return rep

    
class TokenPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(TokenPairSerializer, self).validate(attrs)
        data['id'] = self.user.id
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name

        return data
