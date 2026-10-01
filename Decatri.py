import random
import os

Code_Fake = ['X', 'J', 'K', 'L', 'Z']

def SetupCode():
	danh_sach_code = [] 
	for i in range(10): 
		for j in range(i + 1, 10): 
			for k in range(j + 1, 10): 
				danh_sach_code.append(f"{i}{j}{k}" ) 

	c = random.sample(danh_sach_code, 120)
	with open('Code-Decatri', 'w', encoding='utf-8') as f:
		for i in range(26): 
			d = chr(i+ord('a'))
			f.write(f"{str(d)} {c[i]} \n")
		f.write(f"S {c[26]} \n") # Space
		f.write(f"N {c[27]} \n") # Comma .
		f.write(f"P {c[28]} \n") # Period ,
		f.write(f"E {c[29]} \n") # Exclamation !
		f.write(f"Q {c[30]} \n") # Question ?
		f.write(f"A {c[31]} \n") # Apostrophe ' '
		f.write(f"T {c[32]} \n") # Quote " "
		f.write(f"O {c[33]} \n") # Open_paren (
		f.write(f"C {c[34]} \n") # Close_paren )
		f.write(f"U {c[35]} \n") # UPPER

		# Fake code
		f.write(f"X {c[36]} \n") 
		f.write(f"J {c[37]} \n")
		f.write(f"K {c[38]} \n")
		f.write(f"L {c[39]} \n")
		f.write(f"Z {c[40]} \n")

	print("New Code Decatri")

def Encrypt(text=None, debug=False):
	print("="*50)
	
	if not os.path.exists('Code-Decatri'):
		print("Not found file 'Code-Decatri'. You check file in folder?")
		SetupCode()
		return

	text_end = ''
	for w in text:
		if w.isupper(): 
			text_end += 'U'
			text_end += w.lower()
		elif w==' ': text_end += 'S' # space
		elif w==',': text_end += 'N' # ,
		elif w=='.': text_end += 'P' # .
		elif w=='!': text_end += 'E' # !
		elif w=='?': text_end += 'Q' # ?
		elif w=="'": text_end += 'A' # ''
		elif w=='"': text_end += 'T' # ""
		elif w=='(': text_end += 'O' # (
		elif w==')': text_end += 'C' # )

		else: text_end += w

		for i in range(random.randint(0, 3)):
			text_end += random.choice(Code_Fake) # Cái này là mã nhứ/ mã giả	

	danh_sach_code = {} 
	with open("Code-Decatri", "r", encoding="utf-8") as f: 
		for line in f: 
			ky_tu, code = line.rsplit() 
			danh_sach_code[ky_tu] = code 

	encode = ''
	encode_d = ''
	log_system = ''
	n, m = 0, 8
	for w in text_end:
		if w not in danh_sach_code: continue
		r = danh_sach_code[w]
		t = list(r)
		random.shuffle(t)
		t = ''.join(t)
		encode += f"{t} "
		encode_d += f"{t}"
		log_system += f" '{w}' -> {t} "
		if n == m: log_system += '\n'
		else: log_system += '|'
		n = (n +1)%(m+1)

	if debug:
		print("-"*50)
		print(f"Handle: {text_end}")
		print("-"*50)
		print(log_system)
	
	print("-"*50)
	print(f"Encrypt (3-digit):\n{encode}\n")
	print(f"Encrypt (no space):\n{encode_d}\n")


def Decrypt(text=None, debug=False):
	print("="*50)
	danh_sach_code = {} 
	with open("Code-Decatri", "r", encoding="utf-8") as f: 
		for line in f: 
			ky_tu, code = line.rsplit() 
			danh_sach_code[code] = ky_tu

	print(f"Encode: {text}")
	text = text.replace(" ", "")

	list_encode = []
	for i in range(0, len(text), 3):
		list_encode.append( text[i:i+3] )

	b = []
	for i in list_encode:
		b.append(''.join( sorted( list( i ))))

	c = ''
	for n in b:
		if n in danh_sach_code: c+=danh_sach_code[n]
		else: c+='#'
	
	if debug:
		print("-"*50)
		print(list_encode)
		print("-"*50)
		print(b)
		print("-"*50)
		print(c)

	text_end = ''
	Check_Upper = False
	for w in c:
		if w in Code_Fake: pass
		elif w=='S': text_end += ' ' # space
		elif w=='N': text_end += ',' # ,
		elif w=='P': text_end += '.' # .
		elif w=='E': text_end += '!' # !
		elif w=='Q': text_end += '?' # ?
		elif w=='A': text_end += "'" # ''
		elif w=='T': text_end += '"' # ""
		elif w=='O': text_end += '(' # (
		elif w=='C': text_end += ')' # )
		elif w=='U': Check_Upper = True
		elif w=='#': pass
		else: 
			if Check_Upper:
				text_end += w.upper()
				Check_Upper = False
			else: text_end += w

	print("-"*50)
	print('Text: ',text_end)

#SetupCode()
#Encrypt("Hello, World!")
#Decrypt("418938863058975470873386902318138186290368386942594957184317209873681863807873850378381683837092642597158386085957")

print("======= Run Decatri Cipher =======")
print("Type: 'E' to encrypt, 'D' to decrypt, nothing to exit. TY")
type = input(">").lower()
if type=='e': 
	print("Encrypt - Code plain text")
	text=input("Text: ")
	Encrypt(text)
elif type=='d': 
	print("Decrypt - Shifted ciphertext")
	code=input("Ciphertext: ")
	Decrypt(code)
else: print(":P exit")