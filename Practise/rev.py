def reverse(string):
       s=string.split()
       inputword=s[ : :-1]
       output=' '.join(inputword)
       return output
if __name__=="__main__":
       string="hai this is"
       print reverse(string)

