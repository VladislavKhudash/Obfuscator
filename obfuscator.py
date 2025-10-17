# CREATOR 
# NAME: Vladislav 
# SURNAME: Khudash  
# AGE: 17

# DATE: 06.09.2025
# APP: OBFUSCATOR_PYHTON_CODE
# TYPE: OBFUSCATOR
# VERSION: LATEST
# PLATFORM: ANY


# FOR ENCRYPTION OR DECRYPTION
#------------------------------#
PATTERN_LENGTH = 5
PATTERN_MAIN = '(?&$'
PATTERN_ANOTHER = '$&?)'
PATTERN_SYMBOLS = [' ', '\n', '\r', '\t', '\f', '\v', '=', '+', '-', '*', '/', '%', '<', '>', '^', '~', '&', '|', '!', '?', '@', '#', '$', ':', ';', '.', ',', '\\', '\'', '"', '`', '(', ')', '[', ']', '{', '}', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
PATTERN_PYHTON = [b'\x42\x0D\x0D\x0A', b'\x27\x0D\x0D\x0A', b'\x17\x0D\x0D\x0A', b'\xF3\x0D\x0D\x0A', b'\xEE\x0C\x0D\x0A', b'\x33\x0D\x0D\x0A', b'\x16\x0D\x0D\x0A', b'\x0D\x0D\x0D\x0A', b'\x03\xF3\x0D\x0A', b'\x03\xF3\x0D\x0A']
SYMBOLS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-.:;<=>?@[]^_{|}~'
SYMBOLS_HIDDEN = '0123456789abcdefABCDEF'
PATTERN_INIT = "__0000__=v0V0v(chr(0b1100010)+chr(0b1100001)+chr(0o163)+chr(0o145)+chr(0x36)+chr(0x34));__1972__=__0000__.b16decode;__1991__=__0000__.urlsafe_b64decode;__1994__=__0000__.b85decode;__2000__=__0000__.a85decode;__2008__=v0V0v(chr(0b1110000)+chr(0x69)+chr(0o143)+chr(0x6b)+chr(0b1101100)+chr(0o145)).loads;x000=v0V0v(chr(0x7a)+chr(0o154)+chr(0o151)+chr(0x62)).decompress;x0x0x0x0(x000(__2008__(__1972__(__300_000__))))"
ENCODINGS = [
    ('utf-8', 'utf-16', 'utf-32', 'cp866'),
    ('utf-32', 'chr(0b1110101)+chr(0o164)+chr(0x66)+chr(0x2d)+chr(0o63)+chr(0b110010)'),
    ('hz', 'chr(0o150)+chr(0b1111010)'),
    ('iso2022_jp', 'chr(0b1101001)+chr(0o163)+chr(0x6f)+chr(0x32)+chr(0o60)+chr(0b110010)+chr(0o62)+chr(0x5f)+chr(0b1101010)+chr(0x70)'),
    ('chr(0b1100111)+chr(0x7a)+chr(0o151)+chr(0o160)', 'chr(0x7a)+chr(0b1101100)+chr(0o151)+chr(0x62)')
]


from codecs import encode as cs_encode
from base64 import urlsafe_b64encode, b85encode, a85encode, b16encode
from gzip import compress as gzip_compress
from zlib import compress as zlib_compress
from lzma import compress as lzma_compress
from bz2 import compress as bz2_compress
from random import choice, randint
from pickle import dumps
from time import ctime
from threading import Thread
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo, showerror
from tkinter import Tk, Label, Button, Entry


def generator_symbols(length, pattern=SYMBOLS, hidden=False, mode=False):
    symbols = ''

    for _ in range(length): 
        if hidden:
            if mode:
                symbols += f'x00{choice(pattern)}' if choice([0, 1]) else 'x00'
            else:
                symbols += f'\\x00{choice(pattern)}' if choice([0, 1]) else '\\x00'
        else:
            if mode:
                symbols += f'{PATTERN_MAIN}{choice(pattern)}{choice(pattern)}{choice(pattern)}{choice(pattern)}{choice(pattern)}{choice(pattern)}{choice(pattern)}{choice(pattern)}{choice(pattern)}{choice(pattern)}' 
            else: 
                symbols += choice(pattern)

    return symbols


def generator_symbol():
    return str(choice(SYMBOLS_HIDDEN) if choice([0, 1]) else 0)


def encrypt_string(string):
    global session_symbols, PATTERN_SYMBOLS

    string = str(string)

    result = ''

    for n in string:
        if not n in session_symbols:
            PATTERN_SYMBOLS.append(n)
            session_symbols[n] = generator_symbols(PATTERN_LENGTH)

        if n in session_symbols:
            result += PATTERN_MAIN + session_symbols[n]
        else:
            result += PATTERN_ANOTHER + session_symbols[n]
    
    return result


def get_time(): 
    return ctime().split()[3]


def obfuscator(file_path):


    def x0(data):
        return bytes(n ^ key for n in data)   

    
    def encrypt_code(code):
        return bytes((b + key_code) % 256 for b in code.encode(ENCODINGS[0][0]))


    file_name = file_path[:file_path.rfind('.')] 
    file_extension = file_path.split('.')[-1]

    try:
        for _encoding in [
            'utf-8', 'utf-16', 'utf-32', 
            'iso-8859-1', 'iso-8859-5', 
            'cp866', 'cp1251', 'cp500', 
            'koi8-r', 
            'ascii'
        ]:
            try:
                with open(file_path, 'r', encoding=_encoding) as main_file: 
                    code = main_file.read()
            except: 
                if _encoding == 'ascii':
                    showerror('Obfuscator', f'This file cannot be obfuscated\n{file_path}')
                    return
                continue
            else: 
                break

        showinfo('Obfuscator', f'{get_time()}\nStarting to obfuscate this Python file\n{file_path}') 

        key_code = randint(1, 255)
        key = int(f'0x{generator_symbol()}{generator_symbol()}', base=16)
        function_decrypter = b16encode(dumps(zlib_compress("""                                                      
def x00(c_code,session_symbols,pattern_main,pattern_another):
    c_code,session_symbols,pattern_main,pattern_another,r_code=x0x(c_code,1),__2008__(__1991__(v0V0v(chr(0b1100010)+chr(0x7a)+chr(0o62)).decompress(session_symbols))),__2008__(__1994__(x000(pattern_main))),__2008__(__2000__(v0V0v(chr(0b1101100)+chr(0o172)+chr(0o155)+chr(0x61)).decompress(pattern_another))),''
    for n in c_code.split(pattern_main):
        symbol,*another_symbol=n.split(pattern_another)
        for sym in session_symbols.items():
            if sym[-1]==symbol:r_code+=sym[0];break
        if another_symbol:r_code+=''.join(another_symbol)
    exec(compile(r_code, '<string>', 'exec'),globals());return compile('exit(0)', '<string>', 'exec')
""".strip().encode(ENCODINGS[0][-1]), level=9))) 
        function_encrypt_encoding = cs_encode(f"__300_000__={function_decrypter};x00B={ENCODINGS[2][-1]};x00C={ENCODINGS[3][-1]}\ndef x0(data):return bytes(n^{key} for n in data)".encode(ENCODINGS[1][0]), 'uu')
        file_code = f"x0x0x0x0(x00('{cs_encode(encrypt_string(code), 'rot_13')}',{bz2_compress(urlsafe_b64encode(dumps(session_symbols)), compresslevel=9)},{zlib_compress(b85encode(dumps(PATTERN_MAIN)), level=9)},{lzma_compress(a85encode(dumps(PATTERN_ANOTHER)), preset=9)}))".encode(ENCODINGS[0][1])
        main_code = f"""x0x={choice(PATTERN_PYHTON)};x0x0x0x0=lambda:b'{generator_symbols(randint(1000, 2000), SYMBOLS_HIDDEN, hidden=True)}';x000x00x000x=lambda:b'{generator_symbols(randint(1000, 2000), mode=True)}';{generator_symbols(randint(10, 20), SYMBOLS_HIDDEN, mode=True, hidden=True)}=b'{generator_symbols(randint(10_000, 20_000), SYMBOLS_HIDDEN, hidden=True)}';x0=0x000{generator_symbol()};exec({f'v0V0v=__import__;x0x=lambda a,b:v0V0v(chr(0o143)+chr(0o157)+chr(0x64)+chr(0x65)+chr(0o143)+chr(0b1110011)).decode(a, chr(0b1110101)+chr(0x75) if b == 0 else chr(0x72)+chr(0x6f)+chr(0b1110100)+chr(0x5f)+chr(0o61)+chr(0b110011));x000x00x000x=compile(x0x("{cs_encode(PATTERN_INIT, 'rot_13')}",1), "<string>", "exec");x0x0x0x0=exec'.encode(ENCODINGS[1][0])}.decode({ENCODINGS[1][-1]}));x00B=0x0{generator_symbol()}B;x00C=0x0{generator_symbol()}C;x0x0x0x0(x0x({function_encrypt_encoding},0).decode({ENCODINGS[1][-1]})),'{generator_symbols(randint(10_000, 20_000), SYMBOLS_HIDDEN, hidden=True)}';x000=0x0{generator_symbol()};x0x0x0x0(x000x00x000x),""" + f"""'{generator_symbols(randint(10_000, 20_000))}',x0x0x0x0(x000({zlib_compress(file_code, level=9)}).decode(x0({x0(ENCODINGS[0][1].encode(ENCODINGS[3][0]))}).decode(x00C))),b'{generator_symbols(randint(10_000, 20_000), mode=True)}'"""

        with open(f'{file_name}-obfuscated.{file_extension}', 'w', encoding=ENCODINGS[0][0]) as obfuscated_py: 
            obfuscated_py.write(f"""_x0x0x_=eval({f"lambda code:bytes((b - {key_code}) % 256 for b in code).decode('{ENCODINGS[0][0]}')".encode(ENCODINGS[1][0])}.decode({ENCODINGS[1][-1]}));__PYTHON_CODE__={gzip_compress(zlib_compress(main_code.encode(ENCODINGS[0][0]), level=9), compresslevel=9)};__PYTHON_INIT__=eval(_x0x0x_({encrypt_code(f'lambda gz_code:__import__({ENCODINGS[-1][1]}).decompress(__import__({ENCODINGS[-1][0]}).decompress(gz_code))')}));exec(__PYTHON_INIT__(__PYTHON_CODE__))""")
            
        showinfo('Obfuscator', f'{get_time()}\nThis Python file has been successfully created\n{file_name}-obfuscated.{file_extension}')
    except BaseException as error: 
        showerror('Obfuscator', f'Why: An error occurred during obfuscation\nType: {type(error).__name__}\nDescription: {error}')


def get_python_file():
    global session_symbols, PATTERN_LENGTH, PATTERN_MAIN, PATTERN_ANOTHER

    file_path = askopenfilename()

    if file_path == '': 
        return
    
    try:
        if not file_path.split('.')[-1] in ['py', 'pyw']: 
            raise FileExistsError
    except AttributeError:
        return
    except:
        showerror('Obfuscator', f'This file is not a Python file\n{file_path}')
        return
    else:
        user_pattern_length = entry_pattern_length.get()
        user_pattern_main = entry_pattern_main.get()
        user_pattern_another = entry_pattern_another.get()

        if user_pattern_length.isdigit() and int(user_pattern_length) >= 2:
            PATTERN_LENGTH = int(user_pattern_length)
        else:
            showerror('Obfuscator', f'Incorrect PATTERN_LENGTH = {user_pattern_length}\n\nCorrect PATTERN_LENGTH = [2, ∞]')
            return
        
        if user_pattern_main != user_pattern_another and len(user_pattern_main) >= 4:
            PATTERN_MAIN = user_pattern_main
        else:
            showerror('Obfuscator', f'Incorrect PATTERN_MAIN = {user_pattern_main}\n\nCorrect PATTERN_MAIN != PATTERN_ANOTHER and len(PATTERN_MAIN) = [4, ∞]')
            return
        
        if user_pattern_another != user_pattern_main and len(user_pattern_another) >= 4:
            PATTERN_ANOTHER = user_pattern_another
        else: 
            showerror('Obfuscator', f'Incorrect PATTERN_ANOTHER = {user_pattern_another}\n\nCorrect PATTERN_ANOTHER != PATTERN_MAIN and len(PATTERN_ANOTHER) = [4, ∞]')
            return

        session_symbols = {}

        for symbol in PATTERN_SYMBOLS:
            session_symbols[symbol] = generator_symbols(PATTERN_LENGTH) 

        Thread(target=obfuscator, args=(file_path,), name=f'obfuscating_{file_path}').start()


def main():
    global entry_pattern_length, entry_pattern_main, entry_pattern_another

    root = Tk()
    root.title('Obfuscator')
    root.resizable(width=False, height=False)

    Label(root, text='PATTERN LENGTH', font=('Arial', 9, 'bold')).pack()
    entry_pattern_length = Entry(root, font=('Arial', 11))
    entry_pattern_length.insert(0, str(PATTERN_LENGTH))
    entry_pattern_length.pack()

    Label(root, text='PATTERN MAIN', font=('Arial', 9, 'bold')).pack()
    entry_pattern_main = Entry(root, font=('Arial', 11)) 
    entry_pattern_main.insert(0, PATTERN_MAIN)
    entry_pattern_main.pack()

    Label(root, text='PATTERN ANOTHER', font=('Arial', 9, 'bold')).pack()
    entry_pattern_another = Entry(root, font=('Arial', 11))
    entry_pattern_another.insert(0, PATTERN_ANOTHER)
    entry_pattern_another.pack()

    Button(root, text='OBFUSCATE', font=('Arial', 10, 'bold'), width=20, height=2, 
           activebackground='black', activeforeground='white', bd=3, command=get_python_file).pack()
    
    root.mainloop()


main()