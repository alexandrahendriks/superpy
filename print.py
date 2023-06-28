import pandas as pd
from rich.console import Console
from rich.table import Table
from rich import print as rprint
from storage import read_bought, read_sold, read_storage, read_expired, check_available_product_by_name
from profit import get_total_profit, get_profit_by_product, get_profit_by_date, get_profit_between_dates, get_profit_today
from revenue import get_total_revenue, get_revenue_today, get_revenue_between_dates, get_revenue_by_date
from date import today, date_and_time
from functions_and_variables import no_data, get_table

console = Console()
# Print date and time
# Returns and prints todays date
def print_date():
    rprint(f"[green]Today's date is:[green] {today}")
# Returns and prints current date and time
def print_date_and_time():
    rprint(f"[green]Today's date and time is:[green] {date_and_time}")

# Print dataframes into the console
# Print Inventory
# Print sold csv
def print_sold():
    table = Table(title="[bold][yellow]Sold Products")
    df = pd.DataFrame(read_sold()) 
    if df.empty:
        rprint(no_data)
        return
    else:
        get_table(df, table, "yellow") 
        console.print(table) 

# Print storage
def print_storage():
    table = Table(title="[bold][green]Current Storage")
    df = pd.DataFrame(read_storage())
    if df.empty:
        rprint(no_data)
        return
    else:
        get_table(df, table, "green")
        console.print(table)  

# Print bought csv
def print_bought():
    table = Table(title="[bold][blue]Bought Products")
    df = pd.DataFrame(read_bought())
    if df.empty:
        rprint(no_data)
        return
    else:
        get_table(df, table, "cyan")
        console.print(table)    

# Print expired products
def print_expired():
    table = Table(title="[bold][red]Expired Products")
    df = pd.DataFrame(read_expired())
    if df.empty:
        rprint(f"[green]There is no data available!")
        return
    else:
        get_table(df, table, "red")
        console.print(table)  

# Print available products by given name
def print_available_product(name):
    table = Table(title=f"[bold][green]Available {name}")
    df = pd.DataFrame(check_available_product_by_name(name))
    if df.empty:
        rprint(no_data)
        return
    else:
        get_table(df, table, "green")
        console.print(table)  

# Print Profit
# Print dataframe for the total profit
def print_df_for_total_profit():
    table = Table(title="")
    df = pd.DataFrame(get_total_profit())
    if df.empty:
        return
    else:
        get_table(df, table, "cyan")
        console.print(table)  

# Print dataframe for the profit today
def print_df_for_profit_today():
    table = Table(title="")
    df = pd.DataFrame(get_profit_today())
    if df.empty:
        return
    else:
        get_table(df, table, "cyan")
        console.print(table)  

# Print dataframe for the profit on a given date
def print_df_for_profit_on_given_date(date):
    table = Table(title="")
    df = pd.DataFrame(get_profit_by_date(date))
    if df.empty:
        return
    else:
        get_table(df, table, "cyan")
        console.print(table)  

# Print dataframe for the profit between two dates
def print_df_for_profit_between_dates(date1, date2):
    table = Table(title="")
    df = pd.DataFrame(get_profit_between_dates(date1, date2))
    if df.empty:
        return
    else:
        get_table(df, table, "cyan")
        console.print(table)  

# Print dataframe for the profit on exact product
def print_df_for_profit_by_product_name(name):
    table = Table(title="")
    df = pd.DataFrame(get_profit_by_product(name))
    if df.empty:
        return
    else:
        get_table(df, table, "cyan")
        console.print(table)  

# Print Revenue
# Print dataframe for the total revenue
def print_df_for_total_revenue():
    table = Table(title="")
    df = pd.DataFrame(get_total_revenue())
    if df.empty:
        return
    else:
        get_table(df, table, "cyan")
        console.print(table)  

# Print dataframe for revenue today
def print_df_for_revenue_today():
    table = Table(title="")
    df = pd.DataFrame(get_revenue_today())
    if df.empty:
        return
    else:
        get_table(df, table, "cyan")
        console.print(table)  

# Print dataframe for the revenue on a given date
def print_df_for_revenue_on_given_date(date):
    table = Table(title="")
    df = pd.DataFrame(get_revenue_by_date(date))
    if df.empty:
        return
    else:
        get_table(df, table, "cyan")
        console.print(table)  

# Print dataframe for the revenue between two dates
def print_df_for_revenue_between_dates(date1, date2):
    table = Table(title="")
    df = pd.DataFrame(get_revenue_between_dates(date1, date2))
    if df.empty:
        return
    else:
        get_table(df, table, "cyan")
        console.print(table)
