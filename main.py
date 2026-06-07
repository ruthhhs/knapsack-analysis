import time
from algorithms.dp import knapsack_dp
from algorithms.greedy_by_density import greedy_by_density
from algorithms.greedy_by_value import greedy_by_value
from algorithms.greedy_by_weight import greedy_by_weight
from algorithms.ga import knapsack_ga

if __name__ == "__main__":
    # Baca data dari file
    with open("./datasets/dataset1.txt", "r") as f:     # ubah dataset di sini
        C, n = map(int, f.readline().split())
        merch = f.readline().split("|")
        v = list(map(int, f.readline().split()))
        w = list(map(int, f.readline().split()))

    # Eksekusi dan ukur waktu untuk setiap algoritma
    start = time.perf_counter()
    dp_v, dp_w, merch_dipilih = knapsack_dp(C, n, merch, v, w)
    dp_time = time.perf_counter() - start
    print("\n=== Hasil Dynamic Programming ===")
    print("kepuasan \t| Anggaran \t| Waktu")
    print(f"{dp_v} poin \t| Rp {dp_w}000 \t| {dp_time*1000:.3f} ms")
    print("Merchandise yang dibeli  :\n-->", merch_dipilih)

    start = time.perf_counter()
    gd_v, gd_w, merch_dipilih = greedy_by_density(C, n, merch, v, w)
    gd_time = time.perf_counter() - start
    print("\n=== Hasil Greedy by Density ===")
    print("kepuasan \t| Anggaran \t| Waktu")
    print(f"{gd_v} poin \t| Rp {gd_w}000 \t| {gd_time*1000:.3f} ms")
    print("Merchandise yang dibeli  :\n-->", merch_dipilih)

    start = time.perf_counter()
    gv_v, gv_w, merch_dipilih = greedy_by_value(C, n, merch, v, w)
    gv_time = time.perf_counter() - start
    print("\n=== Hasil Greedy by Value ===")
    print("kepuasan \t| Anggaran \t| Waktu")
    print(f"{gv_v} poin \t| Rp {gv_w}000 \t| {gv_time*1000:.3f} ms")
    print("Merchandise yang dibeli  :\n-->", merch_dipilih)

    start = time.perf_counter()
    gw_v, gw_w, merch_dipilih = greedy_by_weight(C, n, merch, v, w)
    gw_time = time.perf_counter() - start
    print("\n=== Hasil Greedy by Weight ===")
    print("kepuasan \t| Anggaran \t| Waktu")
    print(f"{gw_v} poin \t| Rp {gw_w}000 \t| {gw_time*1000:.3f} ms")
    print("Merchandise yang dibeli  :\n-->", merch_dipilih)

    start = time.perf_counter()
    ga_v, ga_w, merch_dipilih = knapsack_ga(C, n, merch, v, w)
    ga_time = time.perf_counter() - start
    print("\n=== Hasil Genetic Algorithm ===")
    print("kepuasan \t| Anggaran \t| Waktu")
    print(f"{ga_v} poin \t| Rp {ga_w}000 \t| {ga_time*1000:.3f} ms")
    print("Merchandise yang dibeli  :\n-->", merch_dipilih)

    # Tampilkan hasil dan waktu eksekusi
    print("\n=== Perbandingan Algoritma Knapsack ===")
    knapsack_dp(C, n, merch, v, w)
    print(f"Dynamic Programing  : ({dp_v}, {dp_w}) ({dp_time*1000:.3f} ms)")
    print(f"Greedy by Density   : ({gd_v}, {gd_w}) ({gd_time*1000:.3f} ms)")
    print(f"Greedy by Value     : ({gv_v}, {gv_w}) ({gv_time*1000:.3f} ms)")
    print(f"Greedy by Weight    : ({gw_v}, {gw_w}) ({gw_time*1000:.3f} ms)")
    print(f"Genetic Algorithm   : ({ga_v}, {ga_w}) ({ga_time*1000:.3f} ms)")