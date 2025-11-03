
def read_matrix(rows, cols, name):
    print(f"\nEnter elements of {name} matrix ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"{name}[{i}][{j}]: "))
            row.append(val)
        matrix.append(row)
    return matrix


def multiply_matrices(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)
    return result


print("Matrix Multiplication Program")


r1 = int(input("Enter rows for Matrix A: "))
c1 = int(input("Enter columns for Matrix A: "))
r2 = int(input("Enter rows for Matrix B: "))
c2 = int(input("Enter columns for Matrix B: "))

if c1 != r2:
    print("It Cannot multiply.")
else:
    A = read_matrix(r1, c1, "A")
    B = read_matrix(r2, c2, "B")
    result = multiply_matrices(A, B)

    print("\n Resultant Matrix (A * B):")
    for row in result:
        print(row)