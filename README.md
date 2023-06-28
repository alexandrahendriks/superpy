# Welcome to SuperPy!

SuperPy is a command-line-tool built in Python, that is able to keep track of the storage of a supermarket. The core functionality of the program is keeping track of and producing reports on various kinds of data. The program shows which products the supermarket offers, how many of each product it has available, how much each product was bought and sold for, and what the product's expiration date is, which date it was bought and which date it was sold, and if it has expired, the date when it did. The program is able to register bought and sold items, produce reports about revenue, profit, and loss on various kinds of conditions, and last, but not least, it is also able to export selections of data into csv or excel files.

The following modules and libraries were used to build this command-line-tool:

    - CSV -- https://docs.python.org/3/library/csv.html
    - pandas -- https://pandas.pydata.org/docs/user_guide/index.html#user-guide
    - datetime -- https://docs.python.org/3/library/datetime.html
    - argparse -- https://docs.python.org/3/library/argparse.html
    - rich -- https://github.com/Textualize/rich

Start:

    Please download the following files and place them in the SAME folder on your computer! 
        - bought.py
        - date.py
        - export.py
        - loss.py
        - main.py
        - print.py
        - profit.py
        - revenue.py
        - sold.py
        - storage.py
        - date.txt
        - bought.csv

If you are missing any of these files or you don't save them to the same folder, the program won't work!  

Make sure you have the following installed on your computer:

    - Pandas: pip install pandas "or" pip3 install pandas
    - Rich: python -m pip install rich
       
Commands to interact with the program in the terminal:

    - date  -- It shows the current date
    - date-and-time -- It shows the current date and time
    - checkpoint -- It shows the date of the last time when the date file was updated
    - set-current-date -- Updates date file with the current date
    - set-date-manually -- Sets the date from manual input
    - advance-date-forwards -- Advance the date by 'x' amount of days forwards
    - advance-date-backwards -- Advance the date by 'x' amount of days backwards
    - register-bought -- Register a newly purchased product
    - register-sold -- Register a sold product
    - storage -- Shows the currently available products in the storage
    - bought -- Shows all the bought products until now
    - sold -- Shows all the sold products
    - expired -- Shows all expired products
    - product -- Shows if the specified product available for sale or not
    - amount -- Shows the amount what is available from the specified product
    - money-loss -- It shows how much money the supermarket lost from the expired items
    - money-loss-by-name -- It shows how much money the supermarket lost from the expired items by product name
    - money-loss-by-date -- It shows how much money the supermarket lost from the expired items on the given date
    - money-loss-between-dates - It shows how much money the supermarket lost from the expired items between the given dates
    - total-profit -- It shows the total profit from all the sold products
    - profit-today -- Shows the current date's profit
    - profit-by-date -- Shows the profit on a specified date
    - profit-between-dates -- Shows the profit between specified dates
    - profit-by-product -- Shows the profit of a specific product
    - total-revenue -- It shows the total revenue from all the sold products
    - revenue-today -- Shows the current date's revenue
    - revenue-by-date -- Shows the revenue on the specified date
    - revenue-between-dates -- Shows the revenue between the specified dates
    - export-storage -- Export storage until given date into csv or excel file
    - export-expired -- Export expired products until the given date into csv or excel file
    - export-sold -- Export products that were sold on given date into csv or excel file
    - export-sold-between -- Export products that were sold between given dates into csv or excel file
    - export-loss -- Export products that casue loss on the given date into csv or excel file
    - export-loss-between -- Export products that casue loss between given dates into csv or excel file


When you start to use the program, make sure you have the desired date saved in the file. You can update this directly from the date.txt file or from the commandline as well. You also have to make sure that the date is correct if you want to register a bought or sold product since the program is going to set the buy_date and sell_date from the date.txt file by default. If you skip this step, the products might be registered with the wrong information, and you will have to manually remove them from the data files.

First, you have to start the command-line-tool from the terminal and write the desired command behind it as follows: 
    
    python main.py command (-argument(s) (if present))
        or
    py main.py command (-argument(s) (if present))

Command usage with examples:
1. Date commands:
    1. date, date-and-time:

        - While the date command is going to return the current date, the date-and-time command is going to return the exact time.
        - It provides information only.
            - Example: py main.py date  --> Today's date is: 2023-06-26
            - Example: py main.py date-and-time --> Today's date and time is: 2023-06-26 20:23:27.646851

    2. checkpoint

        - To control if the right date is set in the date.txt file, use the following command.
            - Example: py main.py checkpoint --> The current date in 'date.txt' file is 2023-06-24

    3. set-current-date, set-date-manually

        - To set the current date, use the following command.
            - Example: py main.py set-current-date --> Date is set to: 2023-06-26
        - To set the date manually, you have to pass the date as an argument (-d/--date) to the function. Set the date in the format of YYYY-MM-DD!
            - Example: py main.py set-date-manually -d 2023-06-25 --> Date is set to: 2023-06-25

    4. advance-date-forwards, advance-date-backwards

        - The program is able to advance the date forward or backward based on the number of days given as an argument (-d/--date). It must be a number. You can never advance the date to a future date!
            - Example: py main.py advance-date-forwards -d 1 --> Date is set to: 2023-06-26
            - Example: py main.py advance-date-backwards -d 10 --> Date is set to: 2023-06-16

2. Register commands:    
    1. register-bought
        - To register a new product, always check first with the checkpoint command if the date is set correctly in the date.txt file; if not, adjust it.
        - The command takes in four arguments. These arguments always have to follow in this order: -pn/--productname (string) -p/--price (float) -a/--amount (integer) -ed/--expirationdate (YYY-MM-DD)
            - Example: py main.py register-bought -pn cola -p 1.99 -a 10 -ed 2024-01-01 
            - Output: You have registered as bought product: 10 cola which cost 1.99 euros each, bought on 2023-06-16 and it is going to expire on 2024-01-01.
    2. register-sold
        - To register a sold product, always check first with the checkpoint command if the date is set correctly in the date.txt file; if not, adjust it.
        - The command takes in four arguments. These arguments always have to follow in this order: -pn/--productname (string) -a/--amount (integer) -p/--price (float)  -ed/--expirationdate (YYY-MM-DD)
        - The expiration date always has to match the date given for the expiration date when the product was bought!
            - Example: py main.py register-sold -pn cola -a 10 -p 1.99 -ed 2024-01-01 
            - Output: You have registered as a sold product: 10 cola, sold for 1.99 euros each on 2023-06-16.
3. Reports:    
    1. storage, bought, sold, expired
        - These commands return a list of the currently available storage, a list of all bought and sold products, and a list of expired products.
        - Example:
            - py main.py storage
            - py main.py bought
            - py main.py sold
            - py main.py expired
    2. product & amount
        - If you want to know if a specific product is available or not, you can pass the name of the product to this command as an argument (-n/--name), and it will return all available products with that name in a table.
        - Example: py main.py product -n cola --> Returns a table
        - If you want to know exactly how many of that product are available, you can pass the product name as an argument (-n/--name) to the amount command and it will return the exact amount that is available for sale.
        - Example: py main.py amount -n cola --> You have 70 available cola for sale!
4. Revenue commands:
    1. total-revenue
        - Returns the total revenue from all sold products until the current date.
        - Example: py main.py total-revenue
        - Output: The total revenue is 209.4 euros.🤑 + a list of the products
    2. revenue-today
        - Returns the total revenue from all sold products on the current date.
        - Example: py main.py revenue-today
        - Output: 
            - The total revenue for 2023-06-26 is 109.5 euros. + a list of the products
                - or
            - There weren't any products sold! The total revenue is 0 euro.😔
    3. revenue-by-date
        - Returns the total revenue from all products sold on the given date. It takes one argument (-d/--date) in the format of YYYY-MM-DD.
        - Example: py main.py revenue-by-date -d 2023-06-21
        - Output: 
            - The total revenue for 2023-06-21 is 139.5 euros. 🤑 + a list of the products
                - or
            - There weren't any products sold! The total revenue is 0 euro.😔
    4. revenue-between-dates
    - Returns the total revenue from all sold products between the given dates.
    - It takes two arguments (-d1/--date1 -d2/--date2) in the format of YYYY-MM-DD.
        - Example: py main.py revenue-between-dates -d1 2023-05-15 -d2 2023-05-30
        - Output: 
            - The total revenue for this period of time is 159.4 euros. 🤑 + a list of the products
                - or
            - There weren't any products sold! The total revenue is 0 euro.😔
5. Profit commands:
    1. total-profit
        - Returns the total profit from all sold products until the current date.
        - Example: py main.py total-profit
        - Output: The total profit is 99.27 euros.🤑 + a list of the products
    2. profit-today
        - Returns the total profit from all sold products on the current date.
        - Example: py main.py profit-today
        - Output: 
            - The total profit today is 109.5 euros. 🤑 + a list of the products
                - or
            - There weren't any products sold! The total profit is 0 euro.😔
    3. profit-by-date
        - Returns the total profit from all sold products on the given date. It takes one argument (-d/--date) in the format of YYYY-MM-DD.
        - Example: py main.py profit-by-date -d 2023-06-21
        - Output: 
            - The total profit for 2023-06-21 is 69.07 euros. 🤑 + a list of the products
                - or
            - There weren't any products sold! The total profit is 0 euro.😔
    4. profit-between-dates
        - Returns the total profit from all sold products between the given dates.
        - It takes two arguments (-d1/--date1 -d2/--date2) in the format of YYYY-MM-DD.
        - Example: py main.py profit-between-dates -d1 2023-05-15 -d2 2023-05-30
        - Output: 
            - The total profit for this period of time is 99.27 euros. 🤑 + a list of the products
                - or
            - There weren't any products sold! The total profit is 0 euro.😔
    5. profit-by-product
        - Returns the profit from a given product.
        - It takes one argument (-n/--name)
        - Example: py main.py profit-by-product -n cola
        - Output: 
            - The total profit for cola is 10 euro.🤑 + a list of products
                - or
            - There wasn't any cola sold.

6. Loss commands:
    1. money-loss
        - Returns the total money loss from all expired products until the current date.
        - Example: py main.py money-loss
        - Output: The total loss is 222.3 euros.😒 + a list of expired products
    2. money-loss-by-date
        - Returns the total money loss from all expired products by the given date. It takes one argument (-d/--date) in the format of YYYY-MM-DD.
        - Example: py main.py money-loss-by-date -d 2023-06-25
        - Output: 
            - The total loss is 19.8 euros.😒 + a list of expired products
                - or
            - There were no products expired! There is no data available!    
    3. money-loss-between-dates
        - Returns the total money loss from all expired products between the given dates.
        - It takes two arguments (-d1/--date1 -d2/--date2) in the format of YYYY-MM-DD.
        - Example: py main.py money-loss-between-dates -d1 2023-05-15 -d2 2023-05-30
        - Output: 
            - The total loss is 173.5 euros.😒 + a list of the expired products
                - or
            - There were no products expired! There is no data available! 
    4. money-loss-by-name
        - Returns the money-loss from a given product.
        - It takes one argument (-n/--name).
        - Example: py main.py money-loss-by-name -n cola
        - Output: 
            - The total loss is 29.0 euros.😒 + a list of expired products
                - or
            - There were no products expired!
7. Export commands: 
    1. export-storage
        - It exports the currently available storage into a csv or an excel file in the given file format on the given date.
        - It takes two arguments: format(-f/--format) and date (-d/--date).
        - For the format argument, you must choose from csv or excel.
        - Date has to be set as YYYY-MM-DD.
        - Example: py main.py export-storage -f csv -d 2023-06-21 
        - Output: 
            - The storage products of 2023-06-22 has been exported as csv file. + file is created
                - or
            - There is no data available!
    2. export-expired  
        - It exports all expired products into a csv or an excel file in the given file format until the given date.
        - It takes two arguments: format(-f/--format) and date (-d/--date).
        - For the format argument you must to choose from csv or excel. 
        - Date has to be set as YYYY-MM-DD.
        - Example: py main.py export-expired -f csv -d 2023-06-21 
        - Output: 
            - The expired products of 2023-06-22 has been exported as csv file. + file is created
                - or
            - There is no data available!
    3. export-sold
        - It exports all sold products into a csv or an excel file in the given file format on the given date.
        - It takes two arguments: format(-f/--format) and date (-d/--date).
        - For the format argument you must to choose from csv or excel. 
        - Date has to be set as YYYY-MM-DD.
        - Example: py main.py export-sold -f csv -d 2023-06-21 
        - Output: 
            - The total profit is 69.07 euros.🤑 The sold products of 2023-06-21 has been exported as csv file. + file is created
                - or
            - There weren't any products sold! The total profit is 0 euro.😔 There is no data available!
    4. export-sold-between
        - It exports all sold products into a csv or an excel file in the given file format between the given dates.
        - It takes three arguments: format(-f/--format) and date (-d1/--date1) and (-d2/--date2).
        - For the format argument you must to choose from csv or excel. 
        - Date has to be set as YYYY-MM-DD
        - Example: py main.py export-sold-between -f csv -d1 2023-06-21 -d2 2023-06-26
        - Output: 
            - The total profit is 69.07 euros.🤑 The sold products between 2023-06-21 and 2023-06-26 has been exported as csv file. + file is created
                - or
            - There weren't any products sold! The total profit is 0 euro.😔 There is no data available!
    5. export-loss
        - It exports expired products into a csv or an excel file in the given file format on the given date, which causes money loss.
        - It takes two arguments: format(-f/--format) and date (-d/--date).
        - For the format argument you must to choose from csv or excel. 
        - Date has to be set as YYYY-MM-DD.
        - Example: py main.py export-loss -f csv -d 2023-06-21
        - Output: 
            - The total loss is 29.0 euros.😒 The lost products of 2023-06-21 has been exported as csv file. + file is created
                - or
            - There were no products expired! There is no data available!
    6. export-loss-between
        - It exports expired products into a csv or an excel file in the given file format between the given dates, which causes money loss.
        - It takes in three arguments: format(-f/--format) and date (-d1/--date1) and (-d2/--date2).
        - For the format argument you must to choose from csv or excel. 
        - Date has to be set as YYYY-MM-DD
        - Example: py main.py export-loss-between -f csv -d1 2023-06-21 -d2 2023-06-26
        - Output: 
            - The total loss is 48.8 euros.😒 The lost products between 2023-06-21 and 2023-06-26 has been exported as csv file. + file is created
                - or
            - There were no products expired! There is no data available!# superpy
