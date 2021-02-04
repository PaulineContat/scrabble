def get_dico_file(file_name) :
    with open(file_name) as f:
        content = f.readlines()
        return [x.strip() for x in content] 

dico = get_dico_file("/Users/pcontat/Desktop/dico.txt")

lettres = input("Quelles sont tes lettres ? ").upper()
lettres_list = []
mots_faisables = []
mot = 0
d = {'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 'R':1, 'S':1, 'T':1, 'a':1, 'e':1 , 'i':1, 'o':1, 'u':1, 'l':1, 'n':1, 'r':1, 's':1, 't':1, 'D':2, 'G':2, 'd':2, 'g':2, 'B':3, 'C':3, 'M':3, 'P':3, 'b':3, 'c':3, 'm':3, 'p':3, 'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 'f':4, 'h':4, 'v':4, 'w':4, 'y':4, 'K':5, 'k':5, 'J':8, 'X':8, 'j':8, 'x':8, 'Q':10, 'Z':10, 'q':10, 'z':10}

for c in lettres :
    lettres_list += c

for mot in dico :
    # print("Test du mot",mot)
    lettres_list_copy = lettres_list.copy()
    j = 0
    k = 0

    while (j < len(mot) and k < len(lettres_list_copy)) :
        if mot[j] == lettres_list_copy[k] :
            j += 1
            del lettres_list_copy[k]
            k = 0
        else :
            k += 1

    if j == len(mot):
        mots_faisables.append(mot)     

# print(mots_faisables, " sont les mots faisables avec ces lettres ! Et son score est de ", score_mot)

def get_score(word):
    d = {'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 'R':1, 'S':1, 'T':1, 'a':1, 'e':1 , 'i':1, 'o':1, 'u':1, 'l':1, 'n':1, 'r':1, 's':1, 't':1, 'D':2, 'G':2, 'd':2, 'g':2, 'B':3, 'C':3, 'M':3, 'P':3, 'b':3, 'c':3, 'm':3, 'p':3, 'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 'f':4, 'h':4, 'v':4, 'w':4, 'y':4, 'K':5, 'k':5, 'J':8, 'X':8, 'j':8, 'x':8, 'Q':10, 'Z':10, 'q':10, 'z':10}
    score_mot = 0

    for c in word :
        score_mot = score_mot + d[c]
    return score_mot




if (len(mots_faisables) == 0):
    print("Non il n'y a pas de mot faisable : aaaaaaah domidommage ><' :'(")
else:
    print("Les mots faisables sont :")
    mots_faisables_dict = dict()
    for mot_faisable in mots_faisables:
        mots_faisables_dict[mot_faisable] = get_score(mot_faisable)
    mots_faisables_dict_tried = {k: v for k, v in sorted(mots_faisables_dict.items(), key=lambda item: item[1], reverse=True)}
    i=0
    for mots_faisables_dict_tried in mots_faisables_dict_tried :
        if i < 10 :
            print(mots_faisables_dict_tried, get_score(mots_faisables_dict_tried))
            i+=1
