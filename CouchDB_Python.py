import couchdb
import os
import pandas as pd
#Este if es para ferificar en que computadora estamos trabajando, WIN o MAC
system = os.name
if system == "nt":
    couch = couchdb.Server('http://root:root8992@127.0.0.1:5984/')
else:
    couch = couchdb.Server('http://admin:root8992@127.0.0.1:5984/')


#Se intenta acceder a la BD, si no existe se crea
db = 'personas'
if db in couch:
    db = couch[db]
    #print(f"Accediendo a la base de datos '{db}'")
else:
    db = couch.create('personas')
    #print(f'Base creada: {db}')


#Se crea un documento
query = {
  "_id": "fromPython1",
  "nombre": "David",
  "apellido": "Rocha",
  "edad": 35,
  "direccion": {
    "calle": "Calle David",
    "ciudad": "Zapopan",
    "estado": "Jalisco",
    "cp": "89922426"
  },
  "fecha": "1989-01-10"
}
#db.save(query)

#Para leer documentos los cuales sabemos el ID
documento = db["fromPython1"]
#print("Documento leído:", documento)
#para leer todos los documentos de la BD
for id in db:
    documento = db[id]
    #print(documento)

#Para modificar un documento
documento = db['fromPython5']
documento['edad'] = 25
#db.save(documento)



#MANGO querys
#Seleccion simple de documentos mediante una condicion:
mango_query = {
   "selector": {"apellido":"Rocha"}
}
#Seleccion simple de documentos mediante una condicion y acomodado por orden
#mediante un valor previamente indexado desde Fauxton
mango_query1 = {
   "selector": {},
    "sort": [{"edad": "asc"}]
}
#Seleccion de todos los documentos pero limitando las cantidad de muestras
#Limit nos topa la busqueda a dicho limite, skip quita esa cantidad
#del total de documentos recibidos
mango_query2 = {
   "selector": {},
    "skip": 1,
    "limit":3
}

mango_query3 = {
   "selector": {
      "direccion.ciudad": {
         "$regex": "(?i)pan"
      }
   },
   "fields": [
      "nombre",
      "apellido",
      "edad"
   ],
   "sort": [
      {
         "edad": "asc"
      }
   ],
   "limit":3
}

print("===RESULTADO DEL MANGO QUERY===")
# Ejecutar la consulta
r = db.find(mango_query3)
# Mostrar los documentos que coinciden
for doc in r:
    print(f"Doc: {doc}")

"""
#Mostrar una vista
vista = db.view('datosPersonas/nombre-completo')
for fila in vista:
    print(fila.key, fila.value)
"""
#doc_id, doc_rev = db.save(doc)
#print(f"Document created with ID: {doc_id} and revision: {doc_rev}")

#doc = db['fromPython']
#print(doc)
#doc['age'] = 31  # Update the age
#db.save(doc)  # Save the updated document
#print(f"Document with ID {doc_id} updated.")