print (100*('*'))
txt = "Luas Permukaan Prisma Segitiga"
x = txt.center (100)
print (x)
print (100*('*'))

print ('\nKelompok : 10')
print ('\nSabtu, shift kedua')
print ('\nAnggota Kelompok :')
print ('1. Ahmad Aldani Herlangga (21120120140168)')
print ('2. Enrico Gathan Agung (21120123140127)')
print ('3. Naufal Labib Nugroho (21120123130109)')
print ('4. Rafi Rai Pasha Afandi (21120123100073)\n')
print('tulis nama kalian pada project, jangan lupa save setelah melakukan PERUBAHAN')

#Input
sisi_segitiga1 = 8
sisi_segitiga2 = (4**2 + 4**2)**(0.5)
sisi_segitiga3 = (4**2 + 4**2)**(0.5)
tinggi_prisma = 20
tinggi_segitiga = 4

print (f'Sisi 1 segitiga : {sisi_segitiga1}')
print (f'Sisi 2 segitiga : {sisi_segitiga2:.3F}')
print (f'Sisi 3 segitiga: {sisi_segitiga3:.3F}')
print (f'Tinggi prisma : {tinggi_prisma}')
print (f'Tinggi Segitiga : {tinggi_segitiga}\n')

#Hitung
luaspermukaan_permukaan = (2 * (1/2 * sisi_segitiga1 * tinggi_segitiga)) + ((sisi_segitiga1 + sisi_segitiga2 + sisi_segitiga3) * tinggi_prisma)

#Output
print (f'Maka luas permukaan prisma tersebut adalah : {luaspermukaan_permukaan:.3F}')