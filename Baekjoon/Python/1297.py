A, B, C = map(int, input().split())
mux = (A**2) / (B**2 + C**2)
print(int((B**2 * mux)**0.5), int((C**2 * mux)**0.5))