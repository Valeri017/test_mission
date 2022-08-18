
def is_correct_brackets(text) -> bool:
    
    while '()' in text:
        text = text.replace('()', '')
    return not text


if __name__ == '__main__':
    print(is_correct_brackets('((())))))((())()()()(())'))
    print(is_correct_brackets('(())'))
