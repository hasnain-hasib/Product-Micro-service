from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    
    
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials= True,
    allow_methods=["*"],
    allow_headers=["*"],
)

redis = get_redis_connection(
    host="redis-16048.c305.ap-south-1-1.ec2.redns.redis-cloud.com",
    port=16048,
    password="7Zes7380K476LtxNOvs4nrKUqhPkh6ZR",
    decode_responses=True 
)

class Product(HashModel):
    name: str
    price: float
    quantity: int
    
    class Meta:
        database = redis

@app.get("/products")
def all():
    return [Product.get(pk) for pk in Product.all_pks()]

@app.post('/products')
def create(product: Product):
    return product.save()
    
