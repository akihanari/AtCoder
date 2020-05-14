# coding: utf-8
S = input()
X = abs(753 - int(S[:3]))
for i in range(len(S)-2):
    X = min(abs(753 - int(S[i:i+3])), X)
print(X)
