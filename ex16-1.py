from sys import argv
script,filename=argv
demo=open(filename,'w+')#只要沾上w就会清空以前的文件 r则必须存在文件 a是在末尾添加
print(demo.read())
#print(demo.readline(1))
#demo=open(filename,'w')

x=input("请输入第一行:")
y=input("请输入第二行:")
demo.write(x)
demo.write("\n")
demo.write(y)
print(demo.read())
