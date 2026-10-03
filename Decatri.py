import random as rn

type="""abcdefghijklmnopqrstuvwxyz0123456789,.!?;:'\"()-_[]{}=@#$&+*/%<>|\\US"""
index=[]
for i in range(10):
    for j in range(i+1,10):
        for k in range(j+1,10):
            index.append(f"{i}{j}{k}")
indexf = [
    f"{a}{b}{c}"
    for a in '0123456789'
    for b in '0123456789'
    for c in '0123456789'
    if len({a, b, c})<3
]

def encrypt(text):
    print('='*15+' ENCRYPT '+'='*15)
    print(text)
    print('-'*39)
    t=''
    for w in text:
        t+='F' if rn.randint(0,1) else ''
        if w.isupper():t+='U'+w.lower()
        elif w==' ':t+='S'
        else:t+=w
    print(t,'\n')
    c1,c2='',''
    for w in t:
        code=rn.choice(indexf)
        if w!='F':code=encrypt_code[w]
        
        code=list(code)
        rn.shuffle(code)
        code=''.join(code)
        
        c1+=code+' '
        c2+=code
    
    print(c1,'\n')
    print(c2,'\n')

def decrypt(code):
    print('='*15+' DECRYPT '+'='*15)
    print(code)
    print('-'*39)
    code=code.replace(" ", "")
    print(code,'\n')
    t=''
    for i in range(0,len(code),3):
        c=code[i:i+3]
        c=''.join(sorted(c))
        if not c in indexf: t+=decrypt_code[c]
    print(t,'\n')
    text=''
    upper=False
    for w in t:
        if w=='U': upper=True
        elif upper: 
            text+=w.upper()
            upper=False
        elif w=='S':text+=' '
        else: text+=w
    print(text,'\n')

r=rn.Random(str(input("Key:")))
c=r.sample(index,len(index))
encrypt_code=dict(zip(type,c))
decrypt_code=dict(zip(c,type))
choice=input("Type 'E'ncrypt or 'D'ecrypt:")
if choice.upper()=='E':
	text=input("Text:")
	encrypt(text)
else: 
	code=input("Code:")
	decrypt(code)
