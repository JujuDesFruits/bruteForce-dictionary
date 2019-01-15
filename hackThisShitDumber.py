import re, itertools, hashlib, sys, datetime
alphabet  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','@','_','#','0','1','2','3','4','5','6','7','8','9']
MAXLEN = 5
MINLEN = 3
string=""
size=0

def display(s):
   print(s)

def redo(string,size):
    if size <= MAXLEN:
        for i in alphabet:
            tmpString=string+i
            tmpSize=size+1
            redo(tmpString,tmpSize)
            if MINLEN <= len(tmpString):
                current_hash=hashlib.md5(tmpString.encode('utf')).hexdigest()
                if current_hash in pwdTable.values():
                    display('mot de passe trouve \'{}\' pour l\'utilisateur {}'.format(tmpString, ','.join(i for i in pwdTable if pwdTable[i] == current_hash)))


with open('shadow', 'r') as f:
    lines = f.readlines()

pwdTable = {}
for line in lines:
   try:
      user, user_hash = re.findall('^([^:]+):\$1\$([^:]+):.+', line)[0]
   except IndexError:
      continue  # si la ligne ne contient pas de hash on passe a la ligne suivante
   else:
      pwdTable[user] = user_hash

display('\n'+str(len(pwdTable))+' Mot de passe chiffré sous MD5 trouvé, déchiffrage en cours entre '+str(MINLEN+1)+' et '+str(MAXLEN+1)+' caractères...\n')
redo(string,size)
