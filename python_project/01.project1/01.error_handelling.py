file = open('youtube.txt','w')

try:
    file.write('Hello world')
finally:
    file.close()

with open('youtube.txt','w') as file:
    file.write('chai aur code')
    