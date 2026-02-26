print()

email = nome.lower().strip()+str('.')+sobrenome.lower().strip()+str('@')+universid.lower().strip()+str('.br')

print("Seus dados a partir de suas respostas:")
print()
print()

print('Seu email é: '+email)
print()

print ("Sua senha automática a partir do seu email:")
a = email.count('a')
e = email.count('e')
i = email.count('i')
o = email.count('o')
u = email.count('u')
print()
print("Senha: a"+str(a)+"e"+str(e)+"i"+str(i)+"o"+str(o)+"u"+str(u))
print()

print(nome.upper().strip()+" "+sobrenome.upper().strip()+', nasceu no dia: '+data_nasc.strip()+' e estuda na universidade: '+universid.upper().strip())
print()
print()

#Formatar textos com {^}

print(f'{nome.upper().strip()} {sobrenome.upper().strip()}, nasceu no dia: {data_nasc.strip()} e estuda na universidade: {universid.upper().strip()}')
