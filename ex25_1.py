words="learn .python .the hard .way is fun"
print(words.split())#默认根据空格拆分字符
changed=words.split('.')
print(changed)

print(changed.pop(2))#删除列表中的第几个字符并返回他的值，从0开始计数
print(changed)
for i in changed:
    print(f"the string is {i}")

A=[[9,11]*2 for i in  range(3)]#多维列表
print(A)
