from collections import deque
def bfs(a, b, c):
    queue = deque([(0, 0, [])])
    visited = set()
    while queue:
        x, y, steps = queue.popleft()
        if x == c or y == c:
            return steps
        operations = [(a, y, 'FILL(1)'),(x, b, 'FILL(2)'),(0, y, 'DROP(1)'),(x, 0, 'DROP(2)'),
                      (max(0, x - (b - y)), min(b, y + x), 'POUR(1,2)'),
                      (min(a, x + y), max(0, y - (a - x)), 'POUR(2,1)')]
        for nx, ny, op in operations:
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + [op]))
    return None

A, B, C = map(int, input().strip().split())
result = bfs(A, B, C)
if result is None:
    print("impossible")
else:
    print(len(result))
    for step in result:
        print(step)