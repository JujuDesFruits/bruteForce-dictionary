import re, itertools, hashlib, sys

sys.stdout = open('decrypt_password', 'w')

def display(result):
    print(result)

with open('shadow', 'r') as f:
   lines = f.readlines()

pwdTable = {}
for line in lines:
   try:
      user, user_hash = re.findall('^([^:]+):\$1\$([^:]+):.+', line)[0]
   except IndexError:
      continue  # si la ligne ne contient pas de hash on passe a la ligne suivante
   else:
      pwdTable[user]=user_hash

with open('dico_mini_fr', 'r') as f:
   lines = f.readlines()

for line in lines:
    word=line.strip()
    current_hash = hashlib.md5(word.encode('utf')).hexdigest()
    for user, password in pwdTable.items():
        if current_hash == password:
            display("le code trouver pour l'utilisateur "+user+" est "+word)
