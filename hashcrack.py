import hashlib
import sys
import pyfiglet

ascii_banner = pyfiglet.figlet_format("crack with kira")
print (ascii_banner)

print("""ALGORITMA:
1)MD5
2)SHA1
3)SHA224
4)SHA256
5)SHA384
6)SHA512
""")

tipe_hash:int = int(input("mau hash tipe apa?:"))
lokasi_wordlist:str = str(input("masukkan lokasi wordlist:"))
hash:str = str(input("masukkan hash:"))

word_list:str = open(f"{lokasi_wordlist}").read()
lists:list[str] = word_list.splitlines()

for word in lists:
    if tipe_hash == 1 :
        hash_object = hashlib.md5(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1;32m HASH FOUND: {word} \n")
    elif tipe_hash == 2:
        hash_object = hashlib.sha1(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1;32m HASH FOUND: {word} \n")
    elif tipe_hash == 3:
        hash_object = hashlib.sha224(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1;32m HASH FOUND: {word} \n")
    elif tipe_hash == 4:
        hash_object = hashlib.sha256(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1;32m HASH FOUND: {word} \n")
    elif tipe_hash == 5:
        hash_object = hashlib.sha384(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1;32m HASH FOUND: {word} \n")
    elif tipe_hash == 6:
        hash_object = hashlib.sha512(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1;32m HASH FOUND: {word} \n")
    else:
        print ("MASUKKAN NILAI HASH YANG ADA PADA LIST DI ATAS!!!")