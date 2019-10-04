def faktorial(n):
    if n <= 1:
        return 1
    else:
        return n*faktorial(n-1)

#Program utama
for n in range(11):
   print ("%d! = %d" % (n, faktorial(n)))
while True:
    try:
        n=input('Nilai n! : ')
        print ('Faktorial %d! = %d'%(n,faktorial(n)))
    except:
        continue
    

# Fungsi Fibonacci
def fibonacci(n):
    if n < 0:
        print ("Tidak ada bilangan yang bernilai negatif")
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Program utama
for n in range(11):
   print ("Fibonacci(%d) = %d" % (n, fibonacci(n)))
while True:
    try:
        n=input("Masukkan sebuah bilangan : ")
        print ("Fibonacci(%d) = %d"%(n,fibonacci(n)))
    except:
        continue
    break