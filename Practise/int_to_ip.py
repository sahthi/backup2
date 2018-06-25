def int_to_ip(num):
    '''function accepts an integer and returns a string in format of WWW.XXX.YYY.ZZZ'''
    string=str(num)
    return (string[0]*3+'.'+string[1]*3+'.'+string[2]*3+'.'+string[3]*3)
num=input("enter numbers:")
print(int_to_ip(num))
