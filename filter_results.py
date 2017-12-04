import json, re, csv


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
p2h = re.compile("[A-Z]\w+ \([A-Z]\w+\) Ba{0,1}[a,p,t]tiste")

p1x = re.compile("Ba{0,1}[a,p,t]tiste, [A-Z]\w\w+")
p2x = re.compile("[A-Z]\w+ Ba{0,1}[a,p,t]tiste")

last_name = re.compile("Ba{0,1}[a,p,t]tiste")
first_middle_name = re.compile(".+(?=\sBa{0,1}[a,p,t]tiste)")
suffix = re.compile("[J,S]r.")

formatted_first_middle_name = re.compile("(?<=tiste, )[A-Z].+")

the = re.compile("[T,t]he ")
shamarr = re.compile("Shamarr")
porter = re.compile("Porter")
kraig = re.compile("Kraig")
nemours = re.compile("Nemours")
raymond = re.compile("Raymond")
dwayne = re.compile("Dwayne")
clint = re.compile("Clint")

recording_list = []
all_formatted_names = []

data = json.load(open('musician_names.json'))
with open('batisteRecordingData.csv', 'w') as csv:

    csv.write('Information Resource, URL, Family Member Last Name, Family Member First Name, Recording Title, Author, Publication Date\n')

    for recording in data:
        names = []
        formatted_names = []
        batiste_info = recording['batiste info']
        for i in batiste_info:

            p1_results = p1.findall(i)
            if p1_results != None:
                for p1_result in p1_results:
                    names.append(p1_result)

            p1a_results = p1a.findall(i)
            if p1a_results != None:
                for p1a_result in p1a_results:
                    names.append(p1a_result)

            p1b_results = p1b.findall(i)
            if p1b_results != None:
                for p1b_result in p1b_results:
                    names.append(p1b_result)

            p2_results = p2.findall(i)
            if p2_results != None:
                for p2_result in p2_results:
                    names.append(p2_result)

            p2a_results = p2a.findall(i)
            if p2a_results != None:
                for p2a_result in p2a_results:
                    names.append(p2a_result)

            p2b_results = p2b.findall(i)
            if p2b_results != None:
                for p2b_result in p2b_results:
                    names.append(p2b_result)

            p2c_results = p2c.findall(i)
            if p2c_results != None:
                for p2c_result in p2c_results:
                    names.append(p2c_result)

            p2d_results = p2d.findall(i)
            if p2d_results != None:
                for p2d_result in p2d_results:
                    names.append(p2d_result)

            p2e_results = p2e.findall(i)
            if p2e_results != None:
                for p2e_result in p2e_results:
                    names.append(p2e_result)

            p2f_results = p2f.findall(i)
            if p2f_results != None:
                for p2f_result in p2f_results:
                    names.append(p2f_result)

            p2g_results = p2g.findall(i)
            if p2g_results != None:
                for p2g_result in p2g_results:
                    names.append(p2g_result)

            p2h_results = p2h.findall(i)
            if p2h_results != None:
                for p2h_result in p2h_results:
                    names.append(p2h_result)


            for name in names:
                name = re.sub('\"', '', name)

                p2x_results = p2x.search(name)

                the_result = the.search(name)
                shamarr_result = shamarr.search(name)
                porter_result = porter.search(name)
                kraig_result = kraig.search(name)
                nemours_result = nemours.search(name)
                raymond_result = raymond.search(name)
                dwayne_result = dwayne.search(name)
                clint_result = clint.search(name)

                if the_result == None:
                    if shamarr_result == None:
                        if porter_result == None:
                            if kraig_result == None:
                                if nemours_result == None:
                                    if raymond_result == None:
                                        if dwayne_result == None:
                                            if clint_result == None:

                                                if p2x_results != None:

                                                    last_name_result = last_name.search(name)
                                                    first_middle_name_result = first_middle_name.search(name)
                                                    suffix_result = suffix.search(name)

                                                    if suffix_result != None:
                                                        formatted_names.append("{0}, {1} {2}".format(last_name_result[0], first_middle_name_result[0], suffix_result[0]))
                                                    else:
                                                        formatted_names.append("{0}, {1}".format(last_name_result[0], first_middle_name_result[0]))

                                                else:
                                                    formatted_names.append(name)




        formatted_names = set(formatted_names)
        formatted_names = list(formatted_names)

        if formatted_names != []:
            recording['batiste names'] = formatted_names
            recording_list.append(recording)

            for formatted_name in formatted_names:

                csv_resource = "Hogan Jazz Archives"
                csv_url = "N/A"
                csv_last_name = "N/A"
                csv_first_name = "N/A"
                csv_title = "N/A"
                csv_author = "N/A"
                csv_publication_date = "N/A"

                csv_last_name_result = last_name.search(formatted_name)
                csv_first_middle_name_result = formatted_first_middle_name.search(formatted_name)
                csv_suffix_result = suffix.search(formatted_name)


                csv_url = recording['url']
                csv_last_name = csv_last_name_result[0]


                if csv_first_middle_name_result != None:
                    csv_first_name = csv_first_middle_name_result[0]
                #     if csv_suffix_result != None:
                #         csv_first_name = "{0} {1}".format(csv_first_middle_name_result[0], csv_suffix_result[0])
                #     else:
                #         csv_first_name = csv_first_middle_name_result[0]

                csv_title = recording['title']
                csv_title = re.sub('\n', '', csv_title)
                csv_title = re.sub(',', ' ', csv_title)
                csv_author = recording['authors']
                csv_author = re.sub(',', ' ', csv_author)
                csv_author = re.sub('\n', '', csv_author)
                csv_publication_date = recording['publication date']


                row = "{0}, {1}, {2}, {3}, {4}, {5}, {6}\n".format(csv_resource, csv_url, csv_last_name, csv_first_name, csv_title, csv_author, csv_publication_date)

                csv.write(row)



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
