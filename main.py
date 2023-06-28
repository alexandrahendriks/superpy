# Imports
import argparse
import datetime
from date import show_checkpoint, set_date, set_date_manually, advanced_date_forward, advanced_date_backwards
from bought import register_bought
from print import print_bought, print_sold, print_storage, print_expired, print_available_product, print_df_for_profit_between_dates, print_df_for_profit_by_product_name, print_df_for_profit_on_given_date, print_df_for_profit_today, print_df_for_revenue_between_dates, print_df_for_revenue_on_given_date, print_df_for_revenue_today, print_df_for_total_profit, print_df_for_total_revenue, print_date, print_date_and_time
from loss import money_loss, money_loss_between_dates, money_loss_by_date, money_loss_by_product_name
from storage import sum_available
from sold import register_sold
from export import export_storage, export_expired, export_products_sold_between_dates, export_products_sold_on_date, export_products_expired_between_dates, export_products_expired_by_date

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.
def main():

# Defining argument parser
    parser = argparse.ArgumentParser(prog="SuperPy", description="Data processing")

    # Defining subparser

    subparser = parser.add_subparsers(title="subcommands", description="valid subcommands", dest="subcommand", required=True)
    # Add parsers
    # Date parsers
    show_date = subparser.add_parser("date", help="It shows you the current date")
    show_date_and_time = subparser.add_parser("date-and-time", help="It shows you the current date and time")
    show_chekpoint = subparser.add_parser("checkpoint", help="It shows you the date of the last time when the date file was updated")
    set_current_date = subparser.add_parser("set-current-date", help="Updates date file with the current date.")
    set_date_manual = subparser.add_parser("set-date-manually", help="Set the date from manual input")
    advance_date_forwards = subparser.add_parser("advance-date-forwards", help="Advance the date by 'x' amount of days forwards")
    advance_date_backwards = subparser.add_parser("advance-date-backwards", help="Advance the date by 'x' amount of days backwards")

    set_date_manual.add_argument("-d", "--date",  type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date(), help="Set the date in the format of YYYY-MM-DD", required=True)
    advance_date_forwards.add_argument("-d", "--date", type=int, help="Add amount of days you want to advance the date forward with. It must to be a number!", required=True)
    advance_date_backwards.add_argument("-d", "--date", type=int, help="Add amount of days you want to advance the date backwards with. It must to be a number!", required=True)
    
    #Register new product
    bought_product = subparser.add_parser("register-bought", help="Register the newly purchased product")
    bought_product.add_argument("-pn", "--productname", type=str, help="Enter the name of the product", required=True)
    bought_product.add_argument("-p", "--price", type=float, help="Enter the price of the product", required=True)
    bought_product.add_argument("-a", "--amount", type=int, help="Enter the amount of the product that has been bought", required=True)
    bought_product.add_argument("-ed", "--expirationdate", type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date(), help="Enter the expiration date of the product", required=True)

    # Register sold product

    sold_product = subparser.add_parser("register-sold", help="Register sold product")
    sold_product.add_argument("-pn", "--productname", type=str, help="Enter the name of the product", required=True)
    sold_product.add_argument("-a", "--amount", type=int, help="Enter the amount of the product that has been sold", required=True)
    sold_product.add_argument("-p", "--price", type=float, help="Enter the price of the product", required=True)
    sold_product.add_argument("-ed", "--expirationdate", type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date(), help="Enter the expiration date of the product that has been sold", required=True)

    #Report storage
    current_storage = subparser.add_parser("storage", help="Shows the currently available products in the storage")
    bought = subparser.add_parser("bought", help="Shows all the bought products until now")
    sold = subparser.add_parser("sold", help="Shows all the sold products")
    expired = subparser.add_parser("expired", help="Shows all expired products")
    available_product = subparser.add_parser("product", help="Shows if the specified product available for sale or not")
    available_product.add_argument("-n", "--name", type=str, help="Enter the name of the product", required=True)

    amount_of_available_product = subparser.add_parser("amount", help="Shows the amount what is available from the specified product")
    amount_of_available_product.add_argument("-n", "--name", type=str, help="Enter the name of the product", required=True)

    # Profit and loss
    profit_loss = subparser.add_parser("money-loss", help="It shows how much money the supermarket lost from the expired items")
    profit_loss_by_name = subparser.add_parser("money-loss-by-name", help="It shows how much money the supermarket lost from the expired items by product name")
    profit_loss_by_name.add_argument("-n", "--name", required=True, type=str, help="Enter the name of the product")

    profit_loss_by_date = subparser.add_parser("money-loss-by-date", help="It shows how much money the supermarket lost from the expired items on the given date")
    profit_loss_by_date.add_argument("-d", "--date", required=True, type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date() , help="Set the date in the format of YYYY-MM-DD")

    profit_loss_between = subparser.add_parser("money-loss-between-dates", help="It shows how much money the supermarket lost from the expired items between the given dates")
    profit_loss_between.add_argument("-d1", "--date1", required=True, type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date(), help="Set the date in the format of YYYY-MM-DD")
    profit_loss_between.add_argument("-d2", "--date2", required=True, type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date(), help="Set the date in the format of YYYY-MM-DD")

    total_profit = subparser.add_parser("total-profit", help="It shows the total profit from all the sold products")
    profit_today = subparser.add_parser("profit-today", help="Shows the current date's profit")
    profit_by_date = subparser.add_parser("profit-by-date", help="Shows the profit on the specified date")
    profit_by_date.add_argument("-d", "--date", type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date(), help="Set the date in the format of YYYY-MM-DD", required=True)

    profit_between_dates = subparser.add_parser("profit-between-dates", help="Shows the profit between specified dates")
    profit_between_dates.add_argument("-d1", "--date1", type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date(), help="Set the date in the format of YYYY-MM-DD", required=True)
    profit_between_dates.add_argument("-d2", "--date2", type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date(), help="Set the date in the format of YYYY-MM-DD", required=True)

    profit_by_product = subparser.add_parser("profit-by-product", help="Shows the profit of a specified product")
    profit_by_product.add_argument("-n", "--name", type=str, help="Enter the name of the product", required=True)
    
    # Revenue
    revenue_today = subparser.add_parser("revenue-today", help="Shows the current date's revenue")
    total_revenue = subparser.add_parser("total-revenue", help="It shows the total revenue from all the sold products")

    revenue_by_date = subparser.add_parser("revenue-by-date", help="Shows the revenue on the specified date")
    revenue_by_date.add_argument("-d", "--date", type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date(), help="Set the date in the format of YYYY-MM-DD", required=True)

    revenue_between_dates = subparser.add_parser("revenue-between-dates", help="Shows the revenue between specified dates")
    revenue_between_dates.add_argument("-d1", "--date1", type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date(), help="Set the date in the format of YYYY-MM-DD", required=True)
    revenue_between_dates.add_argument("-d2", "--date2", type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date(), help="Set the date in the format of YYYY-MM-DD", required=True)
    
    # Export
    export_stor = subparser.add_parser("export-storage", help="Export storage until given date into csv or excel file")
    export_stor.add_argument("-f", "--format", type=str, required=True, help="Please choose from csv or excel!")
    export_stor.add_argument("-d", "--date", type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date(), help="Set the date in the format of YYYY-MM-DD", required=True)

    export_exp = subparser.add_parser("export-expired", help="Export expired products until the given date into csv or excel file")
    export_exp.add_argument("-f", "--format", type=str, required=True, help="Please choose from csv or excel!")
    export_exp.add_argument("-d", "--date", type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date(), help="Set the date in the format of YYYY-MM-DD", required=True)

    export_sold_by_date = subparser.add_parser("export-sold", help="Export products that were sold on given date into csv or excel file")
    export_sold_by_date.add_argument("-f", "--format", type=str, required=True, help="Please choose from csv or excel!")
    export_sold_by_date.add_argument("-d", "--date", type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date(), help="Set the date in the format of YYYY-MM-DD", required=True)

    export_sold_between_dates = subparser.add_parser("export-sold-between", help="Export products that were sold between given dates into csv or excel file")
    export_sold_between_dates.add_argument("-f", "--format", type=str, required=True, help="Please choose from csv or excel!")
    export_sold_between_dates.add_argument("-d1", "--date1", type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date(), help="Set the date in the format of YYYY-MM-DD", required=True)
    export_sold_between_dates.add_argument("-d2", "--date2", type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date(), help="Set the date in the format of YYYY-MM-DD", required=True)
    
    export_loss_by_date = subparser.add_parser("export-loss", help="Export products that casues loss on the given date into csv or excel file")
    export_loss_by_date.add_argument("-f", "--format", type=str, required=True, help="Please choose from csv or excel!")
    export_loss_by_date.add_argument("-d", "--date", type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date(), help="Set the date in the format of YYYY-MM-DD", required=True)

    export_loss_between_dates = subparser.add_parser("export-loss-between", help="Export products that casues loss between given dates into csv or excel file")
    export_loss_between_dates.add_argument("-f", "--format", type=str, required=True, help="Please choose from csv or excel!")
    export_loss_between_dates.add_argument("-d1", "--date1", type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date(), help="Set the date in the format of YYYY-MM-DD", required=True)
    export_loss_between_dates.add_argument("-d2", "--date2", type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date(), help="Set the date in the format of YYYY-MM-DD", required=True)

    args = parser.parse_args()

    # Adding functions to commands

    # Date commands
    if args.subcommand == "date":
        show_date.set_defaults(function=print_date())

    if args.subcommand == "date-and-time":
        show_date_and_time.set_defaults(function=print_date_and_time()) 

    if args.subcommand == "checkpoint":
        show_chekpoint.set_defaults(function=show_checkpoint())

    if args.subcommand == "set-current-date":
        set_current_date.set_defaults(function=set_date())  

    if args.subcommand == "set-date-manually":
        set_date_manual.set_defaults(function=set_date_manually(args.date))

    if args.subcommand == "advance-date-forwards":
        advance_date_forwards.set_defaults(function=advanced_date_forward(args.date))  

    if args.subcommand == "advance-date-backwards":
        advance_date_backwards.set_defaults(function=advanced_date_backwards(args.date))      

    # Register bought products command       
    if args.subcommand == "register-bought":
        bought_product.set_defaults(function=register_bought(args.productname, args.price, args.amount, args.expirationdate)) 

    # Register sold product command

    if args.subcommand == "register-sold":
        sold_product.set_defaults(function=register_sold(args.productname, args.amount, args.price, args.expirationdate))

    # Storage commands
    if args.subcommand == "storage":
        current_storage.set_defaults(function=print_storage())

    if args.subcommand == "bought":
        bought.set_defaults(function=print_bought())

    if args.subcommand == "sold":
        sold.set_defaults(function=print_sold())

    if args.subcommand == "expired":
        expired.set_defaults(function=print_expired())  

    if args.subcommand == "product":
        available_product.set_defaults(function=print_available_product(args.name))

    if args.subcommand == "amount":
        amount_of_available_product.set_defaults(function=sum_available(args.name))    

    # Profit and loss commands

    if args.subcommand == "money-loss":
        profit_loss.set_defaults(function=money_loss()) 

    if args.subcommand == "money-loss-by-name":
        profit_loss_by_name.set_defaults(function=money_loss_by_product_name(args.name))

    if args.subcommand == "money-loss-by-date":
        profit_loss_by_date.set_defaults(function=money_loss_by_date(args.date))

    if args.subcommand == "money-loss-between-dates":
        profit_loss_between.set_defaults(function=money_loss_between_dates(args.date1, args.date2))                      

    if args.subcommand == "total-profit":
        total_profit.set_defaults(function=print_df_for_total_profit())

    if args.subcommand == "profit-today":
        profit_today.set_defaults(function=print_df_for_profit_today())   

    if args.subcommand == "profit-by-date":
        profit_by_date.set_defaults(function=print_df_for_profit_on_given_date(args.date))   

    if args.subcommand == "profit-between-dates":
        profit_between_dates.set_defaults(function=print_df_for_profit_between_dates(args.date1, args.date2))

    if args.subcommand == "profit-by-product":
        profit_by_product.set_defaults(function=print_df_for_profit_by_product_name(args.name))       

    # Revenue commands

    if args.subcommand == "total-revenue":
        total_revenue.set_defaults(function=print_df_for_total_revenue())   

    if args.subcommand == "revenue-today":
        revenue_today.set_defaults(function=print_df_for_revenue_today())   

    if args.subcommand == "revenue-by-date":
        revenue_by_date.set_defaults(function=print_df_for_revenue_on_given_date(args.date))   

    if args.subcommand == "revenue-between-dates":
        revenue_between_dates.set_defaults(function=print_df_for_revenue_between_dates(args.date1, args.date2))                   

    # Export commands

    if args.subcommand == "export-storage":
        export_stor.set_defaults(function=export_storage(args.format, args.date)) 

    if args.subcommand == "export-expired":
        export_exp.set_defaults(function=export_expired(args.format, args.date)) 

    if args.subcommand == "export-sold":
        export_sold_by_date.set_defaults(function=export_products_sold_on_date(args.format, args.date)) 

    if args.subcommand == "export-sold-between":
        export_sold_between_dates.set_defaults(function=export_products_sold_between_dates(args.format, args.date1, args.date2))             

    if args.subcommand == "export-loss":
        export_loss_by_date.set_defaults(function=export_products_expired_by_date(args.format, args.date))
    
    if args.subcommand == "export-loss-between":
        export_loss_between_dates.set_defaults(function=export_products_expired_between_dates(args.format, args.date1, args.date2))

if __name__ == "__main__":
    main()
