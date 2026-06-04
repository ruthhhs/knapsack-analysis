import heapq

def greedy_by_weight(C, n, v, w):
    # Min-heap berdasarkan weight
    heap = []

    for i in range(n):
        heapq.heappush(heap, (w[i], i))

    total_value = 0
    total_weight = 0
    selected = []

    while heap:
        weight, idx = heapq.heappop(heap)

        if total_weight + w[idx] <= C:
            total_weight += w[idx]
            total_value += v[idx]
            selected.append(idx)

    if not selected:
        return -1, -1

    return total_value, total_weight