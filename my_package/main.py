from math_utils import factorial, gcd
from string_utils import to_uppercase,strip_whitespace

def main():
    '''Тестування функцій з math_utils'''
    print("Факторіал 5:", factorial(5))
    print("НСВ 48 та 18:", gcd(48, 18))

    '''Тестування функцій з string_utils'''
    text = "Привіт Пайтон"
    print("У верхньому регистрі", to_uppercase(text))
    print("Після удаління пробілів", strip_whitespace(text))

if __name__ == "__main__":
     main()
