with open("txt.csv") as csv_file:
    tabla = csv_file.read().splitlines()
    print(tabla)

    for row in tabla:
        row_data = row.split(",")
        print(f"{row_data[0]} is {row_data[1]} years old and {row_data[2]}")
