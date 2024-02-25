import modulos.menu as m

if (__name__ =='__main__'):
    contactos={}
    m.c.checkFile('agenda.json',contactos)
    m.Principal(contactos)
    
    
    pass