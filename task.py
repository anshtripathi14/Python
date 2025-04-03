import time
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

def log_function(func):
    def wrapper(*args, **kwargs):
        logging.info(F"Function Calling: {func.__name__} with arguments= {args}, keyword_arguments={kwargs}")
        result= func(*args, **kwargs)
        logging.info(f"Function {func.__name__} returned {result}")
        return result 
    return wrapper

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start= time.time()
        result =func(*args, **kwargs)
        end= time.time()
        logging.info(f"Execution time for {func.__name__}: {end - start} seconds")
        return result
    return wrapper

def read_products(file_path):
    products=[]
    with open(file_path, 'r') as file:
        for line in file:
            name, price, quantity= line.strip().split(',')
            products.append({
                'product_name': name,
                'price': float(price),
                'quantity': int(quantity)
            })
    return products

@log_function
@measure_execution_time
def  sort_products_by_price(products):
    return sorted(products, key=lambda x: x['price'])

@log_function
@measure_execution_time
def find_most_expensive_product(products):
    return max(products, key=lambda x: x['price'])

@log_function
@measure_execution_time
def find_lowest_quantity_product(products):
    return min(products, key=lambda x: x['quantity'])

@log_function
@measure_execution_time
def create_unique_product_names(products):
    return set(product['product_name'] for product in products)

@log_function
@measure_execution_time
def filter_products_by_price(products, min_price):
    return [product for product in products if product['price'] > min_price]

def main():
    file_path = 'C:\\Users\\Ansh Tripathi\\OneDrive\\Desktop\\products.txt'
    
    products = read_products(file_path)
    
    sorted_products = sort_products_by_price(products)
    logging.info(f'Sorted products: {sorted_products}')
    print("\n")
    
    most_expensive_product = find_most_expensive_product(products)
    logging.info(f'Most expensive product: {most_expensive_product}')
    print("\n")
    
    lowest_quantity_product = find_lowest_quantity_product(products)
    logging.info(f'Product with the lowest quantity: {lowest_quantity_product}')
    print("\n")
    
    unique_product_names = create_unique_product_names(products)
    logging.info(f'Unique product names: {unique_product_names}')
    print("\n")
    
    min_price = 1.5 
    filtered_products = filter_products_by_price(products, min_price)
    logging.info(f'Products with price greater than {min_price}: {filtered_products}')
    print("\n")

if __name__ == '__main__':
    main()

