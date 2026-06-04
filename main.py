import time
from algorithms.dp import knapsack_dp
from algorithms.greedy_by_density import greedy_by_density
from algorithms.greedy_by_value import greedy_by_value
from algorithms.greedy_by_weight import greedy_by_weight

if __name__ == "__main__":
    # Baca data dari file
    with open("./datasets/dataset7.txt", "r") as f:
        C, n = map(int, f.readline().split())
        v = list(map(int, f.readline().split()))
        w = list(map(int, f.readline().split()))

    # Eksekusi dan ukur waktu untuk setiap algoritma
    start = time.perf_counter()
    dp_result = knapsack_dp(C, n, v, w)
    dp_time = time.perf_counter() - start

    start = time.perf_counter()
    greedy_result1 = greedy_by_density(C, n, v, w)
    greedy_time = time.perf_counter() - start

    start = time.perf_counter()
    greedy_result2 = greedy_by_value(C, n, v, w)
    greedy_time = time.perf_counter() - start

    start = time.perf_counter()
    greedy_result3 = greedy_by_weight(C, n, v, w)
    greedy_time = time.perf_counter() - start

    start = time.perf_counter()
    # ga_result = knapsack_ga(C, v, w)
    # ga_time = time.perf_counter() - start

    # Tampilkan hasil dan waktu eksekusi
    print(f"Dynamic Programing  : {dp_result} ({dp_time*1000:.3f} ms)")
    print(f"Greedy by Density   : {greedy_result1} ({greedy_time*1000:.3f} ms)")
    print(f"Greedy by Value     : {greedy_result2} ({greedy_time*1000:.3f} ms)")
    print(f"Greedy by Weight    : {greedy_result3} ({greedy_time*1000:.3f} ms)")
    # print(f"GA     : {ga_result} ({ga_time*1000:.3f} ms)")