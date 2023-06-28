from rich import print as rprint
from storage import read_sold
from date import today
from functions_and_variables import the_revenue, can_not_set
# Data
sold = read_sold()

# Get the revenue of all sold items
def get_total_revenue():
    price = []
    sold_products = []
    for product in sold:
        sold_products.append(product)
        price.append(float(product["sell_price"]) * int(product["amount"]))
    sold_price = sum(price)
    the_revenue(sold_price)
    return sold_products 

# Get the total revenue today
def get_revenue_today():
    sell_price = []
    sold_products = []
    for product in sold:
        if product["sell_date"] == str(today):
            sold_products.append(product)
            sell_price.append(float(product["sell_price"]) * int(product["amount"]))           
    revenue = sum(sell_price)
    the_revenue(revenue)
    return sold_products

# Get the total revenue on an exact date
def get_revenue_by_date(date):
    sell_price = []
    sold_products = []
    if str(date) > str(today):
        rprint("[red]Date can not be set to future date!")
        return
    for product in sold:
        if product["sell_date"] == str(date):
            sold_products.append(product)
            sell_price.append(float(product["sell_price"]) * int(product["amount"]))      
    revenue = sum(sell_price)
    the_revenue(revenue) 
    return sold_products

# Get the total revenue in a period of time
def get_revenue_between_dates(date1, date2):
    sell_price = []
    sold_products = []
    if date1 > today or date2 > today:
        rprint(can_not_set)
        return
    for product in sold:
        if product["sell_date"] >= str(date1) and product["sell_date"] <= str(date2):
            sold_products.append(product)
            sell_price.append(float(product["sell_price"]) * int(product["amount"]))  
    revenue = sum(sell_price)
    the_revenue(revenue)
    return sold_products

