import pyperclip
d={"1":" One","2":" Two","3":" Three","4":" Four","5":" Five","6":" Six","7":" Seven","8":" Eight","9":" Nine","0":" Zero"}
h=pyperclip.paste()
pairs = h.split(", ")
symbol_dict = {}
for pair in pairs:
    number, symbol = pair.split(" = ")
    symbol_dict[symbol] = number
print(symbol_dict)
m={"@":"0", "(":"1","&":"2","!":"3","#":"4","^":"5",")":"6","$":"7","%":"8","*":"9"}
j="India :"
k=" (+91 "
o=input("Enter:")
f=pyperclip.paste()
for i in f:
    if i in symbol_dict.keys():
        k=k+symbol_dict[i]
    else:
       k=k+i
for i in k[6:]:
    if i in d.keys():
        j=j+d[i]
print(j+k+")")
pyperclip.copy(j+k+")")