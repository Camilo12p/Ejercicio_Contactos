import modulos.coreFile as c

def addContact(dataContacts:dict):

    id=int(input('Ingrese el valor del id --> '))
    name=str(input('Ingrese el Nombre del contacto --> '))
    email=str(input('Ingrese el email del contacto --> '))
    celular=int(input('Ingrese el celular del contacto --> '))
    tel=int(input('Ingrese el telefono del contacto --> '))

    contacto={
        'id':id,
        'name':name,
        'email':email,
        'celular':celular,
        'telefono':tel
    }

    dataContacts.update({id:contacto})
    c.addData('agenda.json',{id:contacto})

def editContact(srcdata:dict):
    if len(srcdata)<=0:
        print('No tiene datos que editar')
    else:
        id=str(input('Ingrese el id del contacto a editar --> '))
        menu=[]
        print('Que desea editar')
        
        for key in srcdata[id]:
            menu.append(key)
        for i in range(len(menu)):
            if menu[i]!='id':
                print(f'{i}.{menu[i]}')
        op=int(input('Ingrese un valor --> '))
        for i in range(len(menu)):
            if op==i:
                val=input('Ingrese el valor de ' + menu[op]+ ' --> ')
                srcdata[id][menu[op]]=val

        c.updateFile('agenda.json',srcdata)


def deleteContact(srcdata:dict):
    id=str(input('Ingrese el id a buscar --> '))
    srcdata.pop(id)
    c.updateFile('agenda.json',srcdata)

def searchContact(srcdata:dict):
    id=str(input('Ingrese el id a buscar --> '))
    for key ,value in srcdata.get(id).items():
        print(f'{key} : {value}')


