formatter="{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))#"字符串需要引号，数字或者逻辑判断不需要"
print(formatter.format(True,False,False,True))#True or False 首字母要大写
print(formatter.format(formatter,formatter,formatter,formatter))

print(formatter.format("Try your","own text here","Maybe a poem","Or a song about fear"))
