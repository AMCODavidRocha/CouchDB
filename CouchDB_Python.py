import couchdb
couch = couchdb.Server('http://admin:root8992@127.0.0.1:5984/')

db = 'personas'
if db in couch:
    db = couch[db]
    print(f"Accediendo a la base de datos '{db}'")
else:
    print(f"La base de datos '{db}' no existe.")

# Listar los documentos en la base de datos
#for doc_id in db:
#    doc = db[doc_id]  # Obtener el documento por su ID
#    print(f"DOC ID: {doc_id} ≤≤≤≤≤≤≤≤")
#    for key, value in doc.items():
#        print(f"Campo: {key}, Valor: {value}")




query = {
    "selector": {
        "apellido": "Rocha"
    },
    "fields": ["nombre","apellido"],
    "limit": 100,
    "skip": 0
}

# Ejecutar la consulta
r = db.find(query)
print(r)
# Mostrar los documentos que coinciden
for doc in r:
    print(f"Doc: {doc}")


"""""
doc = {
  "_id": "fromPython",
  "nombre": "Monty",
  "apellido": "Python",
  "edad": 50,
  "direccion": {
    "calle": "Calle python",
    "ciudad": "New Python",
    "estado": "Python States",
    "cp": "12345"
  },
  "fecha": "1974-01-01"
}
"""
#doc_id, doc_rev = db.save(doc)
#print(f"Document created with ID: {doc_id} and revision: {doc_rev}")

#doc = db['fromPython']
#print(doc)
#doc['age'] = 31  # Update the age
#db.save(doc)  # Save the updated document
#print(f"Document with ID {doc_id} updated.")