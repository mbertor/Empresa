from unittest import TestCase
from Departamento import *
from Empleado import *
from mockito import *

__author__ = 'Raul'


class TestDepartamento(TestCase):



    def test_get_salario_total(self):

        empleado1=mock(Empleado)
        when(empleado1).get_salario().thenReturn(1000)

        empleado2=mock(Empleado)
        when(empleado2).get_salario().thenReturn(2000)

        empleado3=mock(Empleado)
        when(empleado3).get_salario().thenReturn(1000)

        departamento = Departamento('Calidad',1)
        departamento.aniadir_empleado(empleado1)
        departamento.aniadir_empleado(empleado2)
        departamento.aniadir_empleado(empleado3)
        self.assertEqual(departamento.get_salario_total(),400)


