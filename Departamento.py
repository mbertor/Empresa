__author__ = 'Raul'

class Departamento():

    def __init__(self,nombre,id):
        self.nombre_depto=nombre
        self.id_depto=id
        self.lista=[]


    def aniadir_empleado(self,empleado):
        self.lista.append(empleado)

    def get_salario_total(self):
        num=0
        for i in self.lista:
             num += i.get_salario()
        return num

    def get_nombre_depto(self):
        return self.nombre_depto

    def salario_total_mensual(self):
        num = 0
        for i in self.lista:
            num += i.get_salario_mensual()
        return num