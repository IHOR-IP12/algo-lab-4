# graph - список суміжності графа
# vertex - поточна вершина
# parent - тато vertexy
#stack чи є в активному пошуку під час пошуку циклу

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
    with open("input.txt", "r") as f:
        n = len(f.readlines())
        f.seek(0)  

        graph = [[] for _ in range(n)]

        for i, line in enumerate(f):
            vertices = list(map(int, line.split()))
            for vertex in vertices[1:]:
                graph[i].append(vertex - 1)

    visited = [False] * n

    has_cycle_result = False
    for i in range(n):
        if not visited[i]:
            if check_cycle(graph, i, visited, -1):
                has_cycle_result = True
                break

    with open("output.txt", "w") as f:
        f.write(str(has_cycle_result))

if __name__ == "__main__":
    main()





#без циклу
#1
#2
#3
#4
#5
#6
#7
#8
#9
#10
#11
#12