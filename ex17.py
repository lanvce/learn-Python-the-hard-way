from sys import argv
from os.path import exists

script,from_file,to_file=argv

#print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line,how?
in_file=open(from_file,'w');
in_file.write("If sudaqiang is your father");
in_file=open(from_file,'r');
indata=in_file.read()
#print("Ready,hit RETURN to continue,CTRL_C to abort.")

#input()

out_file=open(to_file,'w')
out_file.write(indata)
out_file=open(to_file,'r')
print(out_file.read())
#print("Alright,all done.")

out_file.close()
in_file.close()
