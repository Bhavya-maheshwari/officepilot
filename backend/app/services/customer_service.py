from app.models.customer import Customer

customers = []


def get_customers():
    return customers


def add_customer(customer: Customer):
    customers.append(customer)
    return customer