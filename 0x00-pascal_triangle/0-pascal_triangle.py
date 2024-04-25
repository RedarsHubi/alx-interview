#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    lista = []

    # Generate Pascal's Triangle
    for i in range(n):
        row = [1]  # Start each row with 1
        for j in range(1, i):  # Generate elements in between 1 and 1
            row.append(lista[i - 1][j - 1] + lista[i - 1][j])
        if i > 0:  # Skip for the first row
            row.append(1)  # End each row with 1
        lista.append(row)

    # Modify odd rows after the third row
    for i in range(3, n):
        if i % 2 == 1:
            mid = len(lista[i]) // 2
            lista[i][mid] = lista[i - 1][mid - 1] + lista[i - 1][mid]

    return (lista)
