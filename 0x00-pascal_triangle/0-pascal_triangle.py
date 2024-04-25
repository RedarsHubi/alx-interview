def pascal_triangle(n):
    list_of_lists = []

    # Generate Pascal's Triangle
    for i in range(n):
        row = [1]  # Start each row with 1
        for j in range(1, i):  # Generate elements in between 1 and 1
            row.append(list_of_lists[i - 1][j - 1] + list_of_lists[i - 1][j])
        if i > 0:  # Skip for the first row
            row.append(1)  # End each row with 1
        list_of_lists.append(row)

    # Modify odd rows after the third row
    for i in range(3, n):
        if i % 2 == 1:
            mid_index = len(list_of_lists[i]) // 2
            list_of_lists[i][mid_index] = list_of_lists[i - 1][mid_index - 1] + list_of_lists[i - 1][mid_index]

    return(list_of_lists)
