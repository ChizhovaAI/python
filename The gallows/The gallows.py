import random
word_list = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", "история", "женщина", "развитие", "власть", "правительство", "начальник", "спектакль", "автомобиль", "экономика", "литература", "граница", "магазин", "председатель", "сотрудник", "республика", "личность"]

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

def display_hangman(tries):
    stages = [
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    //
        |
        |  

        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    / 
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    \|
        |     |
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |     |
        |     |
        |     
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    
        |     
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     
        |    
        |       
        |  
        '''
    ]
    return stages[tries]
def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('Давайте играть в угадайку слов!')
    display_hangman(tries)
    print(word_completion)
    e = 0
    while (e!=3):
        e = input("Угадаешь слово целиком(1) или букву(2)? Для выхода нажми 3\n")
        if(e.isdigit()):
            e = int(e)
        else:
            print("Введи цифру")
        print(word_completion)
        if (e==1):
            sl = input("Напиши слово! ")
            if (sl.isalpha()):
                if (sl.upper()==word):
                    return (print('Поздравляем, ты угадал слово! Ты победил!\nКоличество попыток:', 6-tries))
                elif (sl.upper() in guessed_words):
                    print("Ты уже называл  это слово.")
                else:
                    print("Неа, пробуй дальше")
                    tries = tries-1
                    guessed_words.append(sl.upper())
                    print(display_hangman(tries))
                    if (tries==0):
                        return (print("Было загадано слово: ", word))
            else:
                print("Вводим только буквы!")
        if (e==2):
            sl = input("Буква: ")
            if (sl.isalpha()and len(sl)==1):
                count = 0
                if ((sl.upper() in word) and (sl.upper() not in guessed_letters)):
                    for i in range(len(word)):
                        if (word[i]==sl.upper()):
                            if (i==len(word)-1):
                                word_completion = word_completion[:i] + word[i]
                            else:
                                word_completion = word_completion[:i] + word[i] + word_completion[i + 1:]
                    guessed_letters.append(sl.upper())
                    print("Верно!!", word_completion)
                    if (word_completion == word):
                        return (print("Ты выйграл! Поздравляем!\nКоличество использованных попыток равно: ", 6-tries))
                elif (sl.upper() in guessed_letters):
                    print("Эта буква уже была введена!")
                else:
                    print("Этой буквы нет в слове.")
                    tries = tries - 1
                    guessed_letters.append(sl.upper())
                    print(display_hangman(tries))
                    if (tries==0):
                        return print(("Было загадано слово: ", word))
            else:
                print("Вводим только буквы! Буква должна быть одна!")


word = get_word(word_list)
play(word)
num = input('Хочешь сыграть еще? y/n или д/н\n')
while(num=='y' or num=='д'):
    word = get_word(word_list)
    play(word)
