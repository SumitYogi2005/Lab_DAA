# 2D Array Operations using Python List of Lists


# ------------------------------------------
# 1. Display 2D Array
# ------------------------------------------

def display_array(arr):

    print("\nCurrent 2D Array:")

    for row in arr:
        print(row)


# ------------------------------------------
# 2. Insert a New Row
# ------------------------------------------

def insert_row(arr, position, new_row):

    if position < 0 or position > len(arr):
        print("Invalid position!")
        return

    arr.insert(position, new_row)

    print("\nRow inserted successfully!")
    display_array(arr)


# ------------------------------------------
# 3. Delete a Row
# ------------------------------------------

def delete_row(arr, position):

    if position < 0 or position >= len(arr):
        print("Invalid position!")
        return

    deleted = arr.pop(position)

    print("\nDeleted Row:", deleted)
    display_array(arr)


# ------------------------------------------
# 4. Search for an Element
# ------------------------------------------

def search_element(arr, target):

    found = False

    for i in range(len(arr)):

        for j in range(len(arr[i])):

            if arr[i][j] == target:

                print("\nElement Found!")
                print("Row:", i)
                print("Column:", j)

                found = True

    if not found:
        print("\nElement Not Found!")

    return found


# ------------------------------------------
# 5. Rotate 2D Array 90 Degrees Clockwise
# ------------------------------------------

def rotate_clockwise(arr):

    if not arr:
        print("\nArray is empty!")
        return

    # Check that the matrix is rectangular
    if any(len(row) != len(arr[0]) for row in arr):
        print("\nRotation requires a rectangular array!")
        return

    rows = len(arr)
    cols = len(arr[0])

    # Create a new matrix with swapped dimensions
    rotated = []

    for j in range(cols):

        new_row = []

        for i in range(rows - 1, -1, -1):

            new_row.append(arr[i][j])

        rotated.append(new_row)

    # Update original array
    arr[:] = rotated

    print("\nArray rotated 90 degrees clockwise!")
    display_array(arr)


# ------------------------------------------
# 6. Main Program
# ------------------------------------------

def main():

    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    while True:

        print("\n========== 2D ARRAY OPERATIONS ==========")

        display_array(arr)

        print("\n1. Insert a New Row")
        print("2. Delete a Row")
        print("3. Search for an Element")
        print("4. Rotate 90 Degrees Clockwise")
        print("5. Display Array")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        # Insert Row
        if choice == "1":

            try:
                position = int(input("Enter row position: "))

                if position < 0 or position > len(arr):
                    print("Invalid position!")
                    continue

                values = input(
                    "Enter row elements separated by spaces: "
                )

                new_row = list(map(int, values.split()))

                if arr and len(new_row) != len(arr[0]):
                    print("New row must have the same number of columns!")
                    continue

                insert_row(arr, position, new_row)

            except ValueError:
                print("Please enter valid integers!")

        # Delete Row
        elif choice == "2":

            try:
                position = int(input("Enter row position to delete: "))

                delete_row(arr, position)

            except ValueError:
                print("Please enter a valid position!")

        # Search Element
        elif choice == "3":

            try:
                target = int(input("Enter value to search: "))

                search_element(arr, target)

            except ValueError:
                print("Please enter a valid integer!")

        # Rotate Array
        elif choice == "4":

            rotate_clockwise(arr)

        # Display Array
        elif choice == "5":

            display_array(arr)

        # Exit
        elif choice == "6":

            print("\nProgram terminated successfully!")
            break

        else:

            print("\nInvalid choice! Please try again.")


# ------------------------------------------
# 7. Execute Program
# ------------------------------------------

if __name__ == "__main__":
    main()