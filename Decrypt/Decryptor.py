from os import system
from Decrypt_pack import rotation_decrypt
from Decrypt_pack import key_decrypt
from Decrypt_pack import rotation_and_key
from Decrypt_pack import rotation_decrypt_uppercase
from Decrypt_pack import key_decrypt_uppercase
from Decrypt_pack import rotation_and_key_uppercase
from Decrypt_pack import rotation_decrypt_letters
from Decrypt_pack import key_decrypt_letters
from Decrypt_pack import rotation_and_key_letters
from Decrypt_pack import test
from Decrypt_pack import test_uppercase
from Decrypt_pack import test_letters
from Decrypt_pack import test_key
from Decrypt_pack import test_uppercase_key
from Decrypt_pack import test_letters_key
def main():
    try:
        from argparse import ArgumentParser

    except:
        system('pip3 install argparse')
        from argparse import ArgumentParser

    parse = ArgumentParser(description="Decryptes a text",prog="Decrypter",epilog='For more information about this tool read |README.txt|')

    parse.add_argument('-t','--text',help='Path of the text file which will be decrypted.',type=str)
    parse.add_argument('-n','--number',help ='Rotation number or decryption.',type=int,nargs="?",default=None)
    parse.add_argument('-p','--path',help='Path where decrypted text will be written.',nargs = '?',default='decrypted_text.txt',type=str)
    parse.add_argument('-k','--key',help='Key which will be used for decryption.',nargs="?",default = None,type=str)
    parse.add_argument('-uc','--upper_case',help='Text will be decrypted with the base of uppercase letters.',const=True,nargs='?',default=False,type=bool)
    parse.add_argument('-lo','--letters_only',help='Text will be decrypted with the base of only letters.',const=True,nargs='?',default=False,type=bool)

    args = parse.parse_args()

    try:
        if not args.number and not args.key:
            raise ValueError('One(key or rotation number) or both should be given')
        
        if args.upper_case and args.letters_only:
            raise ValueError('Only one(uppercase or letters only) should be given')
        
        with open(args.text,'r+') as f:
            text = f.read().strip()
        
        if not args.upper_case and not args.letters_only:
            test(text)
            if args.number and not args.key:
                new_text = rotation_decrypt(rotation_number=args.number,text=text)
                with open(args.path,'w+') as nf:
                    nf.write(new_text)

                    print(f'Successfully decrypted text to {args.path}')
        
            if not args.number and args.key:
                test_key(args.key)
                new_text = key_decrypt(key=args.key,text=text)
                with open(args.path,'w+') as nf:
                    nf.write(new_text)
                
                    print(f'Successfully decrypted text to {args.path}')

            if args.number and args.key:
                test_key(args.key)
                new_text = rotation_and_key(rotation_number=args.number,key=args.key,text=text)
                with open(args.path,'w+') as nf:
                    nf.write(new_text)
                
                    print(f'Successfully decrypted text to {args.path}')

        if args.upper_case and not args.letters_only:
            test_uppercase(text)
            if args.number and not args.key:
                new_text = rotation_decrypt_uppercase(rotation_number=args.number,text=text)
                with open(args.path,'w+') as nf:
                    nf.write(new_text)

                    print(f'Successfully decrypted text to {args.path}')
        
            if not args.number and args.key:
                test_uppercase_key(args.key)
                new_text = key_decrypt_uppercase(key=args.key,text=text)
                with open(args.path,'w+') as nf:
                    nf.write(new_text)
                
                    print(f'Successfully decrypted text to {args.path}')

            if args.number and args.key:
                test_uppercase_key(args.key)
                new_text = rotation_and_key_uppercase(rotation_number=args.number,key=args.key,text=text)
                with open(args.path,'w+') as nf:
                    nf.write(new_text)
                
                    print(f'Successfully decrypted text to {args.path}')
        
        if not args.upper_case and args.letters_only:
            test_letters(text)
            if args.number and not args.key:
                new_text = rotation_decrypt_letters(rotation_number=args.number,text=text)
                with open(args.path,'w+') as nf:
                    nf.write(new_text)

                    print(f'Successfully decrypted text to {args.path}')
        
            if not args.number and args.key:
                test_letters_key(args.key)
                new_text = key_decrypt_letters(key=args.key,text=text)
                with open(args.path,'w+') as nf:
                    nf.write(new_text)
                
                    print(f'Successfully decrypted text to {args.path}')

            if args.number and args.key:
                test_letters_key(args.key)
                new_text = rotation_and_key_letters(rotation_number=args.number,key=args.key,text=text)
                with open(args.path,'w+') as nf:
                    nf.write(new_text)
                
                    print(f'Successfully decrypted text to {args.path}')

    except FileNotFoundError:
        print(f'Given path {args.path} or given text file {args.text} does not exist')
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()