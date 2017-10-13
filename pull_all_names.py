from bs4 import BeautifulSoup
import csv, lxml

# create empty list where links will be deposited
csv_list = []

# open csv output file and two html input files
with open("search_links.csv", 'w') as links_spreadsheet:
    with open("search_page1.htm") as results:
        with open("search_page2.htm") as results2:

            # parse html docs and create vars for results
            soup1 = BeautifulSoup(results, "lxml")
            soup2 = BeautifulSoup(results2, "lxml")
            links1 = soup1.find_all
            links2 = soup2.find_all

            # grab all links and place in list
            for link1 in links1('a', href=True):
                if 'holdingsInfo' in link1['href']:
                    csv_list.append(link1)

            for link2 in links2('a', href=True):
                if 'holdingsInfo' in link2['href']:
                    csv_list.append(link2)

    # write each link in list to output file and add absolute url reference to make searchable
    for row in csv_list:
        links_spreadsheet.write('http://voyager.tcs.tulane.edu/vwebv/{0}, \n'.format(row['href']))
