str = input()
answer = ''
for c in str:
    if c == c.lower():
        answer += c.upper()
    else:
        answer += c.lower()
print(answer)