from Crypto.Util.number import *
import random
flag = "RAHASIA"
def main():
    arsip = {}
    p = getStrongPrime(512)
    q = getStrongPrime(512)
    n = p * q
    tot = (p-1) * (q-1)
    e = random.randint(2**15, 2**16)
    while GCD(e, tot) != 1:
        e = random.randint(2**15, 2**16)
    d = pow(e, -1, tot)
    nomor_arsip_admin = random.randint(2, 100000000)
    while isPrime(nomor_arsip_admin):
        nomor_arsip_admin = random.randint(2, 100000000)
    arsip[nomor_arsip_admin] = flag
    try:
        perintah = "0"
        while perintah != "4":
            print("Selamat datang di arsip dijital Kriptografi ITB!")
            print("Ketik angka untuk menjalankan perintah: ")
            print("1. Tambah Arsip")
            print("2. Baca Arsip")
            print("3. Nomor Arsip Admin")
            print("4. Keluar")
            print("")
            print("Masukkan perintah: ", end="")
            perintah = input().strip("\n")
            if perintah == "1":
                print("Masukkan nomor arsip (dalam bentuk integer): ")
                nomor_arsip = input().strip("\n")
                if int(nomor_arsip) == int(nomor_arsip_admin):
                    print("Nomor arsip admin tidak boleh diganti")
                    continue
                print("Masukkan isi arsip: ", end="")
                input_arsip = input().strip("\n")
                arsip[int(nomor_arsip)] = input_arsip
                cipher_nomor_arsip = pow(int(nomor_arsip), e, n)
                print(f"Token akses nomor arsip: {cipher_nomor_arsip}")
            elif perintah == "2":
                try:
                    print("Masukkan token akses nomor arsip (dalam bentuk integer):", end="")
                    nomor_arsip = input().strip("\n")
                    plain_nomor_arsip = pow(int(nomor_arsip), d, n)
                    print(f"Isi arsip: {arsip[int(plain_nomor_arsip)]}")
                except Exception as e:
                    print("Token akses nomor arsip invalid")
            elif perintah == "3":
                print(f"Nomor arsip admin: {nomor_arsip_admin}")
            elif perintah == "4":
                exit()
            else:
                print("Perintah tidak dikenal")
    except Exception as e:
        print("Terjadi kesalahan")

if __name__ == "__main__":
    main()