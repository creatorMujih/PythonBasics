def printTable(table):
    colWidths = [0] * len(tableData)

    for row in table:
        for i in range(len(row)):
            colWidths[i] = max(colWidths[i], len(row[i]))
    for row in table:
        for i in range(len(row)):
            print(row[i].rjust(colWidths[i]), end=' ')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)