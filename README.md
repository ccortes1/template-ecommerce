
# Basic template to an e-commerce
---
## Overview: 
This repository is a template of an e-commerce, is a project for deep about in the use of Django. anybody can take this repository for learning to build a simple e-commerce.

### Scope
In this project be build simple e-commerce with a product catalog, CRUD of users and products, and one system for creating invoices.
We use Django for the backend, SQLite for the database, and bootstrap for the frontend.

#### Use cases
Description...
* The customer can buy one or some products.
* The customer can register to buy unfilled the form of invoice or buy directly and fill the form in each purchase.
* The customer has a shopping cart.
* The owner of the store has a dashboard to manage the website and see the number of products in the inventory.

#### Out of Scope
Descripción...
* The owner of the store does not have statistics of the products and the users
* The shopping cart doesn't  save the products list when the browser close
---
## Architecture
This project uses a pattern of design MVC in a monolith connected to a database

### Modelo de datos
Poner diseño de entidades, Jsons, tablas, diagramas entidad relación, etc..

---
## Limitaciones
Lista de limitaciones conocidas. Puede ser en formato de lista.
Ej.
* Llamadas del API tienen latencia
* no se soporta mas de X llamadas por segundo

---
## Costo
Descripción/Análisis de costos
Ejemplo:
"Considerando N usuarios diarios, M llamadas a X servicio/baseDatos/etc"
* 1000 llamadas diarias a serverless functions. $XX.XX
* 1000 read/write units diarias a X Database on-demand. $XX.XX
Total: $xx.xx (al mes/dia/año)
