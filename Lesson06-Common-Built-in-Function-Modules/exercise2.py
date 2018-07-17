def caesar_code(s,t):
    s = str(s)
    t = int(t)
    l = []
    for i in range(len(s)):
        aa = ord(s[i])+t
        if aa > 122:
            b = aa-123
            aa = 97+b
        l.append(chr(aa))
        
    return ''.join(l)
caesar_code('xvillage',3)
