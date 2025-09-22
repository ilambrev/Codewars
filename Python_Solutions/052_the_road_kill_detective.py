from preloaded import ANIMALS

# ANIMALS = ['hyena', 'penguin', 'bear', 'baboon', 'squirrel',
#            'aardvark', 'rabbit', 'parrot', 'gibbon', 'killerwhale',
#            'quokka', 'quoll', 'giraffe', 'jellyfish',
#            'reindeer', 'alligator', 'hippopotamus', 'otter']

def road_kill(photo):
    def is_animal_name_found(animal, letters):
        if len([letter for letter in letters if not letter in animal]) > 0:
            return False

        start_index = 0
        is_name_found = True

        for i in range(len(animal)):
            letter = animal[i]
            is_letter_found = False

            for j in range(start_index, len(letters)):
                if letter == letters[j]:
                    start_index = j + 1
                    is_letter_found = True
                    break
                elif not letters[j] == animal[i - 1]:
                    is_letter_found = False
                    break

            if not is_letter_found:
                is_name_found = False
                break

        return is_name_found

    animal_name = '??'

    letters = [letter for letter in photo if not letter == '=']

    if not letters:
        return animal_name

    for animal in ANIMALS:
        if is_animal_name_found(animal, letters):
            animal_name = animal
        elif is_animal_name_found(animal[::-1], letters):
            animal_name = animal

    return animal_name

# print(road_kill("==========h===yyyyyy===eeee=n==a========"))  # "hyena"
# print(road_kill("======pe====nnnnnn=======================n=n=ng====u==iiii=iii==nn========================n="))  # "penguin"
# print(road_kill("=====r=rrr=rra=====eee======bb====b======="))  # "bear"
# print(road_kill("===g=eccc==kkkooBo="))  # "??"
# print(road_kill("===d==o=ggBg="))  # '??'
# print(road_kill("===b=b==========a=a=a=a=a=a=a=boo======n====="))  # "baboon"
# print(road_kill("====l===e===r=======riuqs====="))  # "squirrel"
# print(road_kill("=====k====r=a=vvvv==d=d=d=d=r==a=a======="))  # "aardvark"
# print(road_kill("====rraabbiitt=="))  # "rabbit"
# print(road_kill("ppp=aaaaa===rrr===rrr===o=t="))  # "parrot"
# print(road_kill("ggggg==iiii==b=bbbbb===oooo=nnn==="))  # "gibbon"
# print(road_kill("kkkkk==i=lllll===llll=eeee=rrrrwwwhhhhh=aaaa===llee==="))  # "killerwhale"
# print(road_kill("===qqqqquuu===oooo===k=kkkkk==aa"))  # "quokka"
# print(road_kill("=pppp=aaaa===rrrrr=rrrr===o==ttt==="))  # "parrot"
# print(road_kill("==q==uuuuooooo==ll==llll=="))  # "quoll"
# print(road_kill("=ggggg==iiiii==rrr==afff==f===eeeee="))  # "giraffe"
# print(road_kill("===aaaa=a=rrrddddd=vvvvv=aa===rrkkkk==="))  # "aardvark"
# print(road_kill("===qqqq==uo==lllll=ll="))  # "quoll"
# print(road_kill("jjj===e=lll==lllll===yff==i==sssssh"))  # "jellyfish"
# print(road_kill("===rr===eeee=ii==n=dee===e==rrrrr=="))  # "reindeer"
# print(road_kill("==aaaa==lllllli==ggggg=aa==ttttt===o=r==="))  # "alligator"
# print(road_kill("===ssssqqq===uuuiiiii===rrr==rrrr===eeeee==lllll="))  # "squirrel"
# print(road_kill("rrr===e==i==nnnnn=dd===ee===e==rrr=="))  # "reindeer"
# print(road_kill("==hhhh=iippppp==pppp===oo===pppp==ooooo==ttttt=aaaaa==m=uuuuu=sss=="))  # "hippopotamus"
# print(road_kill("===oottt==tt===errr==="))  # "otter"
# print(road_kill("==rr==eee=iiii===nnnnn==d===eeeeeeerrrrr==="))  # "reindeer"
# print(road_kill("=quuuuu=ooollll==lllll="))  # "quoll"
# print(road_kill("jjj===eeeelllll===llyyyyy===ffff===ii==ssss==hhh="))  # "jellyfish"
# print(road_kill("==gggg=iiiiirrrr===aaaaaff==fffeee"))  # "giraffe"
# print(road_kill("r===aa===bbbb==bbbbb==iiii===tttt="))  # "rabbit"
# print(road_kill("=a===aaaa=rr=d===vv===aaaa==rrkkk="))  # "aardvark"
# print(road_kill("==hhhhh==iiiipp==ppppp===oooo=ppp=ooo==ttttt===a===mmm=uuuuus"))  # "hippopotamus"
# print(road_kill("=b==aaaaabb===oooo===o=nnnnn"))  # "baboon"
# print(road_kill("==reiii=nndd=eeee==eeerrrr"))  # "reindeer"