import pandas as pd
from datetime import date
from rich import print as rprint

# Variables
can_not_set = "[red]Date can not be set to future date!"
no_data = "[red]There is no data available!"


# Functions
# Get the id from the latest purchased or sold product
def get_id(df, id):
    last_id = df[id].max()
    if pd.isna(last_id) == True:
        last_id = 1
    else:
        last_id += 1
    return last_id

# Export products into a csv or excel file by date
def export(df, sort, date, file):
    if file == "csv":
        df.to_csv(f"{sort}_{date.strftime('%Y-%m-%d')}.csv", index=False, header=True)
        rprint(f"[green]The {sort} products of {date.strftime('%Y-%m-%d')} has been exported as {file} file.")
    elif file == "excel":
       df.to_excel(f"{sort}_{date.strftime('%Y-%m-%d')}.xlsx", sheet_name=f"{sort} products of {date.strftime('%Y-%m-%d')}", engine="xlsxwriter")
       rprint(f"[green]The {sort} products of {date.strftime('%Y-%m-%d')} has been exported as {file} file.")

# Export products between the specified dates to csv or excel files
def export_between(df, sort, date1, date2, file):
    if file == "csv":
        df.to_csv(f"{sort}_between_{date1.strftime('%Y-%m-%d')}_and_{date2.strftime('%Y-%m-%d')}.csv", index=False, header=True)
        rprint(f"[green]The {sort} products between {date1.strftime('%Y-%m-%d')} and {date2.strftime('%Y-%m-%d')} has been exported as {file} file.")
    elif file == "excel":
       df.to_excel(f"{sort}_between_{date1.strftime('%Y-%m-%d')}_and_{date2.strftime('%Y-%m-%d')}.xlsx", sheet_name=f"{sort} between {date1.strftime('%Y-%m-%d')} and {date2.strftime('%Y-%m-%d')}", engine="xlsxwriter")
       rprint(f"[green]The {sort} products between {date1.strftime('%Y-%m-%d')} and {date2.strftime('%Y-%m-%d')} has been exported as {file} file.") 

# Creates rich table to the console
def get_table(df, table, color):
    for column in df.columns.values:
        table.add_column(column, style=color)
    for index, row in df.iterrows():
        table.add_row(row[0], row[1], row[2], row[3], row[4], row[5])
    return table 

# Prints message for total loss
def total_loss(price, loss):
    if price == []:
        rprint(f"[green]There were no products expired!")
        return
    else:
        rprint(f"[red]The total loss is {round(loss, 2)} euros.\U0001F612")    

# Prints message for profit
def the_profit(profit):
    if profit != 0:
        rprint(f"[green]The total profit is {round(profit, 2)} euros.\U0001F911")
    else:
        rprint(f"[red]There weren't any products sold!")
        rprint(f"[red]The total profit is {profit} euro.\U0001F614")

# Prints message for revenue
def the_revenue(revenue):
    if revenue != 0:
        rprint(f"[green]The total revenue is {round(revenue, 2)} euros.\U0001F911")
    else:
        rprint(f"[red]There weren't any products sold!")
        rprint(f"[red]The total revenue is {revenue} euro.\U0001F614")        