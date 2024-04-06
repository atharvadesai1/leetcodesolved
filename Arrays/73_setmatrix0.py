matrix  = [[1,1,1],[1,0,1],[1,1,1]]

tuple_mat = []
for elements in matrix:
    tuple_mat.append(tuple(elements))
tuple_mat  = tuple(tuple_mat)
new_matrix = matrix

for i in range(len(tuple_mat)):
    for j in range(len(tuple_mat[i])):
        if tuple_mat[i][j] == 0:
            for t in range(len(tuple_mat)):
                new_matrix[t][j] = 0
            for s in range(len(tuple_mat[i])):
                new_matrix[i][s] = 0

print(new_matrix)