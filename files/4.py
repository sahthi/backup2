#!/usr/bin/python

def Main():
    words = ['deltas','desalt','lorry','lasted','retainers','salted','aerospace','slated','staled','resmelts',]
    out = []
    for i in range(0,len(words)-2):
        for j in range(i+1,len(words)):
            if sorted(words[i]) == sorted(words[j]):
                if words[i] not in out:
                    out.append(words[i])
    print out
                
if __name__ == "__main__":
    Main()
