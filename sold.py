import pandas as pd
from rich.console import Console
from rich import print as rprint
from date import get_date
from storage import write_storage, read_storage
from functions_and_variables import get_id

console = Console()

# Register sold product
def register_sold(product_name, amount, price, expiration_date):
    date = get_date()
    storage = read_storage()
    df = pd.read_csv("sold.csv")
    for name in storage:
        if product_name == name["product_name"] and str(expiration_date) == name["expiration_date"]:
            bought_id = name["bought_id"]
            new_id = get_id(df,'id')
            product = {"id": [new_id],
                        "bought_id": [bought_id],
                        "product_name": [product_name], 
                        "amount": [amount],
                        "sell_date": [date],
                        "sell_price": [price]}
            df = pd.DataFrame(product)
            df.to_csv("sold.csv", mode="a", index=False, header=False)
            write_storage()
            console.print(f"[green]You have registered as a sold product: [blue]{amount} [white]{product_name}[green], sold for [blue]{price} [green]euros each on [blue]{date}.")
            break
    else:
        rprint("[red]There is no product with the given information!")