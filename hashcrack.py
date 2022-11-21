import hashlib
import sys
import pyfiglet

ascii_banner = pyfiglet.figlet_format("crack with kira")
print (ascii_banner)

print("ALGORITMA:\nMD5\nSHA1\nSHA224\nSHA256\nSHA384\nSHA512")

tipe_hash = str(input("mau hash tipe apa?:"))
lokasi_wordlist = str(input("masukkan lokasi wordlist:"))
hash = str(input("masukkan hash:"))

word_list = open(f"{lokasi_wordlist}").read()
lists = word_list.splitlines()

for word in lists:
    if tipe_hash == "MD5" :
        hash_object = hashlib.md5(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1;32m HASH FOUND: {word} \n")
    elif tipe_hash == "SHA1":
        hash_object = hashlib.sha1(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1;32m HASH FOUND: {word} \n")
    elif tipe_hash == "SHA224":
        hash_object = hashlib.sha224(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1;32m HASH FOUND: {word} \n")
    elif tipe_hash == "SHA256":
        hash_object = hashlib.sha256(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1;32m HASH FOUND: {word} \n")
    elif tipe_hash == "SHA384":
        hash_object = hashlib.sha384(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1;32m HASH FOUND: {word} \n")
    elif tipe_hash == "SHA512":
        hash_object = hashlib.sha512(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1;32m HASH FOUND: {word} \n")
    else:
        print ("MASUKKAN NILAI HASH YANG ADA PADA LIST DI ATAS!!!")