# IMPORTACION DE LIBRERIAS Y OTRAS FUNCIONALIDADES DE PYTHON #
import json
from os import system

# IMPORTACION DE LOS MODULOS PARA PODER INGRESAR #
from Modulos.Validaciones.Validaciones import menuNoValid
from Storage.Datos.datos import camper
from Storage.Datos.datos import Estados
from Storage.Datos.datos import En_riesgo
from Storage.Datos.datos import Inscrito
from Storage.Datos.datos import Aprobado
from Storage.Datos.datos import Filtrado




def search():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ***************************
        *  Evaluacion del Camper  *
        ***************************
        """)
        for i,val in enumerate(camper):
            print(f"""
________________________
Codigo: {i}
Nombre: {val.get('Nombre')}
Apellido: {val.get('Apellido')}
Identificacion: {val.get('Identificacion')}
Direccion: {val.get('Direccion')}
Edad: {val.get('Edad')}
NombreAcudiente: {val.get('NombreAcudiente')}
NumeroAcudiente: {val.get('NumeroAcudiente')}
idAcudiente: {val.get('idAcudiente')}
TelefonoCamper: {val.get('TelefonoCamper')}
Estado: {val.get('Estado')}
________________________
""")
        Codigo = int(input("Ingrese el numero del camper al que desea asignar notas \n"))
        print(f"""
________________________
Codigo: {Codigo}
Nombre: {camper[Codigo].get('Nombre')}
Apellido: {camper[Codigo].get('Apellido')}
Identificacion: {camper[Codigo].get('Identificacion')}
Direccion: {camper[Codigo].get('Direccion')}
Edad: {camper[Codigo].get('Edad')}
NombreAcudiente: {camper[Codigo].get('NombreAcudiente')}
NumeroAcudiente: {camper[Codigo].get('NumeroAcudiente')}
idAcudiente: {camper[Codigo].get('idAcudiente')}
TelefonoCamper: {camper[Codigo].get('TelefonoCamper')}
Estado: {camper[Codigo].get('Estado')}
________________________
        """)
        print("¿Este es el camper al que desea asignar nota? \n")
        print("1. Si")
        print("2. No")
        print("3. Salir\n")
        opc = int(input("Seleccione su opcion \n"))
        if (opc == 1):
            Nota_teorica = int(input("ingrese el valor de la nota teorica \n"))
            Nota_Practica = int(input("ingrese el valor de la nota practica \n"))
            Promedio = (Nota_teorica + Nota_Practica) / 2
            if Promedio <= 59:
                print("! LO SENTIMOS EL CAMPER NO HA SUPERADO LA PRUEBA ! \n")
                info2 = {
                    "Nombre": camper[Codigo].get('Nombre'),
                    "Apellido": camper[Codigo].get('Apellido'),
                    "Identificacion": camper[Codigo].get('Identificacion'),
                    "Direccion": camper[Codigo].get('Direccion'),
                    "Edad": camper[Codigo].get('Edad'),
                    "NombreAcudiente": camper[Codigo].get('NombreAcudiente'),
                    "NumeroAcudiente": camper[Codigo].get('NumeroAcudiente'),
                    "idAcudiente": camper[Codigo].get('idAcudiente'),
                    "TelefonoCamper": camper[Codigo].get('TelefonoCamper'),
                    "Estado": int(input("Asigne el nuevo estado del camper:\n\t"+"\t".join([f"{Estados.index(i)+1}. {i}\n" for i in (Estados)])))
                }
                if info2["Estado"] == 4:
                    En_riesgo.append(info2)
                    with open("Storage/Campers/En_riesgo.json", "w") as f:
                        datos = json.dumps(En_riesgo, indent=4)
                        f.write(datos)
                        f.close()
                else:
                    if info2["Estado"] == 3:
                        Aprobado.append(info2)
                        with open("Storage/Campers/Aprobados.json", "w") as f:
                            datos = json.dumps(Aprobado, indent=4)
                            f.write(datos)
                            f.close()
                    else:
                        if info2["Estado"] == 2:
                            Inscrito.append(info2)
                            with open("Storage/Campers/Inscritos.json", "w") as f:
                                datos = json.dumps(Inscrito, indent=4)
                                f.write(datos)
                                f.close()
                        else:
                            if info2["Estado"] == 1:
                                print("EL CAMPER NO SUPERO LA PRUEBA Y SE QUEDA COMO PREINSCRITO PARA NUEVAS PRUEBAS")
                            else:
                                if info2["Estado"] == 5:
                                    Filtrado.append(info2)
                                    with open("Storage/Campers/Filtrados.json", "w") as f:
                                        datos = json.dumps(Filtrado, indent=4)
                                        f.write(datos)
                                        f.close()
                return "Sucessfully Camper"
            else:
                print("! EL CAMPER HA SUPERADO LA PRUEBA !")
                info = {
                    "Nombre": camper[Codigo].get('Nombre'),
                    "Apellido": camper[Codigo].get('Apellido'),
                    "Identificacion": camper[Codigo].get('Identificacion'),
                    "Direccion": camper[Codigo].get('Direccion'),
                    "Edad": camper[Codigo].get('Edad'),
                    "NombreAcudiente": camper[Codigo].get('NombreAcudiente'),
                    "NumeroAcudiente": camper[Codigo].get('NumeroAcudiente'),
                    "idAcudiente": camper[Codigo].get('idAcudiente'),
                    "TelefonoCamper": camper[Codigo].get('TelefonoCamper'),
                    "Estado": int(input("Asigne el nuevo estado del camper:\n\t"+"\t".join([f"{Estados.index(i)+1}. {i}\n" for i in (Estados)])))            
                }
                if info["Estado"] == 4:
                    En_riesgo.append(info)
                    with open("Storage/Campers/En_riesgo.json", "w") as f:
                        datos = json.dumps(En_riesgo, indent=4)
                        f.write(datos)
                        f.close()
                else:
                    if info["Estado"] == 3:
                        Aprobado.append(info)
                        with open("Storage/Campers/Aprobados.json", "w") as f:
                            datos = json.dumps(Aprobado, indent=4)
                            f.write(datos)
                            f.close()
                    else:
                        if info["Estado"] == 2:
                            Inscrito.append(info)
                            with open("Storage/Campers/Inscritos.json", "w") as f:
                                datos = json.dumps(Inscrito, indent=4)
                                f.write(datos)
                                f.close()
                        else:
                            if info["Estado"] == 1:
                                print("EL CAMPER NO SUPERO LA PRUEBA Y SE QUEDA COMO PREINSCRITO PARA NUEVAS PRUEBAS")
                            else:
                                if info["Estado"] == 5:
                                    Filtrado.append(info)
                                    with open("Storage/Campers/Filtrados.json", "w") as f:
                                        datos = json.dumps(Filtrado, indent=4)
                                        f.write(datos)
                                        f.close()
                return print(f"Camper successfully ")            
        elif (opc == 2):
            bandera = False
        elif (opc == 3):
            system("clear")
            bandera = False

            
def menu():
    bandera = True
    while (bandera):
        print("""*******************************
MODULO DE EVALUACION DEL CAMPER
*******************************
CRUD del modulo de Evaluacion del camper
""")
        print("\t1. Prueba Teorica y Practica del camper (Registro de Prueba)")
        print("\t0. Salir \n")
        opc = int(input("seleccione su opcion \n"))
        match(opc):
            case 1: search()
            case 0: bandera = False, system("clear")
            case _: print(menuNoValid(opc))