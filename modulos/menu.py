import os
import modulos.exit as e
import modulos.contactos as co
import modulos.coreFile as c
from tabulate import tabulate


def Principal(contactos:dict):
    global dataContacts
    dataContacts=contactos
    
    def wraper(func):
        func
        input()
        Principal(dataContacts)

    isOption=True
    while isOption:
        os.system('cls')    
        menu=[['1.Agregar'],['2.Editar'],['3.Eliminar'],['4.Buscar'],['5.Salir']]
        print(tabulate(menu, tablefmt='grid'))
        try:
            op=int(input('Selecciona una opcion --> '))
            if op==1:
                wraper(co.addContact(dataContacts))
            elif op==2:
                wraper(co.editContact(dataContacts))
            elif op==3:
                wraper(co.deleteContact(dataContacts))
            elif op==4:
                wraper(co.searchContact(dataContacts))
            elif op==5:
                isOption= e.exit()

        except ValueError:
            print('Ingrese un valor valido')
            input()
        

        

