from typing import Dict
from fastapi import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    product_id : str
    product_name : str
    product_price : float

products : Dict[str , Product] = {}

@app.get("/")
def root():
    return "Product API"

@app.get("/products")
def get_product():
    return list(products.values())

@app.post("/products")
def create_product(product : Product):
    products[product.product_id] = product
    return {"message": "successfully Created product", "product": product}

@app.put("/product/{product_id}")
def update_product(product_id : str , product:Product) :
    if product_id not in products:
        raise HTTPException( status_code=404 , detail="product is not found")

    product[product_id] = product
    return {"message": "successfully Updated product", "product": product}

@app.delete("/product/{product_id}")
def delete_product(product_id : str , product:Product):
    if product_id not in products:
        raise HTTPException( status_code=404 , detail="product is not found")

    del_product = products.pop(product_id)
    return {"message": "successfully deleted product", "product": del_product}