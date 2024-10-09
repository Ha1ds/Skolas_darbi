input_fails=open("data.txt","r")
saturs=input_fails.read()
input_fails.close()

output_fails=open("output.txt","w")
output_fails.write(saturs)
output_fails.close()

