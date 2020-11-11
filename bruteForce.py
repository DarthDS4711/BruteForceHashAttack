#!/usr/bin/env python
#_*_coding: utf-8_*_
import hashlib
import os
def md5Attack():
	hashpass = str(input("HASH: "))
	if(len(hashpass) == 32):
		finded = False
		passwordFinded = ""
		passwordList = open("passwords.txt", "r")
		for p in passwordList.readlines():
			word = p.strip("\n")
			word = word.encode('utf-8')
			word = hashlib.md5(word).hexdigest()
			if(word == hashpass):
				passwordFinded = p
				finded = True
				break
			print(p)
		passwordList.close()
		if(finded == True):
			print("Password: {} HASH: {}".format(passwordFinded, hashpass))
		else:
			print("Tu hash no esta encontrado en el diccionario de datos se podria decir que es seguro :)")

	else:
		print("Longitud de hash incorrecta")
def sha1Attack():
	hashpass = str(input("HASH: "))
	if(len(hashpass) == 40):
		finded = False
		passwordFinded = ""
		passwordList = open("passwords.txt", "r")
		for p in passwordList.readlines():
			word = p.strip("\n")
			word = word.encode('utf-8')
			word = hashlib.sha1(word).hexdigest()
			if(word == hashpass):
				passwordFinded = p
				finded = True
				break
			print(p)
		passwordList.close()
		if(finded == True):
			print("Password: {} HASH: {}".format(passwordFinded, hashpass))
		else:
			print("Tu hash no esta encontrado en el diccionario de password se podria decir que es segura :)")

def sha224Attack():
	hashpass = str(input("HASH: "))
	if(len(hashpass) == 56):
		finded = False
		passwordFinded = ""
		passwordList = open("passwords.txt", "r")
		for p in passwordList.readlines():
			word = p.strip("\n")
			word = word.encode('utf-8')
			word = hashlib.sha224(word).hexdigest()
			if(word == hashpass):
				passwordFinded = p
				finded = True
				break
			print(p)
		passwordList.close()
		if(finded == True):
			print("Password: {} HASH: {}".format(passwordFinded, hashpass))
		else:
			print("Tu hash no esta encontrado en el diccionario de password se podria decir que es segura :)")

def sha256Attack():
	hashpass = str(input("HASH: "))
	if(len(hashpass) == 64):
		finded = False
		passwordFinded = ""
		passwordList = open("passwords.txt", "r")
		for p in passwordList.readlines():
			word = p.strip("\n")
			word = word.encode('utf-8')
			word = hashlib.sha256(word).hexdigest()
			if(word == hashpass):
				passwordFinded = p
				finded = True
				break
			print(p)
		passwordList.close()
		if(finded == True):
			print("Password: {} HASH: {}".format(passwordFinded, hashpass))
		else:
			print("Tu hash no esta encontrado en el diccionario de password se podria decir que es segura :)")

def sha384Attack():
	hashpass = str(input("HASH: "))
	if(len(hashpass) == 96):
		finded = False
		passwordFinded = ""
		passwordList = open("passwords.txt", "r")
		for p in passwordList.readlines():
			word = p.strip("\n")
			word = word.encode('utf-8')
			word = hashlib.sha384(word).hexdigest()
			if(word == hashpass):
				passwordFinded = p
				finded = True
				break
			print(p)
		passwordList.close()
		if(finded == True):
			print("Password: {} HASH: {}".format(passwordFinded, hashpass))
		else:
			print("Tu hash no esta encontrado en el diccionario de password se podria decir que es segura :)")

def sha512Attack():
	hashpass = str(input("HASH: "))
	if(len(hashpass) == 128):
		finded = False
		passwordFinded = ""
		passwordList = open("passwords.txt", "r")
		for p in passwordList.readlines():
			word = p.strip("\n")
			word = word.encode('utf-8')
			word = hashlib.sha512(word).hexdigest()
			if(word == hashpass):
				passwordFinded = p
				finded = True
				break
			print(p)
		passwordList.close()
		if(finded == True):
			print("Password: {} HASH: {}".format(passwordFinded, hashpass))
		else:
			print("Tu hash no esta encontrado en el diccionario de password se podria decir que es segura :)")

def obtainOption(option):
	os.system("cls")
	if(option == "1"):
	   md5Attack()
	elif(option == "2"):
	   sha1Attack()
	elif(option == "3"):
	   sha224Attack()
	elif(option == "4"):
	   sha256Attack()
	elif(option == "5"):
	   sha384Attack()
	elif(option == "6"):
	   sha512Attack()
	else:
		print("No ingresaste una opcion valida")


def main():
	print("Ataque de fuerza bruta a un password cifrado\n")
	print("Ingresa el tipo de hash\n")
	print("1.-MD5\n2.-SHA-1\n3.-SHA-224\n4.-SHA-256\n5.-SHA-384\n6.-SHA-512: ")
	option = str(input())
	obtainOption(option)
	input("Presione una tecla para salir...")

if __name__ == '__main__':
	main()