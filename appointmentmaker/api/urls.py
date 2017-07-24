from django.conf.urls import url, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet, base_name='companies')
router.register(r'appointments', views.AppointmentViewSet, base_name='appointments')

urlpatterns = [
    url(r'', include(router.urls)),
]