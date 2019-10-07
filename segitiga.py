def main():
    # menampilkan informasi program
    print("menghitung keliling segitiga \n")
   
    # input panjang, lebar, dan tinggi
    p = float(input("Panjang sisi A \t  : "))
    l = float(input("panjang sisi b \t\t: "))
    t = float(input("panjang sisi c \t\t: "))
   
    # melakukan perhitungan
    V = p + l + t
   
    # menampilkan hasil perhitungan ke layar
    print("\nkeliling \t\t: ", V)

   
if __name__ == "__main__":
    main()