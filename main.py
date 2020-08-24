#regex

import re

txt = "The rain in Spain"

# retorna um Match object
# procura frase que começa com The e termina com Spain
x = re.search("^The.*Spain$", txt)
print(x)
print(x.span())


txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x) 


# \d
# gera objeto List com todos os digitos encontrados.
txt = "essa sequencia contem um digito 1"
x = re.findall("\d", txt)

if x:
    print(x)

#retorna objeto Match
x = re.search("\d", txt)

if x:
    print(x.group())



x = re.findall("\D", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


#\ sequencia especial ?
# hello$ = "termina em hello"
#  ^xxxxx - começa com ^
#  . aqualquer caratere como em "he..o"
#  
#
#
#
#
#