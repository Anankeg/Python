def read_file():
    with open('filtered_words.txt', 'r') as file:
        words = []
        # words = file.readlines()
        for word in file.readlines():
            # word = word.replace('\n', '')
            word = str.replace(word, '\n', '')
            words.append(word)
        print(words)
        print(len(words))
    return words


def de_word(words):
    flag = False
    new_word = input('请输入内容:')
    print(new_word)
    for word in words:
        if word in new_word:
            flag = True
            print(flag)
            break
        else:
            print(flag)
            continue
    if flag:
        print('Freedom')
    else:
        print('Human Rights')


if __name__ == '__main__':
    # read_file()
    de_word(read_file())