from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

products = []
orders = []

@app.get("/")
def home():
    return {"status": "Backend running"}

@app.get("/products")
def get_products():
    return products

@app.post("/products")
def add_product(product: dict):
    products.append(product)
    return {"message": "Product added"}

@app.get("/orders")
def get_orders():
    return orders

@app.post("/orders")
def create_order(order: dict):
    orders.append(order)
    return {"message": "Order created"}
