from string import ascii_uppercase
from string import ascii_letters

l = ['\n','\t'] + list(chr(i) for i in range(32,127))
#96
d1 = {y:x for x,y in enumerate(l)}
d2 = {x:y for x,y in enumerate(l)}

d1_uppercase = {y:x for x,y in enumerate(ascii_uppercase)}
d2_uppercase = {x:y for x,y in enumerate(ascii_uppercase)}

d1_letters = {y:x for x,y in enumerate(sorted(ascii_letters))}
d2_letters = {x:y for x,y in enumerate(sorted(ascii_letters))}

def test(text: str) -> str:
    for i in text:
        if i not in d2.values():
            raise ValueError(f'Text value |{i}| does not match the base for encryption')

def test_uppercase(text: str) -> str:
    for i in text:
        if i not in d2_uppercase.values():
            raise ValueError(f'Text value |{i}| does not match the base for encryption upper_case')
        
def test_letters(text: str) -> str:
    for i in text:
        if i not in d2_letters.values():
            raise ValueError(f'Text value |{i}| does not match the base for encryption letters_only')

def test_key(text: str) -> str:
    for i in text:
        if i not in d2.values():
            raise ValueError(f'Key value |{i}| does not match the base for encryption')

def test_uppercase_key(text: str) -> str:
    for i in text:
        if i not in d2_uppercase.values():
            raise ValueError(f'Key value |{i}| does not match the base for encryption upper_case')
        
def test_letters_key(text: str) -> str:
    for i in text:
        if i not in d2_letters.values():
            raise ValueError(f'Key value |{i}| does not match the base for encryption letters_only')

def rotation_decrypt(rotation_number: int,text: str) -> str:
    '''
    Function to decrypt text with rotation number.
    '''
    new_text = ''
    for i in text:
        m = d1[i]
        m -= rotation_number
        while m < 0:
            m += 97

        new_text += d2[m]
    
    return new_text

def key_decrypt(key: str,text: str) -> str:
    '''
    Function to decrypt text with a key.
    '''
    new_text = ''
    j = len(text) - len(key) - 1
    while j >= len(key):
        j -= len(key)

    j = key.index(key[j])
    for i in text[::-1]:
        if j < 0:
            j = len(key) - 1
        
        n = d1[i]
        n -= d1[key[j]]
        while n < 0:
            n += 97

        new_text += d2[n]
        j -= 1

    return new_text[::-1] 

def rotation_and_key(rotation_number: int,key: str,text: str) -> str:
    '''
    Function to decrypt text when rotation number and key both are included.
    If key is long enough,rotation will not be used.
    '''
    new_text = ''
    flag = True
    k = len(key) - 1
    if len(text) - len(key) <= 0:
        flag = False
        k = len(text) - len(key) - 1
        k = key.index(key[k])

    m = len(text) - len(key)
    for i in text[::-1]:
        if m <= 0:
            flag = False
        
        if flag:
            j = d1[i]
            j -= rotation_number
            while j < 0:
                j += 97
            
            new_text += d2[j]
            m -= 1
            continue
        
        j = d1[i]
        j -= d1[key[k]]
        while j < 0:
            j += 97
        
        new_text += d2[j]
        k -= 1
    
    return new_text[::-1]

def rotation_decrypt_uppercase(rotation_number: int,text: str) -> str:
    '''
    Function to decrypt text with rotation number.
    Decryption is done by uppercase letters.
    '''
    new_text = ''
    for i in text:
        m = d1_uppercase[i]
        m -= rotation_number
        while m < 0:
            m += 26
        
        new_text += d2_uppercase[m]
    
    return new_text

def key_decrypt_uppercase(key: str,text: str) -> str:
    '''
    Function to decrypt text with a key.
    Decryption is done by uppercase letters.
    '''
    new_text = ''
    j = len(text) - len(key) - 1
    while j >= len(key):
        j -= len(key)

    j = key.index(key[j])
    for i in text[::-1]:
        if j < 0:
            j = len(key) - 1
        
        n = d1_uppercase[i]
        n -= d1_uppercase[key[j]]
        while n < 0:
            n += 26

        new_text += d2_uppercase[n]
        j -= 1

    return new_text[::-1]

def rotation_and_key_uppercase(rotation_number: int,key: str,text: str) -> str:
    '''
    Function to decrypt text when rotation number and key both are included.
    If key is long enough,rotation will not be used.
    Decryption is done by uppercase letters.
    '''
    new_text = ''
    flag = True
    k = len(key) - 1
    if len(text) - len(key) <= 0:
        flag = False
        k = len(text) - len(key) - 1
        k = key.index(key[k])

    m = len(text) - len(key)
    for i in text[::-1]:
        if m <= 0:
            flag = False
        
        if flag:
            j = d1_uppercase[i]
            j -= rotation_number
            while j < 0:
                j += 26
            
            new_text += d2_uppercase[j]
            m -= 1
            continue
        
        j = d1_uppercase[i]
        j -= d1_uppercase[key[k]]
        while j < 0:
            j += 26
        
        new_text += d2_uppercase[j]
        k -= 1
    
    return new_text[::-1]

def rotation_decrypt_letters(rotation_number: int,text: str) -> str:
    '''
    Function to decrypt text with rotation number.
    Decryption is done by only letters.
    '''
    new_text = ''
    for i in text:
        m = d1_letters[i]
        m -= rotation_number
        while m < 0:
            m += 52

        new_text += d2_letters[m]
    
    return new_text

def key_decrypt_letters(key: str,text: str) -> str:
    '''
    Function to decrypt text with a key.
    Decryption is done by only letters.
    '''
    new_text = ''
    j = len(text) - len(key) - 1
    while j >= len(key):
        j -= len(key)

    j = key.index(key[j])
    for i in text[::-1]:
        if j < 0:
            j = len(key) - 1
        
        n = d1_letters[i]
        n -= d1_letters[key[j]]
        while n < 0:
            n += 52

        new_text += d2_letters[n]
        j -= 1

    return new_text[::-1]

def rotation_and_key_letters(rotation_number: int,key: str,text: str) -> str:
    '''
    Function to decrypt text when rotation number and key both are included.
    If key is long enough,rotation will not be used.
    Decryption is done by only letters.
    '''
    new_text = ''
    flag = True
    k = len(key) - 1
    if len(text) - len(key) <= 0:
        flag = False
        k = len(text) - len(key) - 1
        k = key.index(key[k])

    m = len(text) - len(key)
    for i in text[::-1]:
        if m <= 0:
            flag = False
        
        if flag:
            j = d1_letters[i]
            j -= rotation_number
            while j < 0:
                j += 52
            
            new_text += d2_letters[j]
            m -= 1
            continue
        
        j = d1_letters[i]
        j -= d1_letters[key[k]]
        while j < 0:
            j += 52
        
        new_text += d2_letters[j]
        k -= 1
    
    return new_text[::-1]