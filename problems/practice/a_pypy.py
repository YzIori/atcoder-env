#!/usr/bin pypy3

def main(a, b, c, S):
    print(a+b+c, S)

if __name__ == "__main__":
    a = int(input())
    b, c = map(int, input().split())
    S = input()

    main(a, b, c, S)