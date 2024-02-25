import os

def exit()->bool:
    
    n=input('Desea Salir?\nN.Para no salir\nEnter.Para salir\n--> ').upper()
    if n=='N' or n=='NO':
        return True
    elif n=='':
        print('Bye Bye :)')
        return False
    else:
        os.system('cls')
        return exit()

