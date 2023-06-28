import pandas as pd
from rich.console import Console
from date import get_date
from storage import write_storage
from functions_and_variables import get_id

console = Console()

# Register new product
def register_bought(product_name, price, amount, expiration_date):
    date = get_date()
    df = pd.read_csv("bought.csv")
    new_id = get_id(df,'bought_id')
    product = {"bought_id": [new_id],
               "product_name": [product_name], 
               "buy_date": [date],
               "price": [price],
               "amount": [amount], 
               "expiration_date": [expiration_date]}
    df = pd.DataFrame(product)
    df.to_csv("bought.csv", mode="a", index=False, header=False)
    write_storage()
    console.print(f"[green]You have registered as bought product: [blue]{amount} [white]{product_name} [green]which cost [blue]{price} [green]euros each, bought on [blue]{date}, [green]and it is going to expire on [red]{expiration_date}.")