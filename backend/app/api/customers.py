from fastapi import APIRouter
from app.models.customer import Customer
from app.services.customer_service import add_customer, get_customers

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.get("/")
def list_customers():
    return get_customers()


@router.post("/")
def create_customer(customer: Customer):
    return add_customer(customer)