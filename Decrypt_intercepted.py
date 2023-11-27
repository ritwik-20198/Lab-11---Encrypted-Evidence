import string
from base64 import b64encode, b64decode

#Inputting the ciphertext in intercepted.txt via file handling 'open' function.
file_path = 'intercepted.txt'
with open(file_path, 'r') as file:
     intercepted_text= file.read()

def Decrypt_step1(s):
	#To generate the decrypt function for step1, we transpose the parameter strings while creating the Translation Table.
	d_step1 = str.maketrans("mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON","zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA")
	step1_dconvertedstr=str.translate(s, d_step1)
	print('Decrypted Converted string after Step1:',step1_dconvertedstr)
	return step1_dconvertedstr

def Decrypt_step2(s):
	#To generate the decrypt function for step2, we decode the Base64 encoding
	step2_decoded=b64decode(s.encode())
	print('Decrypted Converted string after Step2:',step2_decoded.decode())
	return step2_decoded.decode()


def Decrypt_step3(ciphertext, shift=4):
	#To generate the decrypt function for step3, we transpose the parameter strings while creating the Translation Table.
	loweralpha = string.ascii_lowercase
	shifted_string = loweralpha[shift:] + loweralpha[:shift] #creating Key for Caeser cipher with shift=4
	print('KEY string:',shifted_string)
	converted = str.maketrans(shifted_string,loweralpha) # creating Translation table: Dictionary[a:e,b:f,c:g....]
	step3_convertedstr= str.translate(ciphertext,converted)  #decrypting via Ceaser cipher, substituting characters
	print('Decrypted converted string after Step3:',step3_convertedstr)
	return step3_convertedstr

print('Intercepted Ciphertext: ',intercepted_text)
ia = intercepted_text

# List to store the sequence of decryption steps taken
Sequence_of_Decryption_steps = []

# we keep checking the ciphertext, until it has numeric values (1,2,3) in the beginning, signifying the encryption steps
while(ia[:1].isnumeric()):
		r = 'Decrypt_step'+ia[:1]
		print('Taking ',r)
		Sequence_of_Decryption_steps.append(ia[:1])
		ia = ia[1:]
		ia = ia +'='
		_a = globals()[r](ia)
		ia=_a
		print('partial decrypted text:',ia)

print('Plaintext (i.e. Secret Message) = ',ia)
print('Decryption steps Sequence :',Sequence_of_Decryption_steps)