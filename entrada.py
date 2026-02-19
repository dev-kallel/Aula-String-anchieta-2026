print()
print()
name = input("Nome: ")
print()
dominio = input("Domínio: ")

print()
print()

print ('Suas informações:'+'\n'+'\n'+'Nome: ' + name + ' - Domínio: '+ dominio +'\n'+'\n'+'Bem-vindo ao Python!!!!!!!!!!!!!!!!' +'\n'+'\n' + "O seu email é: "+ name.lower()+"@"+dominio.lower()+".com"+'\n'+'\n')
email = name+dominio+str('com')

print()

#colocar string com letras minúsculas

palavra = name

#colocar string com letras maíusculas 

print('Colocando o texto em letra maíuscula: '+palavra.upper())
print()
PALAVRA = name
print('Colocando o texto em letra minúscula: '+palavra.lower())
print()

#Gerar senha automaticamente pelo contador de string

print ("Sua senha automática a partir do seu email:")
a = email.count('a')
e = email.count('e')
i = email.count('i')
o = email.count('o')
u = email.count('u')

print()

print("Senha: a"+str(a)+"e"+str(e)+"i"+str(i)+"o"+str(o)+"u"+str(u))

print()
