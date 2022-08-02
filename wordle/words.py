import random
words=[]
i = 1
batas = int(input())
while i <= batas:
    word=input()
    words.append(word)
    i += 1
def get_word():
    return random.choice(words)
# print(get_word())