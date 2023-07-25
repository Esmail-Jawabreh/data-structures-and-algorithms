def adjacency_matrix_to_list(nodes, matrix):
    adjacency_list = {}

    for i, node in enumerate(nodes):
        neighbors = [nodes[j] for j in range(len(matrix[i])) if matrix[i][j]]
        adjacency_list[node] = neighbors

    return adjacency_list
