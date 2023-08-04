# Dummy data
import random

# Generate random data for sales_data, inventory_data, and product_data
products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
sales_data = {product: random.randint(100, 1000) for product in products}
inventory_data = {product: random.randint(50, 200) for product in products}
product_data = {chr(65 + i): random.randint(10, 100) for i in range(5)}

# Generate random data for sales_year_data
sales_year_data = {year: random.randint(5000, 20000) for year in range(2018, 2023)}

# Generate random data for inventory_month_data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
inventory_month_data = {month: random.randint(200, 1500) for month in months}
