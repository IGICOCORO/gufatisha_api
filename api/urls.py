from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

router = routers.DefaultRouter()

router.register("client", ClientViewset)
router.register("hotel", HotelViewset)
router.register("valeur_ajoutée", ValeurAjouteeViewset)
router.register("chambre", ChambreViewset)
router.register("Reservation", ReservationViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
