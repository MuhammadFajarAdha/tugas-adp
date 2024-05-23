print("nama : muhammad fajar adha")
print("nim  : 2310432040")
print("shift: 4")

def load_data():
    try:
        with open("finance.txt", "r") as file:
            data = file.readlines()
            data_dict = {}
            for line in data:
                transaction = line.strip().split(",")
                data_dict[transaction[0]] = {
                    "description": transaction[1],
                    "amount": float(transaction[2]),
                    "type": transaction[3]
                }
            return data_dict
    except FileNotFoundError:
        return {}

def save_data(data):
    with open("finance.txt", "w") as file:
        for tanggal, transaksi in data.items():
            file.write(f"{tanggal},{transaksi['description']},{transaksi['amount']},{transaksi['type']}\n")

def display_data(data):
    print("Data Keuangan:")
    for tanggal, transaksi in data.items():
        print(f"Tanggal: {tanggal}")
        print(f"Deskripsi: {transaksi['description']}")
        print(f"Jumlah: {transaksi['amount']}")
        print(f"Tipe: {transaksi['type']}")
        print()

def add_transaction(data):
    tanggal = input("Tanggal: ")
    description = input("Deskripsi: ")
    amount = float(input("Jumlah: "))
    tipe = input("Tipe (pemasukan/pengeluaran): ")
    data[tanggal] = {"description": description, "amount": amount, "type": tipe}
    save_data(data)
    print("Data berhasil disimpan!")

def delete_transaction(data):
    tanggal = input("Tanggal transaksi yang ingin dihapus: ")
    if tanggal in data:
        del data[tanggal]
        save_data(data)
        print("Data berhasil dihapus!")
    else:
        print("Data tidak ditemukan!")

data = load_data()
while True:
    print("Menu:")
    print("1. Tampilkan data keuangan")
    print("2. Tambahkan transaksi baru")
    print("3. Hapus transaksi")
    print("4. Keluar")
    choice = input("Pilihan: ")
    if choice == "1":
        display_data(data)
    elif choice == "2":
        add_transaction(data)
    elif choice == "3":
        delete_transaction(data)
    elif choice == "4":
        break
    else:
        print("Pilihan tidak valid!")