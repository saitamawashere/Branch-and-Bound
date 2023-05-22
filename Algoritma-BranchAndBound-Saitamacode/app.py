import queue

# Fungsi untuk menghitung batasan pada masalah
def compute_bound(node):
    # Implementasikan rumus atau metode perhitungan batasan sesuai dengan masalah yang ingin diselesaikan
    # Di sini, kita akan menggunakan contoh sederhana yaitu menjumlahkan elemen-elemen array
    return sum(node['partial_solution']) + sum(node['remaining_elements'])

# Fungsi untuk mencetak solusi optimal
def print_solution(node):
    print("Solusi optimal:", node['partial_solution'])

# Fungsi untuk menjalankan algoritma Branch and Bound
def branch_and_bound(elements):
    n = len(elements)
    initial_node = {'partial_solution': [], 'remaining_elements': elements}
    best_solution = None
    q = queue.Queue()
    q.put(initial_node)

    while not q.empty():
        node = q.get()

        # Jika node merupakan solusi yang lengkap
        if len(node['remaining_elements']) == 0:
            if best_solution is None or sum(node['partial_solution']) < sum(best_solution):
                best_solution = node['partial_solution']
        
        # Jika node masih membutuhkan pemisahan
            else:
                bound = compute_bound(node)
                if best_solution is None or bound < sum(best_solution):
                    for i in range(len(node['remaining_elements'])):
                        new_partial_solution = node['partial_solution'] + [node['remaining_elements'][i]]
                        new_remaining_elements = node['remaining_elements'][:i] + node['remaining_elements'][i+1:]
                        new_node = {'partial_solution': new_partial_solution, 'remaining_elements': new_remaining_elements}
                        q.put(new_node)
    return best_solution

# Main program
if __name__ == '__main__':
    elements = input("Masukkan elemen-elemen array (pisahkan dengan spasi): ").split()
    elements = [int(e) for e in elements]
    solution = branch_and_bound(elements)
    if solution:
        print_solution(solution)
    else:
        print("Tidak ditemukan solusi optimal.")
