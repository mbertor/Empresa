__author__ = 'Raul'

class Empleado():

    def __init__(self,nombre,apellidos,dni,direccion,edad,email,salario):
            self.nom = nombre
            self.nom2 = apellidos
            self.dni = dni
            self.direc = direccion
            self.edad = edad
            self.mail = email
            self.sal = float(salario)

    def get_salario(self):
        return self.sal

    def get_dni(self):
        return self.dni

    def get_nombre_apellidos(self):
        return self.nom + ' ' + self.nom2

    def get_edad(self):
        return self.edad

    def get_email(self):
        return self.mail

    def get_direccion(self):
        return self.direc

    def get_salario_mensual(self):
        return self.get_salario()/12
