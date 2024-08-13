import random

from lexicon.lexicon_ru import LEXICON_RU


# Функция, возвращающая случайный выбор бота в игре
def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])


# Функция, возвращающая ключ из словаря, по которому
# хранится значение, передаваемое как аргумент - выбор пользователя 
def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            break
    return key


# Функция, определяющая победителя
def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    user_win = {'scissors_paper',
                'paper_rock',
                'rock_lizard',
                'lizard_spock',
                'spock_scissors',
                'scissors_lizard',
                'lizard_paper',
                'paper_spock',
                'spock_rock',
                'rock_scissors'}
    res_str = user_choice + '_' + bot_choice
    if user_choice == bot_choice:
        return 'nobody_won'
    elif res_str in user_win:
        return 'user_won'
    return 'bot_won'