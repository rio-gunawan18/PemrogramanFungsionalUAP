#1. Data tuple:
data_tuple = ('Pensil', 1500, 'Buku', 5000, 'Penggaris', 2000)

#2. Fungsi untuk memishkan data tuple:
def pisah_data(data_tuple):
    nama = [data_tuple[i] for i in range(0, len(data_tuple),2)]
    harga = [data_tuple[i] for i in range(1, len(data_tuple), 2)]
    return nama, harga

#3. Fungsi untuk membuat dictionary:
def membuat_dictionary(nama, harga):
    return dict(zip(nama, harga))

#4. Hasil:
print(f"1. {data_tuple}")
nama_list, harga_list = pisah_data(data_tuple)
print(f"2. {nama_list} {harga_list}")
hasil_dict = membuat_dictionary(nama_list, harga_list)
print(f"3. {hasil_dict}")