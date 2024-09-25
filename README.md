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
