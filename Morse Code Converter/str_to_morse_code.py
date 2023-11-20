morse_dict = {'A':'. -',
              'B':'- . . .',
              'C':'- . - .',
              'D':'- . .',
              'E':'.',
              'F':'. . - .',
              'G':'- - .',
              'H':'. . . .',
              'I':'. .',
              'J':'. - - -',
              'K':'- . -',
              'L':'. - . .',
              'M':'- -',
              'N':'- .',
              'O':'- - -',
              'P':'. - - .',
              'Q':'- - . -',
              'R':'. - .',
              'S':'. . .',
              'T':'-',
              'U':'. . -',
              'V':'. . . -',
              'W':'. - -',
              'X':'- . . -',
              'Y':'- . - -',
              'Z':'- - . .',
              '0':'- - - - -',
              '1':'. - - - -',
              '2':'. . - - -',
              '3':'. . . - -',
              '4':'. . . . -',
              '5':'. . . . .',
              '6':'- . . . .',
              '7':'- - . . .',
              '8':'- - - . .',
              '9':'- - - - .'}

def morese_code_coverter(str):
        morse = ''
        for let in str:
            if let in morse_dict:
                morse+=morse_dict[let] + '  '
            else:
                morse += let + '  '
            # elif let == ' ':
            #     morse+='/ '    
        morse.join(morse)
        print(f'Morse code of your str is: {morse}')
    
def main():
    while True:
        str=input('Type a string you want to convert into morse code (Type "exit" to end): ').upper()
        if str.lower()=='exit':
            break
        morese_code_coverter(str)
        ask_again=input('Do you want to convert another text (Type: y/n): ').upper()
        if ask_again!='Y':
            break
                  
if __name__=='__main__':
    main()
    
# should_end=True
# str = input(f'Type a string you want to convert into morse code: ').upper()
# while True:
    