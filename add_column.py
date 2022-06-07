import csv

profit_calc = 0
my_dict = {"year": "2018", "month": [], "sales": [], "expenditure": [], "profit": []}
field_names = ["year", "month", "sales", "expenditure", "profit"]
whole_data = []


# open and read spreadsheet
with open('sales.csv', 'r') as csv_file:
    spreadsheet1 = csv.DictReader(csv_file)
    for row in spreadsheet1:
        sales_year = row['year']
        months = row['month']
        month_sales = row['sales']
        month_expenditure = row['expenditure']
        profit_calc = (int(month_sales) - int(month_expenditure))
        my_dict["month"] = months
        my_dict["sales"] = month_sales
        my_dict["expenditure"] = month_expenditure
        my_dict["profit"] = profit_calc
        whole_data.append(my_dict)
        print(whole_data)
        my_dict = {"year": "2018", "month": [], "sales": [], "expenditure": [], "profit": []}


with open('sales2.csv', 'w+') as csv_file:
    spreadsheet2 = csv.DictWriter(csv_file, fieldnames=field_names)
    spreadsheet2.writeheader()
    spreadsheet2.writerows(whole_data)

