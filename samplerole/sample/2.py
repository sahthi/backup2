from urllib.request import urlopen
import sys

def fetch_data(url):
     try:
           w=urlopen(url)
     except:
           print("BAD url")
           sys.exit(100)
     data=w.read()
     data_s=str(data,"utf-8")
     return data_s

if __name__ == "__main__":
     print (fetch_data("https://sixty-north.com/c/t.txt"))
