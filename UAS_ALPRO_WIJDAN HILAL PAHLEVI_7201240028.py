import os
from collections import deque

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' berhasil dibuat.")
    else:
        print(f"Folder '{folder_name}' sudah ada.")

def delete_folder(folder_name):
    if os.path.exists(folder_name):
        os.rmdir(folder_name)
        print(f"Folder '{folder_name}' berhasil dihapus.")
    else:
        print(f"Folder '{folder_name}' tidak ditemukan.")

def create_file(file_name):
    if not os.path.exists(file_name):
        open(file_name, 'w').close()
        print(f"File '{file_name}' berhasil dibuat.")
    else:
        print(f"File '{file_name}' sudah ada.")

def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File '{file_name}' berhasil dihapus.")
    else:
        print(f"File '{file_name}' tidak ditemukan.")

def write_to_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
        print(f"Berhasil menulis ke file '{file_name}'.")

def read_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            print(f"Isi file '{file_name}':\n{file.read()}")
    else:
        print(f"File '{file_name}' tidak ditemukan.")

# Searching for a file or folder
def search_item(name, path="."):
    found_items = []
    for root, dirs, files in os.walk(path):
        if name in dirs or name in files:
            found_items.append(os.path.join(root, name))
    if found_items:
        print(f"Item ditemukan di:")
        for item in found_items:
            print(item)
    else:
        print(f"Item '{name}' tidak ditemukan.")

# Sorting items in a directory
def sort_items(path="."):
    try:
        items = os.listdir(path)
        items.sort()
        print("Isi folder setelah disortir:")
        for item in items:
            print(item)
    except FileNotFoundError:
        print(f"Path '{path}' tidak ditemukan.")

# Stack implementation (LIFO)
stack = []
def push_to_stack(item):
    stack.append(item)
    print(f"'{item}' ditambahkan ke stack.")

def pop_from_stack():
    if stack:
        item = stack.pop()
        print(f"'{item}' dihapus dari stack.")
    else:
        print("Stack kosong.")

# Queue implementation (FIFO)
queue = deque()
def enqueue(item):
    queue.append(item)
    print(f"'{item}' ditambahkan ke queue.")

def dequeue():
    if queue:
        item = queue.popleft()
        print(f"'{item}' dihapus dari queue.")
    else:
        print("Queue kosong.")

def main():
    while True:
        print("\n=== Sistem Manajemen File dan Folder ===")
        print("1. Buat Folder")
        print("2. Hapus Folder")
        print("3. Buat File")
        print("4. Hapus File")
        print("5. Tulis ke File")
        print("6. Baca File")
        print("7. Cari File atau Folder")
        print("8. Sortir Isi Folder")
        print("9. Tambah ke Stack")
        print("10. Hapus dari Stack")
        print("11. Tambah ke Queue")
        print("12. Hapus dari Queue")
        print("13. Keluar")

        choice = input("Pilih opsi (1-13): ")

        if choice == '1':
            folder_name = input("Masukkan nama folder: ")
            create_folder(folder_name)
        elif choice == '2':
            folder_name = input("Masukkan nama folder: ")
            delete_folder(folder_name)
        elif choice == '3':
            file_name = input("Masukkan nama file: ")
            create_file(file_name)
        elif choice == '4':
            file_name = input("Masukkan nama file: ")
            delete_file(file_name)
        elif choice == '5':
            file_name = input("Masukkan nama file: ")
            content = input("Masukkan isi file: ")
            write_to_file(file_name, content)
        elif choice == '6':
            file_name = input("Masukkan nama file: ")
            read_file(file_name)
        elif choice == '7':
            name = input("Masukkan nama file atau folder yang dicari: ")
            search_item(name)
        elif choice == '8':
            path = input("Masukkan path folder (tekan Enter untuk folder saat ini): ") or "."
            sort_items(path)
        elif choice == '9':
            item = input("Masukkan item untuk ditambahkan ke stack: ")
            push_to_stack(item)
        elif choice == '10':
            pop_from_stack()
        elif choice == '11':
            item = input("Masukkan item untuk ditambahkan ke queue: ")
            enqueue(item)
        elif choice == '12':
            dequeue()
        elif choice == '13':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
