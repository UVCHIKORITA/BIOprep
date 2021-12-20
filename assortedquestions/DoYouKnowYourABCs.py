all_vals = list(map(int, input().strip().split(" ")))

maxVal = max(all_vals)
all_vals.remove(maxVal)
BandC = max(all_vals)
all_vals.remove(BandC)
A = maxVal - BandC
AandC = max(all_vals)
all_vals.remove(AandC)
C = AandC - A
B = BandC - C
print(str(A)+" "+str(B)+" "+str(C))