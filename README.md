Get All Products
GET /products
<img width="1346" height="631" alt="Screenshot 2026-04-28 132519" src="https://github.com/user-attachments/assets/d2ff666b-de2d-4f10-b357-7e60f68b5495" />

Get Product by ID

<img width="1269" height="637" alt="Screenshot 2026-04-28 135342" src="https://github.com/user-attachments/assets/a691b178-14a1-4c73-b679-e1e5712ce316" /># Product & Inventory Management REST APIA simple REST API for managing products and inventory with support for stock updates and inventory logging.---## 📌 Features### Product Management- Create a product- Get all products- Get product by ID- Update product- Delete product### Inventory Management- Add stock to a product- Remove stock from a product- Maintain inventory logs for all stock changes---## 📡 API Endpoints### 1. Products#### Create Product`POST /products````json{  "name": "iPhone 15",  "sku": "IPH15-128-BLK",  "price": 80000,  "quantity": 10}
GET /products/{id}

<img width="1272" height="655" alt="Screenshot 2026-04-28 135419" src="https://github.com/user-attachments/assets/015de417-de4e-41a1-945b-f69294d001b1" />

Update Product
PUT /products/{id}
# Product & Inventory Management REST APIA simple REST API for managing products and inventory with support for stock updates and inventory logging.---## 📌 Features### Product Management- Create a product- Get all products- Get product by ID- Update product- Delete product### Inventory Management- Add stock to a product- Remove stock from a product- Maintain inventory logs for all stock changes---## 📡 API Endpoints### 1. Products#### Create Product`POST /products````json{  "name": "iPhone 15",  "sku": "IPH15-128-BLK",  "price": 80000,  "quantity": 10}
Get All Products
GET /products
Get Product by ID
GET /products/{id}
Update Product
PUT /products/{id}
Delete Product
DELETE /products/{id}

2. Inventory
Add Stock
POST /inventory/add
{  "product_id": 1,  "quantity": 5}
Remove Stock
POST /inventory/remove
{  "product_id": 1,  "quantity": 2}

🗄️ Database Schema
Table: products
ColumnTypeConstraintsidINTPrimary KeynameVARCHARNOT NULLskuVARCHARUNIQUE, NOT NULLpriceDECIMALNOT NULLquantityINTNOT NULL (≥ 0)created_atTIMESTAMPDEFAULT CURRENT_TIMESTAMP

Table: inventory_logs
ColumnTypeConstraintsidINTPrimary Keyproduct_idINTForeign KeytypeENUMADD / REMOVEquantityINTNOT NULLcreated_atTIMESTAMPDEFAULT CURRENT_TIMESTAMP

⚙️ Business Rules


Product quantity can never be negative


Inventory updates must be atomic (use database transactions)


Every stock change must be recorded in inventory_logs



🚀 Notes


Ensure proper validation for all inputs


Handle errors gracefully (invalid product, insufficient stock, etc.)


Maintain clean and modular code structure


If you want, I can also:- make it more “GitHub professional” (badges, setup, tech stack, etc.)- or tailor it for Node.js / Java / Python specifically.
Delete Product
DELETE /products/{id}


2. Inventory
Add Stock
POST /inventory/add
{  "product_id": 1,  "quantity": 5}
Remove Stock
POST /inventory/remove
{  "product_id": 1,  "quantity": 2}

🗄️ Database Schema
Table: products
ColumnTypeConstraintsidINTPrimary KeynameVARCHARNOT NULLskuVARCHARUNIQUE, NOT NULLpriceDECIMALNOT NULLquantityINTNOT NULL (≥ 0)created_atTIMESTAMPDEFAULT CURRENT_TIMESTAMP

Table: inventory_logs
ColumnTypeConstraintsidINTPrimary Keyproduct_idINTForeign KeytypeENUMADD / REMOVEquantityINTNOT NULLcreated_atTIMESTAMPDEFAULT CURRENT_TIMESTAMP

⚙️ Business Rules


Product quantity can never be negative


Inventory updates must be atomic (use database transactions)


Every stock change must be recorded in inventory_logs



🚀 Notes


Ensure proper validation for all inputs


Handle errors gracefully (invalid product, insufficient stock, etc.)


Maintain clean and modular code structure


If you want, I can also:- make it more “GitHub professional” (badges, setup, tech stack, etc.)- or tailor it for Node.js / Java / Python specifically.

FRONTEND RUN ON :- http://localhost:5173/
BACKEND RUN ON :- http://localhost:8000/
