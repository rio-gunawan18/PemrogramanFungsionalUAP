#Soal 8.1
ganjil = [x for x in range(51) if x % 2 != 0]
kelipatan_tiga = [x for x in ganjil if x % 3 == 0]

# Pemetaan
hasil_pemetaan_8_1 = [f"{x} kelipatan 3" for x in kelipatan_tiga]
print("soal 8.1")
print(hasil_pemetaan_8_1)
print()

#Soal 8.2
def is_prima(angka):
    if angka < 2:
        return False
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            return False
    return True

data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

hasil_filter = list(filter(is_prima, data))

# Pemetaan
hasil_pemetaan_8_2 = [f"{x} angka prima" for x in hasil_filter]
print("soal 8.2")
print(hasil_pemetaan_8_2)
print()

#Soal 8.3
def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    reversed_string = cleaned_string[::-1]
    return cleaned_string == reversed_string

string = 'Ada apa dengan si m rio gunawan'
kata_kalimat = string.split()

palindrome = [kata.lower() for kata in kata_kalimat if is_palindrome(kata)]
print("soal 8.3")
# Pemetaan
hasil_pemetaan_8_3_palindrome = [f'{kata} Palindrom' for kata in palindrome]
print(hasil_pemetaan_8_3_palindrome)

non_palindrome = [kata.lower() for kata in kata_kalimat if not is_palindrome(kata)]

# Pemetaan
hasil_pemetaan_8_3_non_palindrome = [f'{kata} Non-Palindrom' for kata in non_palindrome]
print(hasil_pemetaan_8_3_non_palindrome)
