def check_cycle(graph, vertex, visited, parent):
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            if check_cycle(graph, neighbor, visited, vertex):
                return True
        elif parent != neighbor:
            return True
    return False

def main():
    graph = []

    with open("input.txt", "r") as f:
        for i, line in enumerate(f):
            vertices = list(map(int, line.split()))
            graph.append([])
            for vertex in vertices[1:]:
                graph[i].append(vertex - 1)

    n = len(graph)

    visited = [False] * n

    check_cycle_result = False
    for i in range(n):
        if not visited[i]:
            if check_cycle(graph, i, visited, -1):
                check_cycle_result = True
                break

    with open("output.txt", "w") as f:
        f.write(str(check_cycle_result))

if __name__ == "__main__":
    main()