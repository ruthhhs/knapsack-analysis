import heapq

def greedy_by_value(C, n, merch, v, w):
    # Max-heap berdasarkan value
    heap = []

    for i in range(n):
        heapq.heappush(heap, (-v[i], i))

    total_value = 0
    total_weight = 0
    merch_dipilih = []

    while heap:
        value, idx = heapq.heappop(heap)

        if total_weight + w[idx] <= C:
            total_weight += w[idx]
            total_value += v[idx]
            merch_dipilih.append(merch[idx])

    merch_dipilih.reverse()

    if not merch_dipilih:
        print("Tidak ada merchandise yang dapat dibeli.")
        return
    
    return total_value, total_weight, merch_dipilih