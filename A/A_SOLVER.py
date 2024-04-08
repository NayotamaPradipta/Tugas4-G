from math import isqrt
from sympy import mod_inverse
import gmpy2
import re 
import subprocess 
def case_A(n, e, c):
    a = isqrt(n) +  1
    b2 = a*a - n
    b = isqrt(b2)

    while (b*b != b2):
        a += 1
        b2 = a*a - n
        b = isqrt(b2)
    p = a+b 
    q = a-b 
    totient_n = (p-1)*(q-1)
    d = mod_inverse(e, totient_n)
    # Decrypt
    m_int = pow(c, d, n)
    return m_int

def case_B(n, e, c):
    p = isqrt(n)
    print(f"p: {p}")
    totient_n = p * (p-1)
    d = mod_inverse(e, totient_n)
    # Decrypt
    m_int = pow(c, d, n)
    return m_int

def case_C(n, e, c):
    return 

def case_D(n, e, c):
    m_int = cube_root(c, e)
    return m_int

def case_E(n, e, c):
    totient_n = n - 1
    d = mod_inverse(e, totient_n)
    # Decrypt
    m_int = pow(c, d, n)
    return m_int

def decode_m(m_int):
    m_bytes = m_int.to_bytes((m_int.bit_length() + 7) // 8, byteorder='big')
    m_str = m_bytes.decode()
    return m_str

def cube_root(c, e):
    message_int = gmpy2.iroot(c, e)[0]
    return int(message_int)

def auto_solve(main_program):
    n_pattern = re.compile(r'n = (\d+)')
    e_pattern = re.compile(r'e = (\d+)')
    c_pattern = re.compile(r'c = (\d+)')
    paket_pattern = re.compile(r'paket_soal = (\w)')
    process = subprocess.Popen(['python', main_program], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    n, e, c = None, None, None
    while True: 
        line = process.stdout.readline()
        if not line:
            break 
        print(line, end='')
             
        n_match = n_pattern.search(line)
        if n_match: 
            n = int(n_match.group(1))

        e_match = e_pattern.search(line)
        if e_match: 
            e = int(e_match.group(1))
        
        c_match = c_pattern.search(line)
        if c_match:
            c = int(c_match.group(1))
        
        paket_match = paket_pattern.search(line)
        if paket_match:
            paket = paket_match.group(1)
        if "Jawaban =" in line: 
            if n is not None and e is not None and c is not None: 
                if paket == 'A':
                    decrypted_message = case_A(n, e, c)
                elif paket == 'B':
                    decrypted_message = case_B(n, e, c)
                elif paket == 'C':
                    decrypted_message = case_C(n, e, c)
                elif paket == 'D':
                    decrypted_message = case_D(n, e, c)
                elif paket == 'E':
                    decrypted_message = case_E(n, e, c)
                decrypted_message = decode_m(decrypted_message)
                print(decrypted_message)
                process.stdin.write(decrypted_message + '\n')
                process.stdin.flush()
                n, e, c = None, None, None 
if __name__ == "__main__":
    auto_solve("RSA_A.py")