from typing import List

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import *
from .models import *

class TokenPairView(TokenObtainPairView):
	serializer_class = TokenPairSerializer

class ClientViewset(viewsets.ModelViewSet):
	serializer_class = ClientSerializer
	queryset = Client.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]

class HotelViewset(viewsets.ModelViewSet):
	serializer_class = HotelSerializer
	queryset = Hotel.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]

class ValeurAjouteeViewset(viewsets.ModelViewSet):
	serializer_class = ValeurAjouteeSerializer
	queryset = ValeurAjoutee.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]

class ChambreViewset(viewsets.ModelViewSet):
	serializer_class = ChambreSerializer
	queryset = Chambre.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]


class ReservationViewset(viewsets.ModelViewSet):
	serializer_class = ReservationSerializer
	queryset = Reservation.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]
