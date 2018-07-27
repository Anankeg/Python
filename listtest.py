
list1 = ["领导\n", 'anbu\n', '李大钊\n']
list2 = []
for l in list1:
    print(l)
    string = l.replace("\n", "")
    print(string)
    list2.append(string)
print(list2)
