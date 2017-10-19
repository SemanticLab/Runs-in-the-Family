import json, re


p_other_authors = re.compile("Batiste, \w+")
p_authors = re.compile("Batiste, \w.+\.")
p_participant = re.compile("\w+ Batiste")

names = []

data = json.load(open('musician_names.json'))

for recording in data:

    for musicians in recording['other_authors']:
        filter_oa = p_other_authors.findall(musicians)
        for row in filter_oa:
            if row != "":
                names.append(row)


    for musician in recording['authors']:
        filter_a = p_authors.findall(musician)
        for row in filter_a:
            if row != "":
                names.append(row)

    for musician in recording['participant_performers']:
        filter_pp = p_participant.findall(musician)
        for row in filter_pp:
            if row != "":
                names.append(row)



reformat = re.compile("Batiste, \w+")
proper_name_list = []

mixed_name_list = set(names)

for name in mixed_name_list:
    first_last = p_participant.findall(name)
    for name in first_last:
        proper_name_list.append(name)

for name in mixed_name_list:
    last_first = reformat.findall(name)
    for name in last_first:
        split_name = name.split(", ")
        reformat_name = split_name[1] + " " + split_name[0]
        proper_name_list.append(reformat_name)

names = sorted(set(proper_name_list))

for name in names:
    print(name)
