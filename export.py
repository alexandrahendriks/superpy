import pandas as pd
from rich import print as rprint
from storage import get_storage, show_expired_products
from profit import get_profit_by_date, get_profit_between_dates
from date import today
from loss import money_loss_by_date, money_loss_between_dates
from functions_and_variables import can_not_set, no_data, export, export_between

# Export storage on specified dates to csv or excel files
def export_storage(file, date=today):
    df = pd.DataFrame(get_storage())
    new_df = df[(df.expiration_date >= date.strftime("%Y-%m-%d")) & (df.amount != 0) & (df.buy_date <= date.strftime("%Y-%m-%d"))]
    if date > today:
        rprint(can_not_set)
        return
    if df.empty or new_df.empty:
        rprint(no_data)
        return
    else:
        export(new_df, "storage", date, file)

# Export expired products on specified dates to csv or excel files
def export_expired(file, date=today):
    df = pd.DataFrame(show_expired_products(date))
    if date > today:
        rprint(can_not_set)
        return
    if df.empty:
        rprint(no_data)
        return
    else:
        export(df, "expired", date, file)

# Export products that were sold on the specified dates to csv or excel files
def export_products_sold_on_date(file, date=today):
    df = pd.DataFrame(get_profit_by_date(date))
    if date > today:
        rprint(can_not_set)
        return
    if df.empty:
        rprint(no_data)
        return
    else:
        export(df, "sold", date, file)

# Export products that were sold between the specified dates to csv or excel files
def export_products_sold_between_dates(file, date1=today, date2=today):
    df = pd.DataFrame(get_profit_between_dates(date1, date2))
    if date2 > today:
        return
    if df.empty and date2 <= today:
        rprint(no_data)
        return
    else:
        export_between(df, "sold", date1, date2, file)

# Export products that cause money loss on the specified date to csv or excel files
def export_products_expired_by_date(file, date=today):
    df = pd.DataFrame(money_loss_by_date(date))
    if date > today:
        return
    if df.empty:
        return
    else:
        export(df, "lost", date, file)

# Export products that cause money loss between the specified dates to csv or excel files
def export_products_expired_between_dates(file, date1=today, date2=today):
    df = pd.DataFrame(money_loss_between_dates(date1, date2))
    if date2 > today:
        return
    if df.empty:
        return
    else:
        export_between(df, "lost", date1, date2, file)