I = 32767  # Infinity
V = 7  # Number of vertices in Graph
E = 9  # Number of edges in Graph


def print_mcst(T, A):
    print("\nMinimum Cost Spanning Tree Edges\n")
    for i in range(V - 1):
        print(f"[{T[0][i]}]-----[{T[1][i]}]")
    print()


# Set operations: Union and Find
def union(u, v, s):
    if s[u] < s[v]:
        s[u] += s[v]
        s[v] = u
    else:
        s[v] += s[u]
        s[u] = v


def find(u, s):
    x = u
    v = 0

    while s[x] > 0:
        x = s[x]

    while u != x:
        v = s[u]
        s[u] = x
        u = v
    return x


def kruskals_mcst(A):
    T = [[0] * (V - 1) for _ in range(2)]  # Solution array
    track = [0] * E  # Track edges that are included in the solution
    s = [-1] * (V + 1)  # Array for finding cycles

    i = 0
    while i < V - 1:
        min_val = I
        u = v = k = 0

        # Find a minimum cost edge
        for j in range(E):
            if track[j] == 0 and A[2][j] < min_val:
                min_val = A[2][j]
                u = A[0][j]
                v = A[1][j]
                k = j

        # Check if the selected min cost edge (u, v) forms a cycle or not
        if find(u, s) != find(v, s):
            T[0][i] = u
            T[1][i] = v

            # Perform union
            union(find(u, s), find(v, s), s)
            i += 1

        track[k] = 1

    print_mcst(T, A)


def main():
    edges = [
        [1, 1, 2, 2, 3, 4, 4, 5, 5],
        [2, 6, 3, 7, 4, 5, 7, 6, 7],
        [25, 5, 12, 10, 8, 16, 14, 20, 18]
    ]

    kruskals_mcst(edges)


if __name__ == "__main__":
    main()
