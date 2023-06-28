from rich import print as rprint
from storage import read_sold, read_bought
from date import today
from functions_and_variables import the_profit, can_not_set


# Data
sold = read_sold()
bought = read_bought()

# Get the profit from all sold products
def get_total_profit():
    sold_bought_id = []
    profit_per_product = []
    sold_products = []
    for item in sold:
        sold_bought_id.append(item["bought_id"])
    for product in bought:
        if product["bought_id"] in sold_bought_id:
            for item in sold:
                if product["product_name"] == item["product_name"] and product["bought_id"] == item["bought_id"]:
                    sold_products.append(item)
                    profit_per_item = (float(item["sell_price"]) - (float(product["price"])))
                    total_profit = profit_per_item * int(item["amount"])
                    profit_per_product.append(total_profit)
    profit = sum(profit_per_product)
    the_profit(profit)
    return sold_products

# Get the total profit on today's date
def get_profit_today():
    sold_bought_id = []
    profit_per_product = []
    sold_products = []
    for item in sold:
        sold_bought_id.append(item["bought_id"])
    for product in bought:
        if product["bought_id"] in sold_bought_id:
            for item in sold:
                if item["sell_date"] == str(today) and product["bought_id"] == item["bought_id"]:
                    sold_products.append(item)
                    profit_per_item = (float(item["sell_price"]) - (float(product["price"])))
                    total_profit = profit_per_item * int(item["amount"])
                    profit_per_product.append(total_profit)
    profit = sum(profit_per_product)
    the_profit(profit)
    return sold_products
     
# Returns the total profit between give dates
def get_profit_between_dates(date1, date2):
    sold_bought_id = []
    profit_per_product = []
    sold_products = []
    if date1 > today or date2 >today:
        rprint(can_not_set)
        return
    for item in sold:
        sold_bought_id.append(item["bought_id"])
    for product in bought:
        if product["bought_id"] in sold_bought_id:
            for item in sold:
               if item["sell_date"] >= str(date1) and item["sell_date"] <= str(date2) and product["bought_id"] == item["bought_id"]:
                    sold_products.append(item)
                    profit_per_item = (float(item["sell_price"]) - (float(product["price"])))
                    total_profit = profit_per_item * int(item["amount"])
                    profit_per_product.append(total_profit)
    profit = sum(profit_per_product)
    the_profit(profit)
    return sold_products
    
# Returns the total profit on a given date
def get_profit_by_date(date):
    sold_bought_id = []
    profit_per_product = []
    sold_product = []
    if date > today:
        rprint(can_not_set)
        return
    for item in sold:
        sold_bought_id.append(item["bought_id"])
    for product in bought:
        if product["bought_id"] in sold_bought_id:
            for item in sold:
               if item["sell_date"] == str(date) and product["bought_id"] == item["bought_id"]: 
                    sold_product.append(item)
                    profit_per_item = (float(item["sell_price"]) - (float(product["price"])))
                    total_profit = profit_per_item * int(item["amount"])
                    profit_per_product.append(total_profit)
    profit = sum(profit_per_product)
    the_profit(profit)
    return sold_product

# Returns the total profit for an exact product
def get_profit_by_product(name):
    sold_bought_id = []
    profit_per_product = []
    sold_product = []
    for item in sold:
        sold_bought_id.append(item["bought_id"])   
    for product in bought:
        if product["bought_id"] in sold_bought_id:
            for item in sold:
                if item["product_name"] == name and product["bought_id"] == item["bought_id"]: 
                    sold_product.append(item)
                    profit_per_item = (float(item["sell_price"]) - (float(product["price"])))
                    total_profit = profit_per_item * int(item["amount"])
                    profit_per_product.append(total_profit)
    if profit_per_product == []:
        rprint(f"[yellow]There wasn't any {name} sold.")
    else:
        profit = sum(profit_per_product)
        rprint(f"[green]The total profit for {name} is {round(profit, 2)} euro.\U0001F911")
        return sold_product

