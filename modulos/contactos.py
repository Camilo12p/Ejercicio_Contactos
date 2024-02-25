import modulos.coreFile as c
import modulos.validation as v
def addContact(dataContacts:dict):

    id=v.validateInt('id')
    if v.validateId(id,dataContacts):
        return
    name=v.validateStr('nombre')
    email=v.validateEmail()
    celular=v.validateInt('celular')
    tel=v.validateInt('telefono')
    
    if tel=='':
        tel = 'no tiene'

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
        id=str(v.validateInt('id','a editar'))
        menu=[]
        print('Que desea editar')
        try:
            for key in srcdata[id]:
                menu.append(key)
        except KeyError:
            print('El id no se encuentra')
            return
        for i in range(len(menu)):
            if menu[i]!='id':
                print(f'{i}.{menu[i]}')
        op=int(input('Ingrese un valor --> '))
        for i in range(len(menu)):
            if op==i:
                if menu[op]=='email':
                    val=v.validateEmail()
                    srcdata[id][menu[op]]=val
                elif menu[op]=='name':
                    val=v.validateStr('nombre')
                    srcdata[id][menu[op]]=val
                else:
                    val=v.validateInt(menu[op])
                    srcdata[id][menu[op]]=val

        c.updateFile('agenda.json',srcdata)


def deleteContact(srcdata:dict):
    id=str(v.validateInt('id','a borrar'))
    try:
        srcdata.pop(id)
        c.updateFile('agenda.json',srcdata)
    except KeyError:
        print('El id no se encuentra')

def searchContact(srcdata:dict):
    id=str(v.validateInt('id','a buscar'))
    try:
        for key ,value in srcdata.get(id).items():
            print(f'{key} : {value}')
    except AttributeError:
        print('El id no se encuentra en el sistema')

