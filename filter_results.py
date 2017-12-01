import json, re


p1 = re.compile("Ba{0,1}[a,p,t]tiste, [A-Z]\w\w+")
p1a = re.compile("Ba{0,1}[a,p,t]tiste, [A-Z]\w\w+ [A-Z]\w+")
p1b = re.compile("Ba{0,1}[a,p,t]tiste, [A-Z]\w\w+, [J,S]r.")

p2 = re.compile("[A-Z]\w+ Ba{0,1}[a,p,t]tiste")
p2a = re.compile("[A-Z]\w+ [A-Z]\w+ Ba{0,1}[a,p,t]tiste")
p2b = re.compile("[A-Z]\w+ Ba{0,1}[a,p,t]tiste, [J,S]r.")
p2c = re.compile("[A-Z]\w+ [A-Z]\. Ba{0,1}[a,p,t]tiste")
p2d = re.compile("[A-Z]\w+ [A-Z]\. Ba{0,1}[a,p,t]tiste, [J,S]r.")
p2e = re.compile('[A-Z]\w+ \\"[A-Z]\w+\\" Ba{0,1}[a,p,t]tiste')
p2f = re.compile('[A-Z]\w+ \\"[A-Z]\w+\\" Ba{0,1}[a,p,t]tiste, [J,S]r.')
p2g = re.compile("[A-Z]\. Ba{0,1}[a,p,t]tiste")

recording_list = []


data = json.load(open('musician_names.json'))

for recording in data:
    names = []
    batiste_info = recording['batiste info']
    for i in batiste_info:
        p1_results = p1.search(i)
        if p1_results != None:
            names.append(p1_results.group())

        p1a_results = p1a.search(i)
        if p1a_results != None:
            names.append(p1a_results.group())

        p1b_results = p1b.search(i)
        if p1b_results != None:
            names.append(p1b_results.group())

        p2_results = p2.search(i)
        if p2_results != None:
            names.append(p2_results.group())

        p2a_results = p2a.search(i)
        if p2a_results != None:
            names.append(p2a_results.group())

        p2b_results = p2b.search(i)
        if p2b_results != None:
            names.append(p2b_results.group())

        p2c_results = p2c.search(i)
        if p2c_results != None:
            names.append(p2c_results.group())

        p2d_results = p2d.search(i)
        if p2d_results != None:
            names.append(p2d_results.group())

        p2e_results = p2e.search(i)
        if p2e_results != None:
            names.append(p2e_results.group())

        p2f_results = p2f.search(i)
        if p2f_results != None:
            names.append(p2f_results.group())

        p2g_results = p2g.search(i)
        if p2g_results != None:
            names.append(p2g_results.group())

    recording['batiste names'] = names
    recording_list.append(recording)

json.dump(recording_list, open('musician_names_filtered.json', 'w'), indent=4)




#     for musicians in recording['other_authors']:
#         filter_oa = p_other_authors.findall(musicians)
#         for row in filter_oa:
#             if row != "":
#                 names.append(row)
#
#
#     for musician in recording['authors']:
#         filter_a = p_authors.findall(musician)
#         for row in filter_a:
#             if row != "":
#                 names.append(row)
#
#     for musician in recording['participant_performers']:
#         filter_pp = p_participant.findall(musician)
#         for row in filter_pp:
#             if row != "":
#                 names.append(row)
#
#
#
# reformat = re.compile("Batiste, \w+")
# proper_name_list = []
#
# mixed_name_list = set(names)
#
# for name in mixed_name_list:
#     first_last = p_participant.findall(name)
#     for name in first_last:
#         proper_name_list.append(name)
#
# for name in mixed_name_list:
#     last_first = reformat.findall(name)
#     for name in last_first:
#         split_name = name.split(", ")
#         reformat_name = split_name[1] + " " + split_name[0]
#         proper_name_list.append(reformat_name)
#
# names = sorted(set(proper_name_list))
#
# for name in names:
#     print(name)
