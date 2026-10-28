
print("Jumlah Pembelian Pakaian Bayi")

baju_bayi = 45000 * 2
celana_bayi = 32000 * 1
jumper_bayi = 58000 * 2
kaus_kaki = 12000 * 2
topi_bayi = 18000 * 1

total = baju_bayi + celana_bayi + jumper_bayi + kaus_kaki + topi_bayi

dapat_diskon = total > 100000

print("Total Pembelian: Rp" + str(total))

if dapat_diskon == True:
    diskon = total * 0.15
    total_akhir = total - diskon
    print("Besar Diskon: Rp" + str(int(diskon)))
    print("Mendapatkan Diskon")
    print("Total Bayar: Rp" + str(int(total_akhir)))
else:
    print("Tidak Dapat Diskon!")
    print("Total Bayar: Rp" + str(total))
