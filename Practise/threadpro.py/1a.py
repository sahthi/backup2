import string
f1 = open("file1.txt","r")
f2 = open("file2.txt","w")
fr =  f1.readlines()

for line in fr:
        for word in line:
                f2.write(word)
f2.close()
def sed(pattern_string,replacement_string,file1,file2):
        f3 = open(file2,"r")
        f4 = f3.readlines()
        for line in f4:
                for word in line.split():
                        if pattern_string  == word:
                                print line.replace(pattern_string,replacement_string)

sed("the","***********","file1.txt","file2.txt")

