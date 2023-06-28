from datetime import date, datetime
from rich import print as rprint
# Exact date and time
date_and_time = datetime.now()
import datetime # This import had to be under the date_and_time variable otherwhile "datetime.now()" wouldn't work.

# Today's date
today = date.today()

# Date in date.txt
date_in_file = "date.txt"

# Returns the date of the last time the date.txt was updated
def show_checkpoint():
    with open(date_in_file, "r") as f:
        for line in f:
            rprint(f"[green]The current date in 'date.txt' file is {line}.")
                            
# Sets current date and writes in a txt file and prints it out to the console -- "date.txt"
def set_date():
    with open(date_in_file, "w") as f:
        f.write(today.strftime("%Y-%m-%d"))
    with open(date_in_file, "r") as f:    
        for line in f:
            rprint(f"[green]Date is set to: {line}")

# Sets date from input into date.txt (update)
def set_date_manually(date):
    with open(date_in_file, "w") as f:
        f.write(date.strftime("%Y-%m-%d"))
    with open(date_in_file, "r") as f:    
        for line in f:
            rprint(f"[green]Date is set to: {line}")

# Get currently set date in date.txt file
def get_date():
    with open(date_in_file, "r") as f:
        for line in f:
            return line

# Advance the date forwards with amount of days given, but can't set the date further than current date
def advanced_date_forward(day):
    current_date = datetime.datetime.strptime(get_date(), "%Y-%m-%d").date()
    advance_date = current_date + datetime.timedelta(day)
    if advance_date > today:
        rprint("[red]Error! You can't set the date further than the current date!")
    else:    
        with open(date_in_file, "w") as f:
            f.write(advance_date.strftime("%Y-%m-%d"))
        rprint(f"[green]Date is set to: {advance_date}")  

# Advance the date backwards with amount of days given
def advanced_date_backwards(day):
    current_date = datetime.datetime.strptime(get_date(), "%Y-%m-%d").date()
    advance_date = current_date - datetime.timedelta(day)
    with open(date_in_file, "w") as f:
        f.write(advance_date.strftime("%Y-%m-%d"))
    rprint(f"[green]Date is set to: {advance_date}")
