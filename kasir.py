menu = [["nasi goreng",110000],["nasi uduk",90000],["ayam bakar",170000]]

def menu_makanan():
    print("#-------------------------------#")
    print("# No | Nama Makanan | Harga -----------#")
    print("#------------------------------------------#")
    i = 1
    for item in menu:
        print("#" +  str(i)  + "|" + item[0] + "|" + str(item[1]) + "#")
        i+=1
        print("#--------------------------#")
        print("# 0 | checkout #")
        print("#-----------------------------#")
        return





menu_makanan()
jawaban = ""
catatan_pilihan=[]
while jawaban !="0":
    jawaban = input("pilih menu makanan :")
    menu_makanan()
    if jawaban != "0":
        catatan_pilihan.append(int(jawaban)-1)



no = 1
print("pesanan anda :")
total=0
for pilihan in catatan_pilihan:
    print("makanan ke-" +str(no) + "="  +menu[pilihan[0]] + "harga +" + str(menu[pilihan[1]]))
    no+=1
    total =total + menu[pilihan][1]

print("total pembayaran" + str(total))
