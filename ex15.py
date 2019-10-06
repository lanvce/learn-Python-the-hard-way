from  sys import argv #导入参数变量库

script,filename=argv #脚本名，文件名

way=open(filename)#将读取的文件赋给way

print(f"Here is your file {filename}:")#打印文件名
print(way.read())#打印读取文件内容
way.close()
print("Type the filename again :")
file_again=input(">")#>后输入的内容为文件名
txt_again=open(file_again)#将读取的文件赋给txt_again
print(txt_again.read())#打印读取文件内容
txt_again.close()
