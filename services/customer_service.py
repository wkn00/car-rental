from data_access.database import DatabaseAccess

class CustomerService:
    def __init__(self):
        self.database_access = DatabaseAccess()

    def add_new_customer(self, customer_name, customer_contactNumber, customer_email, customer_address):
        self.database_access.add_customer(customer_name, customer_contactNumber, customer_email, customer_address)

    def get_all_customers(self):
        return self.database_access.get_all_customers()
    