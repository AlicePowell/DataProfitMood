
def sales_barchart():
    import csv
    import turtle

    turtle.colormode(255)
    turtle.speed(10)

    def star(star_width, star_color):
        for points in range(5):
            turtle.color(star_color)
            turtle.forward(star_width)
            turtle.right(144)
        turtle.right(180)
        turtle.forward(1)
        turtle.color('white')


    turtle.color('white')
    turtle.left(180)
    turtle.forward(240)
    turtle.right(180)

    months = []
    sales_figures = 0
    turtle_blue = 0

    # open and read spreadsheet
    with open('sales.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        for row in spreadsheet:
            month_sales = row['sales']
            # convert sales figure into a float length that fits in turtle window
            sales_figures = float(month_sales)/49

            # convert sales figure into an integer between 0 and 255
            turtle_blue = 255 - int(sales_figures // 0.6)
            turtle_other = int(turtle_blue / 2)

            # set turtle color and fill for the month
            turtle.pencolor(60, 60, turtle_blue)
            turtle.fillcolor(turtle_other, turtle_other, turtle_blue)

            # draw graph for the month
            turtle.begin_fill()
            turtle.forward(40)
            turtle.left(90)
            turtle.forward(sales_figures)
            turtle.left(90)
            turtle.forward(40)
            turtle.left(90)
            turtle.forward(sales_figures)
            turtle.left(90)
            turtle.forward(40)
            turtle.end_fill()

    # add dotted line for scale
    turtle.penup()
    turtle.left(90)
    turtle.forward(8000 // 49)
    turtle.left(90)
    turtle.color('gold')
    for count1 in range(60):
        turtle.pendown()
        turtle.forward(4)
        turtle.penup()
        turtle.forward(4)
    turtle.left(180)
    turtle.forward(483)
    turtle.write("£8000", move=False, font=("Verdana", 12, "normal"))
    turtle.right(90)
    turtle.forward(14)
    turtle.left(90)
    turtle.write("sales", move=False, font=("Verdana", 12, "normal"))
    turtle.right(180)
    turtle.forward(3)
    turtle.left(90)
    turtle.forward((8000 // 49) - 11)
    turtle.left(90)



    # Position for labels
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(480)
    turtle.right(180)
    turtle.forward(13)

    # Add text labels
    turtle.color('black')

    with open('sales.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        for row in spreadsheet:
            actual_month = row['month']
            actual_month = actual_month.capitalize()
            turtle.write(actual_month, move=False, font=("Verdana", 12, "normal"))
            turtle.forward(40)

    # title
    turtle.right(180)
    turtle.forward(480)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.color("gold")
    turtle.write("2018 Sales Figures Per Month ", move=False, font=("Verdana", 12, "normal"))
    turtle.forward(480)

    # Position for stars
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.pendown()

    # add stars
    star(25, (253, 184, 19))

    turtle.left(90)
    turtle.forward(520)
    turtle.right(90)
    turtle.forward(120)

    star(20, (253, 184, 19))
    turtle.forward(40)
    turtle.done()

