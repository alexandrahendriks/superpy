import pandas as pd
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from storage import read_expired
from date import today
from functions_and_variables import get_table, can_not_set, total_loss, no_data

console = Console()
# Data
expired = read_expired()

# Calculating total money loss from expired items
def money_loss():
    price = []
    for product in expired:
        loss_per_item = float(product["price"]) * int(product["amount"])
        price.append(loss_per_item)
    loss = sum(price)
    total_loss(price, loss)
    table = Table(title="")
    df = pd.DataFrame(expired)
    if df.empty:
        rprint(no_data)
        return
    else:
        get_table(df, table, "red")
        console.print(table)

# Calculating total money loss from expired items by name
def money_loss_by_product_name(name):
    price = []
    products = []
    for product in expired:
       if product["product_name"] == name:
          products.append(product)
          loss_per_item = float(product["price"]) * int(product["amount"])
          price.append(loss_per_item)
    loss = sum(price)
    total_loss(price, loss)
    return products  

# Calculating total money loss from expired items by date
def money_loss_by_date(date=today):
    price = []
    products = []
    if date > today:
        rprint(can_not_set)
        return
    for product in expired:
       if product["expiration_date"] == str(date):
          products.append(product)
          loss_per_item = float(product["price"]) * int(product["amount"])
          price.append(loss_per_item)
    loss = sum(price)
    total_loss(price, loss)
    df = pd.DataFrame(products)
    table = Table(title="")
    if df.empty:
        rprint(no_data)
        return
    else:
        get_table(df, table, "red")
        console.print(table)
    return products

# Calculating total money loss from expired items between dates
def money_loss_between_dates(date1=today, date2=today):
    price = []
    products = []
    if date2 > today:
        rprint(can_not_set)
        return
    for product in expired:
       if product["expiration_date"] >= str(date1) and product["expiration_date"] < str(date2):
          products.append(product)
          loss_per_item = float(product["price"]) * int(product["amount"])
          price.append(loss_per_item)
    loss = sum(price)
    total_loss(price, loss)
    df = pd.DataFrame(products)
    table = Table(title="")
    if df.empty:
        rprint(no_data)
        return
    else:
        get_table(df, table, "red") 
        console.print(table)
    return products    

