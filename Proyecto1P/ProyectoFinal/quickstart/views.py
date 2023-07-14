from django.shortcuts import render
from rest_framework import viewsets, permissions

from empleados.models import Empleado, Departamento
from quickstart.serializers import EmpleadoSerializer, DepartamentoSerializer


# Create your views here.
class EmpleadoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Empleado.objects.all().order_by('apellido')
    serializer_class = EmpleadoSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepartamentoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]

