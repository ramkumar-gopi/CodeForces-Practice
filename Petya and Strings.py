word1 = input().lower()
word2 = input().lower()

if word1 > word2:
    print(1)
elif word2 > word1:
    print(-1)
elif word1 == word2:
    print(0)