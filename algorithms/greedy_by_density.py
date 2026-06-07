import heapq

def greedy_by_density(C, n, merch, v, w):
    # Max-heap berdasarkan density
    heap = []

    for i in range(n):
        density = v[i] / w[i]
        heapq.heappush(heap, (-density, i))

    total_value = 0
    total_weight = 0
    merch_dipilih = []

    while heap:
        density, idx = heapq.heappop(heap)

        if total_weight + w[idx] <= C:
            total_weight += w[idx]
            total_value += v[idx]
            merch_dipilih.append(merch[idx])

    merch_dipilih.reverse()

    if not merch_dipilih:
        print("Tidak ada merchandise yang dapat dibeli.")
        return
    
    return total_value, total_weight, merch_dipilih