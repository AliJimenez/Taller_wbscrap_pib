from rest_framework import serializers

from empleados.models import Empleado, Departamento


class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empleado
        fields = ['url', 'nombre', 'apellido', 'email', 'departamento']


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = ['url', 'nombre']