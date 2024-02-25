

def validateEmail()->str:
    email=str(input('Ingrese el email del contacto --> '))
    if email.isalnum():
        return validateEmail()
    else: 
        return email

def validateInt(nameVar:str,action:str='')->int:
    try:
        var=int(input(f'Ingrese el {nameVar} del contacto {action} --> '))
    except ValueError:
        return validateInt(nameVar)

    return var

def validateStr(nameVar:str)->str:
    var=str(input(f'Ingrese el {nameVar} del contacto --> '))
    if var.isalpha():
        return var
    else: 
        return validateStr(nameVar)

def validateId(id:int,srcdata:dict)->int:
    if str(id) in srcdata:
        print('El id ya se encuentra registrado')
        return True
    else:
        return False