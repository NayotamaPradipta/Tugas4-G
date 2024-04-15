from A_SOLVER import case_A, case_B, case_C, case_D, case_E, decode_m
while True: 
    paket_soal = input("Paket Soal: ")
    n = int(input("n: "))
    e = int(input("e: "))
    c = int(input("c: "))

    if (paket_soal == 'A'):
        decrypted_message = case_A(n, e, c)
    elif (paket_soal == 'B'):
        decrypted_message = case_B(n, e, c)
    elif (paket_soal == 'C'):
        decrypted_message = case_C(n, e, c)
    elif (paket_soal == 'D'):
        decrypted_message = case_D(n, e, c)
    elif (paket_soal == 'E'):
        decrypted_message = case_E(n, e, c)

    decrypted_message = decode_m(decrypted_message)
    print(decrypted_message)