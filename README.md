Get All Products
GET /products
<img width="1346" height="631" alt="Screenshot 2026-04-28 132519" src="https://github.com/user-attachments/assets/d2ff666b-de2d-4f10-b357-7e60f68b5495" />

Get Product by ID

<img width="1269" height="637" alt="Screenshot 2026-04-28 135342" src="https://github.com/user-attachments/assets/a691b178-14a1-4c73-b679-e1e5712ce316" /># Product & Inventory Management REST APIA simple REST API for managing products and inventory with support for stock updates and inventory logging.---## 📌 Features### Product Management- Create a product- Get all products- Get product by ID- Update product- Delete product### Inventory Management- Add stock to a product- Remove stock from a product- Maintain inventory logs for all stock changes---## 📡 API Endpoints### 1. Products#### Create Product`POST /products````json{  "name": "iPhone 15",  "sku": "IPH15-128-BLK",  "price": 80000,  "quantity": 10}
GET /products/{id}

<img width="1272" height="655" alt="Screenshot 2026-04-28 135419" src="https://github.com/user-attachments/assets/015de417-de4e-41a1-945b-f69294d001b1" />

Update Product
PUT /products/{id}

Get All Products
GET /products
<img width="831" height="550" alt="Screenshot 2026-04-28 135654" src="https://github.com/user-attachments/assets/172b73c9-3bf5-4d81-82b0-0d64596285d0" />
Get Product by ID
<img width="842" height="307" alt="Screenshot 2026-04-28 135741" src="https://github.com/user-attachments/assets/1cad6599-93f2-4bda-a396-3d9af7d83f09" />
GET /products/{id}
Update Product
<img width="1280" height="641" alt="Screenshot 2026-04-28 140006" src="https://github.com/user-attachments/assets/673764ac-45b1-470a-bc0d-6f1f51d098d6" />
PUT /products/{id}
Delete Product
DELETE /products/{id}

2. Inventory
Add Stock
POST /inventory/add

Remove Stock
POST /inventory/remove

<img width="1281" height="653" alt="Screenshot 2026-04-28 135858" src="https://github.com/user-attachments/assets/2256a85e-2d2d-40ce-b040-52a44347c46e" />



⚙️ Business Rules
Product quantity can never be negative
Inventory updates must be atomic (use database transactions)
Every stock change must be recorded in inventory_logs

🚀 Notes
Ensure proper validation for all inputs
Handle errors gracefully (invalid product, insufficient stock, etc.)
Maintain clean and modular code structure

<img width="1279" height="633" alt="Screenshot 2026-04-28 135944" src="https://github.com/user-attachments/assets/572faaad-a76d-4c06-be1f-b816e8cad650" />



FRONTEND RUN ON :- http://localhost:5173/
BACKEND RUN ON :- http://localhost:8000/
