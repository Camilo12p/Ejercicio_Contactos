import os
import json

BASE='data/'
def checkFile(*params):    #checkar el archivo
    data=list(params)   
    if (os.path.isfile(BASE+data[0])):
        data[1].update(readFile(data[0],data[1]))
    else:
        createFile(data[0])

def createFile(*params):
    data=list(params)
    with open(BASE+data[0],'w') as bw:
        json.dump({'contactos':1},bw,indent=4)

def readFile(*params):
    data=list(params)
    with open(BASE+data[0],'r') as br:
        return json.load(br) 

def addData(*params):
    data=list(params)
    with open(BASE+data[0],'r+') as brw:   # Leer el archvivo
        data_file= json.load(brw)
        data_file.update(data[1])          # Añade los datos

        brw.seek(0)
        json.dump(data_file,brw,indent=4)   # lo re-escribe

def updateFile(*params):
    with open(BASE+params[0],'w') as bw:
        bw.seek(0)
        json.dump(params[1],bw,indent=4)