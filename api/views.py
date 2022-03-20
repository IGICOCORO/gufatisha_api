from typing import List

from rest_framework import viewsets
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *
from .models import *

class TokenPairView(TokenObtainPairView):
	serializer_class = TokenPairSerializer

class ClientViewset(viewsets.ModelViewSet):
	serializer_class = ClientSerializer
	queryset = Client.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [AllowAny]

class HotelViewset(viewsets.ModelViewSet):
	serializer_class = HotelSerializer
	queryset = Hotel.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [AllowAny]

class ValeurAjouteeViewset(viewsets.ModelViewSet):
	serializer_class = ValeurAjouteeSerializer
	queryset = ValeurAjoutee.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [AllowAny]

class ChambreViewset(viewsets.ModelViewSet):
	serializer_class = ChambreSerializer
	queryset = Chambre.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [AllowAny]
	filter_backends = [DjangoFilterBackend]
	ordering_fields = 'hotel__id'
	search_fields = ['hotel__nom','hotel__id']
	filterset_fields = {
		'hotel__id':['exact'],
	}

class ReservationViewset(viewsets.ModelViewSet):
	serializer_class = ReservationSerializer
	queryset = Reservation.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [AllowAny]
	filter_backends = [DjangoFilterBackend]
	ordering_fields = 'client__phone'
	search_fields = ['id','client__nom','client__phone']
	filterset_fields = {
		'client__phone':['exact'],
	}
