from Crypto.Util.number import *
import random
from sympy import nextprime
flag = "RAHASIA"
tahap = 30
paket_soal = ["A", "B", "C", "D", "E"]
print(f"Selesaikan {tahap} tahap untuk mendapatkan flag!\n")
print("Kirimkan plainteks dalam bentuk format KRIPTOGRAFIITB{secret}!\n")
print("Tips: buatlah kode untuk otomasi :D\n")
counter = 0
try:
    for step in range(tahap):
        print(f"---------------- Tahap-{step}----------------\n")
        message_asli = "KRIPTOGRAFIITB{" + str(random.randint(1,10000))+ "}"
        message_asli = message_asli.encode('utf-8')
        message_int = bytes_to_long(message_asli)
        version = random.choice(paket_soal)
        print(f"paket_soal = {version}\n")
        if version == "A":
            while True:
                ran = random.randint(1, 100)
                p = nextprime(getStrongPrime(1024) - ran)
                q = nextprime(nextprime(nextprime(nextprime(p) + ran) + ran) - ran)
                n = p * q
                e = 65537
                check = GCD(e, (p-1)*(q-1)) == 1
                if check: break
            enc = pow(message_int, e, n)
        elif version == "B":
            p = getStrongPrime(1024)
            n = p * p
            e = 65537
            enc = pow(message_int, e, n)
        elif version == "C":
            while True:
                p = getStrongPrime(1024)
                q = getStrongPrime(1024)
                e = random.randrange(1,65537)
                n = p * q
                tot = (p-1) * (q-1)
                e = random.randint(2**15, 2**16)
                check = GCD(e, (p-1)*(q-1)) == 1
                if check: break
            d = pow(e, -1, tot)
            enc = pow(message_int, d, n)
            e = d
        elif version == "D":
            p = getStrongPrime(1024)
            q = getStrongPrime(1024)
            n = p*q
            e = 3
            enc = pow(message_int, e, n)
        elif version == "E":
            n = getStrongPrime(1024)
            e = 65537
            enc = pow(message_int, e, n)
        
        print(f"n = {n}\n")
        print(f"e = {e}\n")
        print(f"c = {enc}\n")
        
        try:
            print("Jawaban = ")
            input_dec = input().strip("\n")
            if input_dec == message_asli.decode():
                print("Uwaw keren!!!\n")
                counter += 1
            else:
                print(":((((((\n")
        except Exception as e:
            print("Error\n")
except Exception as e:
    print("Error\n")
finally:
    if counter == tahap:
        print(f"Uhuyyyy {flag}\n")
    else:
        print("Tetap semangat dan jangan putus asa!\n")