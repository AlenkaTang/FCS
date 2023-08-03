import random

def keyGeneration():
    p = int(input ("Enter prime number p, (p < 100)"))
    q = int(input ("Enter prime number q, (q < 100)"))
    if ((p > 100) or (q > 100)):
        p = input ("Invalid input. Enter prime number p, (p < 100)")
        q = input ("Invalid input. Enter prime number q, (q < 100)")

    n = p * q
    totient_n = 0
    for i in range(n):
        for j in range(n):
            if((i * j)% n == 1):
                totient_n = totient_n + 1
    d = 0
    while(d == 0):
        e =  random.randrange(3, totient_n)
        for i in range(totient_n):
            if(((e * i) % totient_n) == 1):
                d = i
    result = []
    result.append(n)
    result.append(e)
    result.append(d)
    return result


def rsa_encryption(int_input, publicKey):
    n = publicKey[0]
    e = publicKey[1]
    result = int_input ** e
    result = result % n
    return result

def rsa_decryptipn(int_input, privateKey):
    n = privateKey[0]
    d = privateKey[1]
    result = int_input ** d
    result = result % n
    return result

keySet = keyGeneration()
publicKey = []
publicKey.append(keySet[0])
publicKey.append(keySet[1])
privateKey = []
privateKey.append(keySet[0])
privateKey.append(keySet[2])
m = input("enter int to be encrypted")
m = int(m)
c = rsa_encryption(m,publicKey)
print("encrypted message", c)
m = rsa_decryptipn(c,privateKey)
print("decrypted message", m)


    


