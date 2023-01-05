# -*- coding:utf-8 -*-
print('Hello world!')

def hello():
    print('Hello World!')


def main():
    inputbox = input('Please write"hello":')
    if inputbox == 'hello':
        return hello()


if __name__=='__main__':
    main()
