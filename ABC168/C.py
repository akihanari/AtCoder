# coding: utf-8
import math
A, B, H, M = map(int, input().split())
H = H * 30 + ((M / 60) * 30)
M = M * 6
deg = min(abs(H - M),360 - abs(H - M))
ans = A**2 + B**2 - (2 * A * B * math.cos(math.radians(deg)))
ans = ans**0.5
print(ans)
