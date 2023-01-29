

def coder_func(message, switch):

    alfavite = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = ''


    for char in message:

        if char == ' ':
            result += " "

        for j in alfavite:
            if j == char:

                place = alfavite.find(char)
                new_place = place + switch
                result += alfavite[new_place]
                break

            elif j == char.upper():
                place = alfavite.find(char.upper())
                new_place = place + switch
                result += alfavite[new_place].lower()
                break

    print(result)


def decoder_func(message, switch):

    alfavite = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = ''


    for char in message:

        if char == ' ':
            result += " "

        for j in alfavite:
            if j == char:

                place = alfavite.find(char)
                new_place = place - switch
                result += alfavite[new_place]
                break

            elif j == char.upper():
                place = alfavite.find(char.upper())
                new_place = place - switch
                result += alfavite[new_place].lower()
                break

    print(result)




coder_func("где нам нужно просто поменять знак?", 3)
decoder_func("ёжз ргп рцйрс тусфхс тспзрвхя кргн?", 3)

