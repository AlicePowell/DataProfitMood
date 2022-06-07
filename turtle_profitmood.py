def profitmood():
    import csv
    import turtle
    colour_list = []
    month_list = []
    square_unit = 140

    def draw_square():
        turtle.begin_fill()
        for count in range(5):
            turtle.forward(square_unit)
            turtle.right(90)
        turtle.end_fill()
        turtle.left(90)

    def position_turtle():
        turtle.penup()
        turtle.right(90)
        turtle.forward(square_unit)
        turtle.right(90)
        turtle.forward(3 * square_unit)
        turtle.left(180)
        turtle.pendown()

    def set_colour():
        blue = 255 - item
        shade = (2 * blue) // 3
        red = int(item)
        if red < 94:
            red = red * 3
            turtle.color(255, red, red)
            turtle.fillcolor(240, red, red)
        else:
            blue = blue + 50
            turtle.color(shade, shade, blue)
            turtle.fillcolor(shade, shade, blue)

    def write_month():
        turtle.penup()
        turtle.color(255, 102, 0)
        turtle.write(months, move=False, font=("Verdana", 40, "normal"))
        turtle.forward(square_unit)

    with open('sales2.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        for row in spreadsheet:
            profit_value = int(row['profit'])
            value_add = int(profit_value + 2180)
            colour_value = (value_add // 32)
            colour_list.append(colour_value)
            actual_month = row['month']
            month_list.append(actual_month)

    turtle.colormode(255)
    turtle.speed(10)
    turtle.penup()

    # start position turtle
    turtle.left(180)
    turtle.forward(1.5 * square_unit)
    turtle.right(90)
    turtle.forward(2 * square_unit)
    turtle.right(90)
    turtle.pendown()

    for item in colour_list[0:3]:
        set_colour()
        draw_square()

    position_turtle()

    for item in colour_list[3:6]:
        set_colour()
        draw_square()

    position_turtle()

    for item in colour_list[6:9]:
        set_colour()
        draw_square()

    position_turtle()

    for item in colour_list[9:]:
        set_colour()
        draw_square()

    position_turtle()
    turtle.penup()
    turtle.left(90)
    turtle.forward(3.35 * square_unit)
    turtle.right(90)
    turtle.forward(39)

    for months in month_list[0:3]:
        write_month()
    position_turtle()

    for months in month_list[3:6]:
        write_month()
    position_turtle()

    for months in month_list[6:9]:
        write_month()
    position_turtle()

    for months in month_list[9:]:
        write_month()
    position_turtle()

    turtle.penup()
    turtle.left(180)
    turtle.forward(127)
    turtle.right(90)
    turtle.forward(square_unit + 30)
    turtle.color(34, 34, 51)
    turtle.write("profit", move=False, font=("Verdana", 22, "normal"))
    turtle.right(180)
    turtle.forward(23)
    turtle.left(180)
    turtle.color(200, 200, 255)
    turtle.write("even", move=False, font=("Verdana", 22, "normal"))
    turtle.right(180)
    turtle.forward(24)
    turtle.left(180)
    turtle.color(240, 42, 42)
    turtle.write("loss", move=False, font=("Verdana", 22, "normal"))
    turtle.color('white')
    turtle.penup()

    turtle.done()

