# Matrix Operations using Python


# ------------------------------------------
# 1. Input Matrix
# ------------------------------------------

def input_matrix():

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    if rows <= 0 or cols <= 0:
        raise ValueError("Dimensions must be positive!")

    matrix = []

    print("Enter matrix elements row by row:")

    for i in range(rows):

        row = list(map(int, input(
            f"Enter elements of row {i + 1}: "
        ).split()))

        if len(row) != cols:
            raise ValueError(
                f"Please enter exactly {cols} elements!"
            )

        matrix.append(row)

    return matrix


# ------------------------------------------
# 2. Display Matrix
# ------------------------------------------

def display_matrix(matrix):

    print("\nMatrix:")

    for row in matrix:
        print(" ".join(map(str, row)))


# ------------------------------------------
# 3. Matrix Addition
# ------------------------------------------

def add_matrices(A, B):

    rows_A = len(A)
    cols_A = len(A[0])

    rows_B = len(B)
    cols_B = len(B[0])

    if rows_A != rows_B or cols_A != cols_B:

        print("\nAddition not possible!")
        print("Both matrices must have the same dimensions.")

        return None

    result = []

    for i in range(rows_A):

        row = []

        for j in range(cols_A):

            row.append(A[i][j] + B[i][j])

        result.append(row)

    return result


# ------------------------------------------
# 4. Matrix Multiplication
# ------------------------------------------

def multiply_matrices(A, B):

    rows_A = len(A)
    cols_A = len(A[0])

    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:

        print("\nMultiplication not possible!")
        print("Columns of first matrix must equal rows of second matrix.")

        return None

    result = []

    for i in range(rows_A):

        row = []

        for j in range(cols_B):

            total = 0

            for k in range(cols_A):

                total += A[i][k] * B[k][j]

            row.append(total)

        result.append(row)

    return result


# ------------------------------------------
# 5. Matrix Transpose
# ------------------------------------------

def transpose_matrix(A):

    rows = len(A)
    cols = len(A[0])

    result = []

    for j in range(cols):

        row = []

        for i in range(rows):

            row.append(A[i][j])

        result.append(row)

    return result


# ------------------------------------------
# 6. Determinant of 2x2 Matrix
# ------------------------------------------

def determinant_2x2(A):

    return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])


# ------------------------------------------
# 7. Determinant of 3x3 Matrix
# ------------------------------------------

def determinant_3x3(A):

    a = A[0][0]
    b = A[0][1]
    c = A[0][2]

    d = A[1][0]
    e = A[1][1]
    f = A[1][2]

    g = A[2][0]
    h = A[2][1]
    i = A[2][2]

    det = (
        a * (e * i - f * h)
        - b * (d * i - f * g)
        + c * (d * h - e * g)
    )

    return det


# ------------------------------------------
# 8. Calculate Determinant
# ------------------------------------------

def find_determinant(A):

    rows = len(A)
    cols = len(A[0])

    if rows != cols:

        print("\nDeterminant cannot be calculated!")
        print("Matrix must be square.")

        return None

    if rows == 2:

        return determinant_2x2(A)

    elif rows == 3:

        return determinant_3x3(A)

    else:

        print("\nOnly 2x2 and 3x3 matrices are supported!")

        return None


# ------------------------------------------
# 9. Main Menu
# ------------------------------------------

def main():

    while True:

        print("\n========== MATRIX OPERATIONS ==========")

        print("1. Add Two Matrices")
        print("2. Multiply Two Matrices")
        print("3. Transpose a Matrix")
        print("4. Find Determinant")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        try:

            # Matrix Addition
            if choice == "1":

                print("\nEnter First Matrix:")
                A = input_matrix()

                print("\nEnter Second Matrix:")
                B = input_matrix()

                result = add_matrices(A, B)

                if result is not None:
                    print("\nResult of Matrix Addition:")
                    display_matrix(result)

            # Matrix Multiplication
            elif choice == "2":

                print("\nEnter First Matrix:")
                A = input_matrix()

                print("\nEnter Second Matrix:")
                B = input_matrix()

                result = multiply_matrices(A, B)

                if result is not None:
                    print("\nResult of Matrix Multiplication:")
                    display_matrix(result)

            # Matrix Transpose
            elif choice == "3":

                print("\nEnter Matrix:")
                A = input_matrix()

                result = transpose_matrix(A)

                print("\nTranspose of Matrix:")
                display_matrix(result)

            # Determinant
            elif choice == "4":

                print("\nEnter Matrix:")
                A = input_matrix()

                result = find_determinant(A)

                if result is not None:
                    print("\nDeterminant =", result)

            # Exit
            elif choice == "5":

                print("\nProgram terminated successfully!")
                break

            else:

                print("\nInvalid choice! Please try again.")

        except ValueError as error:

            print("\nInput Error:", error)

        except Exception as error:

            print("\nError:", error)


# ------------------------------------------
# 10. Execute Program
# ------------------------------------------

if __name__ == "__main__":
    main()