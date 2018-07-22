# track-it-backend
This application holds the **RESTFUL API** and **logic** for the `Track-It` application.
https://unilever-track-it.herokuapp.com

## Geting Started
These instructions will get the project up and running on your local machine for development and testing purposes.

#### System Dependencies
- [`Python`](https://www.python.org/)
- [`virtualenv`](https://virtualenv.pypa.io/en/stable/)
- [`Flask`](http://flask.pocoo.org/)
- [`Flask-sqlalchemy`](http://flask-sqlalchemy.pocoo.org/2.3/)
- [`Postgres`](https://www.postgresql.org/)

#### Installation
- Create a virtual environment for the project `mkvirtualenv --python=python3 env`
- Run `pip3 install requirements.txt`
- Start the application `python manage.py runserver`

## Authors
See the list of the [contributors](https://github.com/fob413/track-it-backend/graphs/contributors) who participated in this project.

## Api Documentation

#### User
- `/api/v1/login` **POST**
  - Logs in a user unto the platform so he's authenticated to access other api's
  - Required paramaters
    - `email`: users email
    - `password`: users password

#### Shipment
- `/api/v1/shipment` **GET**
  - Get an array of all available shipments tracked on the platform
- `/api/v1/shipment/<shipment_id>` **GET**
  - Get the details of a single shipment

#### Profoma Invoice
- `/api/v1/pfi` **POST**
  - Create a new PFI, which automatically creates a new shipment
    - Required parameters
      - `item_detail`: detail of the shipment
      - `type`: type of importation
      - `supplier_name`: name of supplier supplying the product
      - `quantity`: quantity of items in this shipment
      - `cost`: amount for buying this item in this shipment
      - `hs_code`: rate to be paid
      - `pfi_number`: pfi number on form
- `/api/v1/pfi/<pfi_id>` **GET**
  - Get the details of a single `PFI`
- `/api/v1/pfi/<pfi_id>` **PUT**
  - Update a `PFI`
  - Required Parameters
    - `item_detail`: detail of the shipment
    - `type`: type of importation
    - `supplier_name`: name of supplier supplying the product
    - `quantity`: quantity of items in this shipment
    - `cost`: amount for buying this item in this shipment
    - `hs_code`: rate to be paid
    - `pfi_number`: pfi number on form

#### Form M
- `/api/v1/formm/<shipment_id>` **GET**
  - Get a details of a single `Form M`
- `/api/v1/formm` **POST**
  - Create a Form M for a shipment
  - Required Parameters
    - `shipments_id`: Current shipment that this form m belongs to
    - `formm_number`: Form M number on the document
- `/api/v1/formm/<foromm_id>` **PUT**
  - Update a Form m for a shipment
  - Required Paramters
    - `shipments_id`: Current shipment that this form m belongs to
    - `formm_number`: Form M number on the document

#### Required Permissions
- `/api/v1/permissions` **POST**
  - Create a permision for a particular shipment
  - Required Parameters
    - `permission_name`: The name of the permission to be obtained
    - `shipments_id`: The id of the current shipment
- `/api/v1/permissions/<shipments_id>` **GET**
  - Get all the permissions requried for a particular shipment
- `/api/v1/permissions/<permission_id>` **PUT**
  - Update a particular permission for a shipment
  - Required Parameters
    - `permission_name`: The name of the permission to be obtained
    - `shipments_id`: The id of the current shipment