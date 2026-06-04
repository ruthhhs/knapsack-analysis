import heapq

def greedy_by_density(C, n, v, w):
    # Max-heap berdasarkan density
    heap = []

    for i in range(n):
        density = v[i] / w[i]
        heapq.heappush(heap, (-density, i))

    total_value = 0
    total_weight = 0
    selected = []

    while heap:
        density, idx = heapq.heappop(heap)

        if total_weight + w[idx] <= C:
            total_weight += w[idx]
            total_value += v[idx]
            selected.append(idx)

    if not selected:
        return -1, -1

    return total_value, total_weight