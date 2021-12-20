word = list(input().strip())
wordcpy = "".join(word)
G = []
X = []
S = []
V = []
I = []
U = []
F = []
E = []
R = []
H = []
O = []
N = []
T = []
W = []

while 'G' in word:
    G.append(word.index("G"))
    word.remove("G")
word = list(wordcpy)
while 'X' in word:
    X.append(word.index("X"))
    word.remove("X")
word = list(wordcpy)
while 'S' in word:
    S.append(word.index("S"))
    word.remove("S")
word = list(wordcpy)
while 'V' in word:
    V.append(word.index("V"))
    word.remove("V")
word = list(wordcpy)
while 'I' in word:
    I.append(word.index("I"))
    word.remove("I")
word = list(wordcpy)
while 'U' in word:
    U.append(word.index("U"))
    word.remove("U")
word = list(wordcpy)
while 'F' in word:
    F.append(word.index("F"))
    word.remove("F")
word = list(wordcpy)
while 'E' in word:
    E.append(word.index("E"))
    word.remove("E")
word = list(wordcpy)
while 'R' in word:
    R.append(word.index("R"))
    word.remove("R")
word = list(wordcpy)
while 'H' in word:
    H.append(word.index("H"))
    word.remove("H")
word = list(wordcpy)
while 'O' in word:
    O.append(word.index("O"))
    word.remove("O")
word = list(wordcpy)
while 'N' in word:
    N.append(word.index("N"))
    word.remove("N")
word = list(wordcpy)
while 'T' in word:
    T.append(word.index("T"))
    word.remove("T")
word = list(wordcpy)
while 'W' in word:
    W.append(word.index("W"))
    word.remove("W")


isDigit = False


# O N E
if len(O) > 0 and len(N) > 0 and len(E) > 0:
    Nt = [x for x in N if x > O[0]]
    if len(Nt) > 0:
        Et = [x for x in E if x > Nt[0]]
        if len(Et) > 0:
            isDigit = True
            print(1)

# T W O
if len(T) > 0 and len(W) > 0 and len(O) > 0:
    Wt = [x for x in W if x > T[0]]
    if len(Wt) > 0:
        Ot = [x for x in O if x > Wt[0]]
        if len(O) > 0:
            isDigit = True
            print(2)

# T H R E E
if len(T) > 0 and len(H) > 0 and len(R) > 0 and len(E) > 1:
    Ht = [x for x in H if x > T[0]]
    if len(Ht) > 0:
        Rt = [x for x in R if x > Ht[0]]
        if len(Rt) > 0:
            Et = [x for x in E if x > Rt[0]]
            if len(Et) > 1:
                isDigit = True
                print(3)

# F O U R
if len(F) > 0 and len(O) > 0 and len(U) > 0 and len(R) > 0:
    Ot = [x for x in O if x > F[0]]
    if len(Ot) > 0:
        Ut = [x for x in U if x > Ot[0]]
        if len(Ut) > 0:
            Rt = [x for x in R if x > Ut[0]]
            if len(Rt) > 0:
                isDigit = True
                print(4)

# F I V E
if len(F) > 0 and len(I) > 0 and len(V) > 0 and len(E) > 0:
    It = [x for x in I if x > F[0]]
    if len(It) > 0:
        Vt = [x for x in V if x > It[0]]
        if len(Vt) > 0:
            Et = [x for x in E if x > Vt[0]]
            if len(Et) > 0:
                isDigit = True
                print(5)

# S I X
if len(S) > 0 and len(I) > 0 and len(X) > 0:
    It = [x for x in I if x > S[0]]
    if len(It) > 0:
        Xt = [x for x in  X if x > It[0]]
        if len(Xt) > 0:
            isDigit = True
            print(6)

# S E V E N
if len(S) > 0 and len(N) > 0 and len(V) > 0 and len(E) > 1:
    Et = [x for x in E if x > S[0]]
    if len(Et) > 0:
        Vt = [x for x in V if x > Et[0]]
        if len(Vt) > 0:
            Ett = [x for x in Et if x > Vt[0]]
            if len(Ett) > 0:
                Nt = [x for x in N if x > Ett[0]]
                if len(Nt) > 0:
                    isDigit = True
                    print(7)

# E I G H T
if len(E) > 0 and len(I) > 0 and len(G) > 0 and len(H) > 0 and len(T) > 0:
    It = [x for x in I if x > E[0]]
    if len(It) > 0:
        Gt = [x for x in G if x > It[0]]
        if len(Gt) > 0:
            Ht = [x for x in H if x > Gt[0]]
            if len(Ht) > 0:
                Tt = [x for x in T if x > Ht[0]]
                if len(Tt) > 0:
                    isDigit = True
                    print(8)

# N I N E
if len(N) > 1 and len(I) > 0 and len(E) > 0:
    It = [x for x in I if x > N[0]]
    if len(It) > 0:
        Nt = [x for x in N if x > It[0]]
        if len(Nt) > 0:
            Et = [x for x in E if x > Nt[0]]
            if len(Et) > 0:
                isDigit = True
                print(9)

if not isDigit:
    print("NO")