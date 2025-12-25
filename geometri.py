import time                             # digunakan untuk mengukur durasi eksekusi algoritma
import matplotlib.pyplot as plt         # digunakan untuk memvisualisasikan data
from prettytable import PrettyTable     # digunakan untuk menampilkan data dalam format tabel

# agar grafik bisa update tanpa harus nutup window
plt.ion()

# fungsi rekursif - manggil dirinya sendiri sampe n=1
def geometric_recursive(a, r, n):
    if n == 1:
        return a
    return a * (r ** (n - 1)) + geometric_recursive(a, r, n - 1)

# fungsi iteratif - pake loop biasa
def geometric_iterative(a, r, n):
    total = 0
    term = a
    for _ in range(n):
        total += term
        term *= r
    return total

# menyimpan data buat grafik
n_values = []
recursive_times = []
iterative_times = []

# menampilkan tabel hasil
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["Jumlah Suku (n)", "Waktu Rekursif (ms)", "Waktu Iteratif (ms)"]

    for i in range(len(n_values)):
        table.add_row([
            n_values[i],
            f"{recursive_times[i]:.6f}",
            f"{iterative_times[i]:.6f}"
        ])

    print(table)

# update grafik perbandingan
def update_graph():
    plt.clf()
    
    plt.plot(n_values, recursive_times, label="Rekursif", marker='o')
    plt.plot(n_values, iterative_times, label="Iteratif", marker='o')

    plt.xlabel("Jumlah Suku (n)")
    plt.ylabel("Waktu Eksekusi (ms)")
    plt.title("Perbandingan Waktu Eksekusi Deret Geometri")
    plt.legend()
    plt.grid(True)
    
    plt.draw()
    plt.pause(0.1)

# nilai awal deret
a = 2  # suku pertama (opsional bisa diisi nilai berapapun)
r = 3  # rasio (opsional bisa diisi nilai berapapun)
MAX_N = 50  # batas maksimal suku ke-n (max library dapat menerima input adalah 999)


# loop utama
while True:
    try:
        n = int(input(f"Masukkan jumlah suku n (1-{MAX_N}, ketik -1 untuk keluar): "))

        if n == -1:
            print("Program selesai.")
            break

        if n <= 0:
            print("Nilai n harus lebih dari 0!")
            continue

        if n > MAX_N:
            print(f"Nilai n maksimal {MAX_N}!")
            continue

        n_values.append(n)

        # hitung waktu rekursif
        start = time.perf_counter_ns()
        geometric_recursive(a, r, n)
        recursive_times.append((time.perf_counter_ns() - start) / 1_000_000)

        # hitung waktu iteratif
        start = time.perf_counter_ns()
        geometric_iterative(a, r, n)
        iterative_times.append((time.perf_counter_ns() - start) / 1_000_000)

        print_execution_table()
        update_graph()

    except ValueError:
        print("Input harus angka!")
