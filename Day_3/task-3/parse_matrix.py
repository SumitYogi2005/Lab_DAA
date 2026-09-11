# Sparse Matrix Operations using Triple Representation


# ------------------------------------------
# 1. Convert Full Matrix into Sparse Form
# ------------------------------------------

def convert_to_sparse(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    sparse = []

    # Count non-zero elements
    non_zero = 0

    for i in range(rows):
        for j in range(cols):

            if matrix[i][j] != 0:
                non_zero += 1

    # Store matrix information
    sparse.append([rows, cols, non_zero])

    # Store non-zero elements
    for i in range(rows):
        for j in range(cols):

            if matrix[i][j] != 0:
                sparse.append([i, j, matrix[i][j]])

    return sparse


# ------------------------------------------
# 2. Reconstruct Full Matrix
# ------------------------------------------

def reconstruct_matrix(sparse):

    rows = sparse[0][0]
    cols = sparse[0][1]

    # Create zero matrix
    matrix = [[0 for j in range(cols)]
              for i in range(rows)]

    # Insert non-zero elements
    for i in range(1, len(sparse)):

        row = sparse[i][0]
        col = sparse[i][1]
        value = sparse[i][2]

        matrix[row][col] = value

    return matrix


# ------------------------------------------
# 3. Add Two Sparse Matrices
# ------------------------------------------

def add_sparse(matrix1, matrix2):

    # Check dimensions
    if (matrix1[0][0] != matrix2[0][0] or
        matrix1[0][1] != matrix2[0][1]):

        print("Matrix dimensions do not match!")
        return None

    rows = matrix1[0][0]
    cols = matrix1[0][1]

    result = []

    # Pointers to non-zero elements
    i = 1
    j = 1

    # Merge two sparse representations
    while i < len(matrix1) and j < len(matrix2):

        r1, c1, v1 = matrix1[i]
        r2, c2, v2 = matrix2[j]

        # Compare positions
        if (r1, c1) < (r2, c2):

            result.append([r1, c1, v1])
            i += 1

        elif (r1, c1) > (r2, c2):

            result.append([r2, c2, v2])
            j += 1

        else:

            # Add values at same position
            total = v1 + v2

            # Store only non-zero results
            if total != 0:
                result.append([r1, c1, total])

            i += 1
            j += 1

    # Add remaining elements of first matrix
    while i < len(matrix1):

        result.append(matrix1[i])
        i += 1

    # Add remaining elements of second matrix
    while j < len(matrix2):

        result.append(matrix2[j])
        j += 1

    # Add header information
    result.insert(0, [rows, cols, len(result)])

    return result


# ------------------------------------------
# 4. Display Sparse Matrix
# ------------------------------------------

def display_sparse(sparse):

    print("\nRow\tColumn\tValue")
    print("-" * 30)

    for row in sparse:
        print(row[0], "\t", row[1], "\t", row[2])


# ------------------------------------------
# 5. Display Full Matrix
# ------------------------------------------

def display_matrix(matrix):

    for row in matrix:
        print(" ".join(map(str, row)))


# ------------------------------------------
# 6. Main Program
# ------------------------------------------

def main():

    matrix1 = [
        [0, 0, 3, 0],
        [0, 0, 0, 0],
        [5, 0, 0, 8],
        [0, 2, 0, 0]
    ]

    matrix2 = [
        [0, 4, 0, 0],
        [0, 0, 0, 6],
        [0, 0, 7, 0],
        [0, 3, 0, 0]
    ]

    print("========== MATRIX 1 ==========")

    print("\nOriginal Matrix:")
    display_matrix(matrix1)

    sparse1 = convert_to_sparse(matrix1)

    print("\nSparse Representation:")
    display_sparse(sparse1)

    print("\nReconstructed Matrix:")
    display_matrix(reconstruct_matrix(sparse1))

    print("\n========== MATRIX 2 ==========")

    print("\nOriginal Matrix:")
    display_matrix(matrix2)

    sparse2 = convert_to_sparse(matrix2)

    print("\nSparse Representation:")
    display_sparse(sparse2)

    print("\nReconstructed Matrix:")
    display_matrix(reconstruct_matrix(sparse2))

    # Add sparse matrices directly
    print("\n========== SPARSE MATRIX ADDITION ==========")

    result = add_sparse(sparse1, sparse2)

    if result is not None:

        print("\nResult in Sparse Representation:")
        display_sparse(result)

        print("\nReconstructed Result Matrix:")
        display_matrix(reconstruct_matrix(result))


# ------------------------------------------
# 7. Execute Program
# ------------------------------------------

if __name__ == "__main__":
    main()