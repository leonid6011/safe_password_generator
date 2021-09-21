import random

def generate_password(len_of_password, chars):
    i = 0
    result = ''
    while i != len_of_password:
        result += random.choice(chars)
        i += 1
    return result

def exception(chars):
    i = 0
    result = ''
    while i != len(chars):
        if not chars[i] in 'il1Lo0O':
            result += chars[i]
        i += 1
    return result

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

print('Укажите количество паролей:')
nbr_of_password = int(input())
print('Укажите длину одного пароля:')
len_of_password = int(input())

print('Включать ли цифры 0123456789? Напишите: д (Да) / н (Нет)')
s = input().lower()
if s == 'д':
    chars += digits
print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Напишите: д (Да) / н (Нет)')
s = input().lower()
if s == 'д':
    chars += uppercase_letters
print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? Напишите: д (Да) / н (Нет)')
s = input().lower()
if s == 'д':
    chars += lowercase_letters
print('Включать ли символы !#$%&*+-=?@^_? Напишите: д (Да) / н (Нет)')
s = input().lower()
if s == 'д':
    chars += punctuation
print('Исключать ли неоднозначные символы il1Lo0O? Напишите: д (Да) / н (Нет)')
s = input().lower()
if s == 'д':
    chars = exception(chars)

i = 0
while i != nbr_of_password:
    print(generate_password(len_of_password, chars))
    i += 1
