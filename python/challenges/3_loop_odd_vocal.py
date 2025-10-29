# TODO: Program untuk mencetak bilangan ganjil dari 1 hingga 15
odd_numbers = []
for x in range(1, 16):
    if x % 2 != 0:
        odd_numbers.append(x)
        
print(odd_numbers)

# TODO: Program menghitung jumlah huruf vokal
word = input("Masukkan kata: ").lower()

vowels = "aiueo"
count = 0

for char in word:
    if char in vowels:
        count += 1
        
print("Jumlah huruf vokal:", count)
