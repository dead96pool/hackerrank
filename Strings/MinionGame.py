def minion_game(string):
    kevin, stuart = 0, 0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            print(string[i])



if __name__ == '__main__':
    s = input()
    minion_game(s)