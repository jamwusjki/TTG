list1 = []
list2 = []
list3 = []
def bin(x):
    sb = x.find('=')
    st = x[0:sb]
    j = sb + 1
    sd = x[j:len(x)]
    list2.append(st)
    list3.append(sd)
    
def go(p):
    if "'" in p:
        e = len(p) - 1
        print(p[1:e])
    else:
        v = list2.index(p)
        print(list3[v])

def lex(l):
    if 'go' in l:
        xs = l.find('(')
        lp = xs + 1
        xc = l.find(')')
        go(l[lp:xc])
    if '=' in l:
        bin(l)

while True:
    c = input(">>")
    list1.append(c)
    if c == 'os':
        for i in range(len(list1)):
            lex(list1[i])
        list1 = []
    if c == 'quit':
        break