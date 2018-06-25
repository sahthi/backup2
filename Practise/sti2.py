def toggle(mystr):
        arr = []
        for char in mystr:
            if char.upper() != char:
                char=char.upper()
                arr.append(char)
            else:
                char=char.lower()
                arr.append(char)
        return ''.join(map(str,arr))
user_input = raw_input()
output = toggle(user_input)
print output
