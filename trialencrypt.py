# This is the program we believe was used to encode the intercepted message.
# some of the retrieved program was damaged (show as &&&&)
# Can you use this to figure out how it was encoded and decode it? 
# Good Luck

import string
import random
from base64 import b64encode, b64decode

secret = 'HelloRitwik' # Assuming this as plaintext

secret_encoding = ['step1', 'step2', 'step3']

def step1(s):	#Substitution Cipher
	#make a Mapping/Translation table with the provided strings
	_step1 = str.maketrans("zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA","mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON")	
	#converts the plaintext to ciphertext with monoalphabetic substitution
	step1_convertedstr=str.translate(s, _step1)
	print('Converted string after Step1:',step1_convertedstr)
	return step1_convertedstr

def step2(s):	#encoding function for Base64 encoding
	s=s.encode()
	double_encoded = b64encode(s)
	print('double encoded string:',double_encoded)
	print('Type after step2:',type(double_encoded))
	return double_encoded.decode()

def step3(plaintext, shift=4):	#Substitution cipher: Caesar cipher with SHIFT = 4
	loweralpha = string.ascii_lowercase
	shifted_string = loweralpha[shift:] + loweralpha[:shift] #creating Key for Caeser cipher with shift=4
	print('KEY string:',shifted_string)
	converted = str.maketrans(loweralpha, shifted_string) # creating Translation table: Dictionary[a:e,b:f,c:g....]
	step3_convertedstr= str.translate(plaintext,converted)  #encrypting via Ceaser cipher, substituting characters
	print('COnverted string after Step3:',step3_convertedstr)
	return step3_convertedstr

def make_secret(plain, count):
	a = '2{}'.format(b64encode(plain).decode()) 
	print('a:',a)
	print(type(a))
	for count in range(count):		#works same as XRANGE function
		r = random.choice(secret_encoding)	#randomly choosing any of the encryption steps defined above
		print('r:',r)
		si = secret_encoding.index(r) + 1
		print('si:',si)
		_a = globals()[r](a)	#function call to abovementioned functions via parameters
		print(type(_a))
		print('_a:',a)
		a = '{}{}'.format(si, _a)
		print('modified a:',a)
	return a

if __name__ == '__main__':
	print('Plaintext (i.e. secret) =',secret)
	print ('Ciphertext = ',make_secret(secret.encode(), count=2)) #prints the final Ciphertext.




