def hitung_pangkat(pangkat):
    def pangkat_dalam_closure(angka):
        return angka ** pangkat
    
    return pangkat_dalam_closure

pangkat_dua = hitung_pangkat(2)
pangkat_tiga = hitung_pangkat(3)

print(pangkat_dua(5))
print(pangkat_tiga(2))
