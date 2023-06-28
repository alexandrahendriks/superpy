# Report

This is my short report on the SuperPy project, which is a command-line-tool, which is able to keep track of the storage of a supermarket. The core functionality of the program is about keeping track of and producing reports on various kinds of data.

In my project I have used multiple modules, some were a must to use and some I have chosen myself.

Modules that I have used:

## CSV:

- The CSV modules I have used only to reading data from the existing CSV files and return the lines from the file with it.

## datetime:

- I have used this module in multiple ways in my project. I have used the date and datetime objects. From the functions I have used today and now to return the exact date and time I also made use of strptime in the argument parsers and strftime in multiple places where I had to work with the date. I also made use of timedelta in the function where you can advance the days with the number of numbers given as an argument.

## argparse:

- Since this module was new, I had to do a bit of research, but honestly, it looks more complicated than I thought. Once I got the hang of it it was quiet easy to work, and build the whole command-line-tool with it.

## pandas:

- I worked a lot with pandas. First I was trying CSV to deal with data, but anywhere I have looked on the internet, everyone is recommending pandas, so I have looked into it myself. I find it quite a powerful tool to use when you are working with data. In my opinion, it is way easier to work with it than with CSV, and I also like it more. Since it is really simple to use and it also needs less coding, I'm probably going to make a lot of use of it in the future as well. You'll find me using pandas throughout my whole code for the exact same reason. Honestly, if CSV hadn't a must to use, I might have used only this module to work with the data.

## rich:

- Finally, I have made use of rich to bring some colour to my project. I implemented it in every print statement and also in the dataframes to make them look prettier and easier to read and understand.


##  As it was listed and asked for in the project description, I have made multiple functionalities for this program

- The program is able to register bought and sold products. As soon as any of these files are updated, it also updates the storage file so we can keep track of the currently available products.
- Produces reports about revenue and profit under various conditions and prints them to the terminal.
- One feature that I thought of myself is that it can also keep track of expired products, and if they do expire, it removes them from the storage. You can also export this data under various conditions.
- The program is also able to calculate how much money the supermarket lost due to these expired products.
- Last, but not least, it is also able to export selections of data into csv or excel files.


Every functionality I have tried to separate into its own file, so all the functions that are kind of in the same category are found in the same file. I also have a functions_and_variables.py file where I placed variables in which I stored the strings for the print statements in my program, well as some other functions that are being used on multiple files in my project.