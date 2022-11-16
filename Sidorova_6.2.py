def get_determinant(matrix):
    result = 0
    if len(matrix) == 2:
        result = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    else:
        for row in range(0, len(matrix)):
            result += (-1) ** row * matrix[row][0] * get_determinant(minor(matrix, row))
    return result


def minor(matrix, delete_row):
    minor_arr = [[0] * (len(matrix) - 1) for i in range((len(matrix) - 1))]
    deleted_row_count = deleted_col_count = 0
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix)):
            if col == 0:
                deleted_col_count = 1
                continue
            if row == delete_row:
                deleted_row_count = 1
                continue
            minor_arr[row - deleted_row_count][col - deleted_col_count] = matrix[row][col]
    return minor_arr


fileInput = open('input.txt')
arr = []
for line in fileInput:
    arr.append(line.strip().split(' '))

for line in arr:
    if len(arr) != len(line):
        print("\nМатрица должна быть квадратной")
        exit(1)
int_arr = []
for k in range(0, len(arr)):
    int_arr.append(list(map(int, arr[k])))

det = get_determinant(int_arr)

fileOutput = open('output.txt', 'w')
fileOutput.write("%s\n" % det)
fileOutput.close()

fileInput.close()
