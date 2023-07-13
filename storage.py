import csv
import pandas as pd
from rich import print as rprint
from date import today
from functions_and_variables import no_data

# Data
bought_products = "bought.csv"
sold_products = "sold.csv"
 
# Read bought items
def read_bought():
    with open(bought_products, "r") as bought:
        bought_reader = csv.DictReader(bought, delimiter=",")
        list_of_bought = list(bought_reader) 
        return list_of_bought
    
# Read sold items   
def read_sold():
    with open(sold_products, "r") as sold:
        sold_reader = csv.DictReader(sold, delimiter=",")
        list_of_sold = list(sold_reader)
        return list_of_sold

# Read currently avaliabe storage
def read_storage():
    with open("storage.csv", "r") as current_storage:
        csv_reader = csv.DictReader(current_storage, delimiter=",")
        list_of_csv = list(csv_reader) 
        return list_of_csv 

# Get the currently available storage from the bought and sold items
def get_storage():
    bought = read_bought()
    sold = read_sold()
    sold_bought_id = []
    for item in sold:
        sold_bought_id.append(item["bought_id"])
    for product in bought:
        if product["bought_id"] in sold_bought_id:
            for item in sold:
                if product["product_name"] == item["product_name"] and product["bought_id"] == item["bought_id"]:
                    storage_amount =  (int(product["amount"]) - int(item["amount"]))
                    product["amount"] = storage_amount
                    if int(product["amount"]) < 0:
                        product["amount"] = 0               
    return bought   

# Check avilable products by product name
def check_available_product_by_name(name):
    products = read_storage()
    product_list = []
    for product in products:
        if product["product_name"] == name and product["expiration_date"] >= str(today):
            product_list.append(product)
    if product_list != []:
        return product_list
    else:
        rprint("[red]Sorry, there isn't any product at the moment available with this product name!")

# Show how much product is exactly available from the searched product
def sum_available(name):
    product = check_available_product_by_name(name)
    amount = []
    for item in product:
        amount.append(int(item["amount"]))
    Sum = sum(amount)
    rprint(f'[green]You have [blue]{Sum} [green]available [blue]{name} [green]for sale!')

# Writes the actual storage into a csv file
def write_storage():
    storage = get_storage()
    df = pd.DataFrame(storage)
    if df.empty:
        return
    else:
        new_df = df[(df.expiration_date >= today.strftime('%Y-%m-%d')) & (df.amount != 0)]
        new_df.to_csv("storage.csv", index=False, header=True)

# Filters out all the products that are expired
def show_expired_products(date=today):
    bought = read_bought()
    expired_products = []
    for product in bought:
        if product["expiration_date"] < str(date):
            expired_products.append(product)     
    return expired_products 
 
# Export expired products into csv
def write_expired_products(date=today):
    expired = show_expired_products(date)
    write_storage()
    df  = pd.DataFrame(expired)
    df.to_csv("expired.csv", index=False, header=True)      

# Read expired products:
def read_expired():
    write_expired_products()
    with open("expired.csv", "r") as expired:
        expired_reader = csv.DictReader(expired, delimiter=",")
        list_of_expired = list(expired_reader)
        return list_of_expired    