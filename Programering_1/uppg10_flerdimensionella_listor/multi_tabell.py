

def multiplication_table(size):
    table = []

    for i in range(int(size)):
        table.append([])
        for j in range(int(size)):
            table[i].append((i + 1)*(j + 1))
    return table

def print_table(table):
    for row in table:
        for value in row:
            print(value, end=" ")
        print()

size = input("Vilken gånger tabbel vill du ha: ")
table = multiplication_table(size)
print_table(table)
