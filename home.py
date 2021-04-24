import sys

def calculate(width, height, words, case):
    fontsize = width // max(map(len, words))

    # iterate over fontsize until a result or fontsize=0
    while fontsize:
        col = len(words[0])
        row = 0
        for word in words[1:]:

            if col + 1 + len(word) > (width // fontsize):
                row += 1
                col = len(word)

                if row >= height / fontsize:
                    break
            else:
                col += 1 + len(word)
        # word check loop ended - does it fit?

        if row >= height // fontsize:
            fontsize -= 1
        else:

            break
    # while
    print(f"Case #{case + 1}: {fontsize}")


n = int(input())
for _ in range(n):
    line = input().split()
    width = int(line[0])
    height = int(line[1])
    words = line[2:]

    calculate(width, height, words, _)