x, y, w, h = map(int, input().split())
print(min(min(abs(w-x), abs(0-x)), min(abs(h-y), abs(0-y))))
