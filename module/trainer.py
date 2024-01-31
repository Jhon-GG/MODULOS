
from os import system
from module.validate import menuNoValid
from .data import *
def save(name):
    trainer.append(name)
    return "Succesfully Trainer", name
def edit():
    return "Edit to trainer"
def search():
    return "The Trainer is available"
def delete():
    return "Trainer Delete"
def menu():
    bandera = True
    while (bandera):
        print("\t----CRUD del Trainer----")
        print("\t 1. Guardar Trainer")
        print("\t 2. Buscar Trainer")
        print("\t 3. Actualizar Trainer")
        print("\t 4. Eliminar Trainer")
        print("\t 0. Atrás")
        opc = int(input())
        match(opc):
            case 1:
                save(input("Ingrese el nombre del Trainer: "))
                print(trainer[0])
            case 0:
                system("cls")
                bandera = False
            case _:
                system("cls")
                menuNoValid(opc)