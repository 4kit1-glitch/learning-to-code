text = "why are you up this late?"
word = "Jockerr"

#capitalize
print(text.capitalize())

#casefole
print(word.casefold())

#center
print(word.center(6))

#count
print(text.count(" ", 4, 12),)

#encode
txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

print(txt.encode(encoding="ascii", errors="replace"))

#endswith
print(text.endswith('?'))

#expandtabs
txt = "h\te\tl\tl\t"

print(txt.expandtabs(4))

#find
print(word.find('e'))

#index , isalpha, isalphanum

#isascii
print(word.isascii())

#isnumeric / isdigit / isdecimal
txt = "123434d3"
print(txt.isdigit(),txt.isdecimal(), txt.isnumeric(), txt.isalnum())

#isidentifier
print(txt.isidentifier())







