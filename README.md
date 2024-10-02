# CouchDB

###### The goal of this issue is to explore CouchDB, focusing on its installation, using the Futon interface, performing Mango queries, temporal view requests. These tasks will be performed using both curl and the Python SDK. Additionally, the final task will involve creating a Python class to connect to CouchDB and handle operations programmatically.

**Tasks:**

***Section 1:***
* Install CouchDB and Load Database from Dump
Research how to install CouchDB locally on your system (Windows, macOS, or Linux).
* Install CouchDB using the official instructions: CouchDB Installation.
* **Task:**
    * Install CouchDB on your local machine.                       
        ![pic](src/img/1-1.png)
    * Verify the installation by accessing the Futon interface,
    usually available at <http://127.0.0.1:5984/_utils/>
        ![pic](src/img/1-2.png)

| **TASK**    | :white_check_mark: |
| :---        |               ---: |
---
***1.1 Load a Database from a Dump File***
* Research how to load a CouchDB database from a dump file.

* **Task:**

    * Download a sample CouchDB database dump. (dump will be provided at DAN-1573)
        ![pic](src/img/1-1-1.png)
        
        ![pic](src/img/1-1-2.png)

    * Load the dump into CouchDB :warning:
        * We had some problems with the export, the json file must have the key "docs" so that CouchDB can generate a document with each json inside "docs". 
        * Also make sure that the versions of the CouchDB documents where they are exported do not come.
        * If CouchDB indicates that the file is not in UTF-8 format, the solution would be to open it in any Windows text editor (VSC, Sublime, etc.) and add it.
            >   `~curl -X POST http://"USER":"PASSWORD"@localhost:5984/sakila/_bulk_docs -H "Content-Type: application/json" -d @sakila_dump_formated.json`

        ![pic](src/img/1-1-3.png)

    * Verify the loaded database by running simple queries or viewing documents in Futon.
        > Equivalent to
        > `~SELECT * FROM actor;`

        ![pic](src/img/1-1-4.png)
        > Equivalent to
        > `~SELECT * FROM actor WHERE first_name = 'SISSY';`

        ![pic](src/img/1-1-5.png)

| **TASK**    | :white_check_mark: |
| :---        |               ---: |
---
***Section 2: CouchDB Operations Using Futon Interface***
* Research and explore the Futon web interface provided by CouchDB.
* Learn how to:
    * Create and manage databases using Futon.
    ![pic](src/img/2-1.png)
    ![pic](src/img/2-2.png)
    * Insert, update, and delete documents through the graphical interface:
        - Insert
    ![pic](src/img/2-3.png)
    ![pic](src/img/2-4.png)
        - Update and Delete
    ![pic](src/img/2-5.png)
    * View logs, CouchDB system information, and design documents.
        - Logs names at the left menu and the design of documents are like an add a register on a table.
    ![pic](src/img/2-6.png)


**Task:**
* Write a brief summary of how to navigate Futon and perform basic operations such as creating databases, adding documents, and updating them

        
    >- CouchDB Fauxton view are very simple and let us create, update or delete DB and Documents, in the log of databases are all the tools we gonna need, like a 
    >- Create DB:
    >   - `Databases-->CreateDatabase`
    >- Create Document:
    >   - `Databases-->"Database"-->CreateDocument`
    >- Delete one or the other
    >   - `Databases-->DeleteDatabase`
    >   - `Databases-->"Document"-->DeleteDoc`
    >- Update a Documents we just need select it and modify directly at the json format.
    >   - `Databases-->"Document"-->SaveChanges` 
    >- Contorl verions are in the BD and Changes menu.
    >   - `Databases-->"Database"-->Changes`

| **TASK**    | :white_check_mark: |
| :---        |               ---: |
---

***Section 3: CouchDB Operations Using curl***
* Research how to interact with CouchDB using the curl command-line tool.

* Learn how to:

    * Send HTTP requests to CouchDB using curl.  
        * Request all db in CouchDB:
        `~curl -X GET user:password@localhost:5984/_all_dbs` 
    * Perform database operations like creating, reading, and updating documents. 
        * Create a DB in CouchDB named personas:
        `curl -X PUT user:password@localhost:5984/personas`
        * Delete a DB in CouchDB named personas:
        `curl -X DELETE user:password@localhost:5984/personas`

        * Create a Document in the DB con un _id creado por nosotros (8992):
        `curl -X PUT user:password@127.0.0.1:5984/personas/8992 -H "Content-Type: application/json" -d '{"nombre":"David","edad":35}'`
        * Create a document with a default CouchDB assignment (without 8992):
        `curl -X POST user:password@127.0.0.1:5984/personas -H "Content-Type: application/json" -d '{"nombre":"Dahra", "apellido": "Rocha", "edad":7, "color":"Rosa}'`
        * Modified a document, for this we need to know the actually _rev and pass the complete params of the document, those gonna be updated and the rest of datas:
        `curl -X PUT user:password@127.0.0.1:5984/personas/"a5a7ea3029f5eee145378f63bd7d758d" -H "Content-Type: application/json" -d '{"_rev":"2-87c6a8f9a1a3f3b4c1bf85e57d296ee8", "nombre":"Makis Makikis", "apellido": "Rocha", "edad": 2, "color":"Gris"}'`
        * To delete a document also we need to know the actually _rev and send in the url:
        `curl -X DELETE user:password@127.0.0.1:5984/personas/"a5a7ea3029f5eee145378f63bd7e5a41?rev=1-0c1f84d414a19290490f75dc5bd2b53b"`
        **Extras:**
        * If we know the id of the document we can request the info of the documento to obtain de _rev:
        `curl -X GET user:password@127.0.0.1:5984/personas/a5a7ea3029f5eee145378f63bd7d51e9`
        * Also if we dont know both _id and _rev we can request a list of all documents:
        `curl -X GET user:password@127.0.0.1:5984/personas/"_all_docs?include_docs=true"`

***3.1. Mango Queries via curl***
* Mango queries provide a declarative way to query CouchDB using JSON syntax.
* Perform the following operations using curl: 
    * Filter documents based on specific fields. 
    `curl -H 'Content-Type: application/json' -X POST admin:root8992@127.0.0.1:5984/personas/_find -d '{"selector":{"nombre":"Dahra"}}'`
    * Perform pagination using limit and skip. (limit are a maxim numbers of documents, skip will remove a number of the total of documents): 
    `curl -H 'Content-Type: application/json' -X POST admin:root8992@127.0.0.1:5984/personas/_find -d '{"selector": {"apellido": "Rocha"},"fields": ["nombre","apellido"],"limit": 100,"skip": 0}'`

**Task:** 
* Execute at least 3 different Mango queries using curl and document the process.

    * the fields where selector is the condition and fields are the results:    

    `curl -H 'Content-Type: application/json' -X POST user:password@127.0.0.1:5984/personas/_find -d '{"selector": {"apellido": "Rocha"},"fields": ["nombre","edad"]}'`

    * Select the nombre field when the condition edad was 35 or 2:
    `curl -H 'Content-Type: application/json' -X POST user:password@127.0.0.1:5984/personas/_find -d '{"selector": {"edad": {"$or": [35,2]}},"fields": ["nombre"]}'`

    * Now, we select the documents where edad are higher than 5 and apellido are equals to Rocha
    `curl -H 'Content-Type: application/json' -X POST user:password@127.0.0.1:5984/personas/_find -d '{"selector": {"edad": {"$gt": 5},"apellido": "Rocha"}}'`

| **TASK**    | :white_check_mark: |
| :---        |               ---: |
---

***3.2. Temporal View Request via curl***
:warning::warning::warning::warning::warning::warning::warning::warning::warning::warning::warning::warning::warning::warning::warning::warning::warning:
>**Temporal Views are not suported:** 
>{"error":"gone","reason":"Temporary views are not supported in CouchDB"}

* Temporal view requests allow you to retrieve documents ordered by a timestamp or other temporal field.
* Perform the following using curl:
    * Create and define a temporal view.
    * Retrieve documents sorted by a specific time-based field.

**Task:**
* Set up and query a temporal view using curl and document the steps and results.

* :warning: Due to this incompatibility, we create and manage views with de CouchDB Fauxton interface, and call it via CURL

    - To create a new view we fallow the next steps:
        - In the design new document, we click en the plus button and choose new view.
        - In the new view page, in the _design input we put the name of the group for the views.
        - in the index name, we put the name of the view. (one design can contain multiple views)
        - In map function we put the code, example:
        `function (doc) {`
        `  emit(doc._id, [doc.nombre, doc.apellido]);`
        `}`
        Where emit() will response with all the docs id and a list of two values.
         ![pic](src/img/3-2-1.png)
        - Finally with CURL we make de call by this form:
        `curl user:password@127.0.0.1:5984/personas/_design/datosPersona/_view/nombre-completo`
        ![pic](src/img/3-2-2.png)

    - To get a list of documents sorted by any value, first we need to create a index of that values, this action we will create in the Fauxton view, just by clicling
        ![pic](src/img/3-2-3.png)
    Then, just need to modify the value that we want in the index, in this example we put "edad" and "edad-index" to the name of the index:
        ![pic](src/img/3-2-4.png)
    Finally, we can use a mango query to select the condition and values that we want, and adding the sort parameter indicate that with that vale we want the sort, asc by defautl or desc.
    `curl -H 'Content-Type: application/json' -X POST user:password@127.0.0.1:5984/personas/_find -d '{"selector":{"direccion.ciudad": "Zapopan"},"fields":["nombre","apellido","edad"],"sort":[{"edad":"desc"}]}'`

| **TASK**    | :white_check_mark: |
| :---        |               ---: |
---

***3.3. Update Documents via curl***

* Perform the following tasks using curl:

    * Update existing documents in CouchDB.  
        >This point was solved in the section 3.
    * Handle document revisions and update conflicts.
        >This point will be pending.

**Task:**
* Execute document updates using curl, including handling conflicts. Document the process and examples.

| **TASK**    |       |
| :---        |  ---: |
---

***Section 4: CouchDB Operations Using Python SDK***
* Research how to interact with CouchDB using the Python SDK (e.g., couchdb library or another suitable SDK).
* Learn how to:
    * Install and set up the CouchDB Python SDK.
    ![pic](src/img/4-1.png)
    * Perform database operations such as creating, reading, and updating documents.
        - Create document:
        
        ![pic](src/img/4-3.png)

        - Reading document:

        ![pic](src/img/4-4.png)

         - Update document:

        ![pic](src/img/4-5.png)

***4.1. Mango Queries via Python SDK***

* Use the Python SDK to perform Mango queries in CouchDB. 
    * We select all the documents where apellido is equal to "Rocha" 
    ![pic](src/img/4-1-1.png)
* Perform the following operations using Python SDK*:

    * Filter documents based on specific fields.
        * We select all documents ordered by "edad" asc:

        ![pic](src/img/4-1-2.png)
    * Perform pagination using limit and skip.
        * We select all the documents with a limit of documents received and exclude 1 of the documents received

        ![pic](src/img/4-1-3.png)

**Task:** 
* Execute at least 3 different Mango queries using Python SDK and document the process.
    - In this consult we make 4 tipes or conditions: **Selector** with a **regex** that de city contains "pan", **fields:** that we want to see, **sort:** by "edad" previously created an index with this field and **limit:** just showing a number of documents.
    ![pic](src/img/4-1-4.png)

***4.2. Temporal View Request via Python SDK***

* Use the Python SDK to perform temporal view requests in CouchDB.

* Perform the following using Python SDK:

    * Create and define a temporal view.
        - For this point we create the view as the task section on point 3.2

    * Retrieve documents sorted by a time-based field.
    ![pic](src/img/4-2-1.png)

**Task:** 
* Set up and query a temporal view using Python SDK and document the results.
    - _disign: the name of the group of views
    - _view: the name of the view
    - map function:add the code that you need
    ![pic](src/img/4-2-2.png)

***4.3. Update Documents via Python SDK***

* Use the Python SDK to update existing documents in CouchDB.
    - We need to know the id from de the document that we need uptdate
![pic](src/img/4-3-1.png)

* Handle document revisions and resolve update conflicts.
    * This point will be pending...

**Task:**
* Execute document updates using Python SDK, including handling conflicts, and document the process.

| **TASK**    | :white_check_mark: |
| :---        |               ---: |
---