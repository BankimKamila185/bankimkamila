openfile = open('abc.txt','w')
string = "print('file demo')"
print(string, file=open_file)
open_file.close()
