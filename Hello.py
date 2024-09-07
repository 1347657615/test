# -*- coding:utf-8 -*-
import __hello__


print('Hello world!')

def hello() -> None:
    print('Hello World!')  

def Hello() -> str:
    return "Hello World!"

def main() -> None:
    inputbox = input('Please write"hello":')
    if inputbox == 'hello':    
        return hello()


if __name__=='__main__':
    main()
