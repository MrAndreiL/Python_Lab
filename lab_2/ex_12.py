def is_rhyme(cuv1, cuv2):
    return (cuv1[len(cuv1) - 1] == cuv2[len(cuv2) - 1] and
            cuv1[len(cuv1) - 2] == cuv2[len(cuv2) - 2])

def get_rhymes(lista_cuvinte):
    result = []

    for word in lista_cuvinte:
        if len(result) == 0:
            result.append(word)
        else:
            gasit = False 
            for rhyme in result:
                if is_rhyme(word[0], rhyme[0]):
                    rhyme.append(word[0])
                    gasit = True
                    break
            if gasit == False:
                result.append(word)
    return result


def main():
    print(get_rhymes([['ana'], ['banana'], ['carte'], ['arme'], ['parte']]))

if __name__ == "__main__":
    main()
