import csv
from turtle_barchart import *
from turtle_profitmood import *

# define the variables
months = []
total_sale = 0
total_sale2 = 0
allSales = []
tupleMonthSale = ()
total_expenditure = 0

# open and read spreadsheet
with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    print("\n")

    # extract the sales for each month and create a list in the variable months
    for row in spreadsheet:
        actual_month = row['month']
        actual_month = actual_month.capitalize()
        month_sales = row['sales']
        months.append(actual_month)
        months.append(month_sales)
        total_expenditure += int(row['expenditure'])
        allSales += [int(month_sales)]
        total_sale2 += int(month_sales)
        tupleMonthSale += ((int(month_sales), actual_month),)

        # turn month_sales into a float and keep adding sales for each months in the variable total_sales
        sales_float = int(month_sales)
        total_sale = total_sale + sales_float

        # print each months sales figure throughout the iteration
        print("In {} 2018 the company made £{} in Sales".format(actual_month, month_sales))

avarage = total_sale2/len(allSales)
avarage = round(avarage, 2)
print("\nThe sales (£) from each month in a single list are:{}".format(months))
print("\nA list of sales for each month (Jan - Dec) is: {}".format(allSales))
print("The highest sales figure (£) by month was: {}".format(max(tupleMonthSale)))
print("The total sales across all months in 2018 was £ {} ".format(total_sale2))
print("The 2018 average sales per month was £ {} \n".format(avarage))

# let assume we hav a sales_sum.txt file in the same directory as this file
with open('sales_sum.txt', 'w') as txt_file:
    txt_file.write("Total sale:")
    txt_file.write(str(total_sale))
with open('summary.csv', 'w') as csv_file:
    csv_file.write(f"Year, total_sales, total_expenditure, avarage\n")
    csv_file.write(f"2018, {total_sale}, {total_expenditure}, {avarage}")


# Add turtle drawings
wakeup_turtle = input("Would you like to see a drawing of the 2018 monthly figures, yes or no?  \n")
wakeup_turtle = wakeup_turtle.capitalize()
if wakeup_turtle == "Yes":
    tasks = input("Choose between Sales or Profit?  \n")
    tasks = tasks.capitalize()
    if tasks == "Sales":
        sales_barchart()
    elif tasks == "Profit":
        profitmood()
    else:
        print("Thank you, goodbye")
else:
    print("OK... well... goodbye")

