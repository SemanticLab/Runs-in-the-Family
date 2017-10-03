from bs4 import BeautifulSoup
import csv, lxml

with open("search_links1.csv", 'w') as links_spreadsheet1:
    with open("search_page1.htm") as results:


        soup1 = BeautifulSoup(results, "lxml")

        links1 = soup1.find_all


        for link1 in links1('a', href=True):
            if 'holdingsInfo' in link1['href']:
                links_spreadsheet1.write('http://voyager.tcs.tulane.edu/vwebv/{0}, \n'.format(link1['href']))
