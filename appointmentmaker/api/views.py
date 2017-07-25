from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response

from api import serializers


class SetApproved(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.company.owner:
            return True

        approved = request.data.get('approved', None)
        return approved is None


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CompanySerializer

    def get_queryset(self):
        return self.request.user.companies.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @detail_route(permission_classes=[IsAuthenticated], methods=['get'], url_path='appointments')
    def appointments(self, request, pk=None):
        appointments = self.get_object().appointments.all()
        serializer = serializers.AppointmentSerializer(appointments, many=True)

        return Response(serializer.data)


class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AppointmentSerializer
    permission_classes = (IsAuthenticated, SetApproved)

    def get_queryset(self):
        approved = self.request.query_params.get('approved')
        company = self.request.query_params.get('company')
        appointments_qs = self.request.user.appointments.all()

        if approved == 'false':
            return appointments_qs.filter(approved=False)
        if approved == 'true':
            return appointments_qs.filter(approved=True)

        if company:
            return appointments_qs.filter(company__pk=company)

        return appointments_qs

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
