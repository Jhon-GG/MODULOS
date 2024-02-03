
import json
from os import system
import module.camper as camper
from module.validate import menuNoValid

def menu():
    print(""""
       ____________________________    
      |****************************|
      |** BIENVENIDO CAMPUSLANDS **|
      |** SEGUIMIENTO ACADEMICO  **|
      |****************************|  
         
          """)
    print("Sistema de almacenamiento de datos para campus")
    print("\t1. Informacion del camper")
    print("\t2. Informacion del trainer")
    print("\t3. Registro notas camper")
    print("\t4. Modulo de reportes")
    print("\t0. Salir")
    
    bandera=True
    while (bandera):
        menu()
        opc=int(input())
        match(opc):
            case 1:
                with open("module/storage/camper.json", "r") as f:
                camper.camper = json.loads(f.read())
                f.close()
                system("cls")
                camper.menu()