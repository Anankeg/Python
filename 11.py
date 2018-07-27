def read_file():
    with open('filtered_words.txt', 'r') as file:
        # words = []
        # while True:
        #     word = file.readline()
        #     word = word.replace('\n', '')
        #     words.append(word)

        words = file.readlines()
        for word in words:
            # word = word.replace('\n', '')
            print(word.strip('\n'))
        # for word in words:
        #     print(word)
        print(words)
        print(len(words))
    return words


def de_word(words):
    flag = False
    new_word = input('请输入内容:')
    print(new_word)
    for word in words:
        # print(word)
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
    read_file()
    # de_word(read_file())
    # print('love' in 'love')