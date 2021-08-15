# export class to convert txt file of subtitle string to csv file

import csv
from pathlib import Path


def export(inputfile, removeperps=True, outputfile=""):

    path = Path(
        "C:/Users/omido/Documents/GitHub/SubChiAI/SubChiAi/src/assets/subs")
    lines = ""

    # prepositions of english
    common_prepositions = "a the about above across after against among around at before behind below beside between by down during for from in inside into near of off on out over through to toward under up with"
    common_prepositions = common_prepositions.split()

    less_comman_prepositions = "aboard along amid as beneath beyond but concerning considering despite except following like minus next onto opposite outside past per plus regarding round save since than till underneath unlike until upon versus via within without"
    less_comman_prepositions = less_comman_prepositions.split()

    full_perps = common_prepositions+less_comman_prepositions

    input_path = path / inputfile
    # open source file and read data line by line
    with open(input_path) as f:
        for line in f:
            if not line.strip():
                continue  # skip the empty line
            lines += line
        lines = lines.replace("\n", " ")

    # seprate each word to list and number of repeats
    words = lines.split()  # list of words in a input string
    countdict = []
    for i in range(len(words)):
        countdict.append([words[i], lines.count(words[i])])

    words = countdict
    # remove duplicates
    res = []
    [res.append(x) for x in words if x not in res]

    # create index words for easier to use
    indexwords = []
    [indexwords.append(x[0]) for x in words]

    # remove junk words
    junk_list = []
    if removeperps == True:
        [junk_list.append(x) for x in indexwords if "[" in x and "]" in x or len(
            x) < 3 or x in full_perps]
        [words.remove(x) for x in words if x[0] in junk_list]

    # sort words by number of repeats
    words.sort(key=lambda x: x[1], reverse=True)

    # save final result into the csv file
    fields = ['words', 'repeats']

    out_path = Path(
        "C:/Users/omido/Documents/GitHub/SubChiAI/SubChiAi/src/assets/exported")
    if outputfile == "":
        outputfile = out_path / inputfile
    with open(outputfile, 'w') as f:

        # using csv.writer method from CSV package
        write = csv.writer(f)

        write.writerow(fields)
        write.writerows(words)
