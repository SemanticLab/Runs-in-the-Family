from bs4 import BeautifulSoup
import csv, lxml, itertools

with open("search_links.csv", 'w') as links_spreadsheet:
    with open("search_page1.htm") as results1:
        with open("search_page2.htm") as results2:

            soup1 = BeautifulSoup(results1, "lxml")
            soup2 = BeautifulSoup(results2, "lxml")
            links1 = soup1.find_all
            links2 = soup2.find_all
            super_links = itertools.chain(links1,links2)

            for link in super_links('a', href=True):
                if 'holdingsInfo?searchId=7&recCount=50&recPointer=' in link['href']:
                    links_spreadsheet.writelinks_spreadsheet.write('http://voyager.tcs.tulane.edu/vwebv/{0}, \n'.format(link['href']))


    #        for link2 in links2('a', href=True):
    #            if 'holdingsInfo?searchId=7&recCount=50&recPointer=' in link2['href']:
    #                prepared_links2 = ('http://voyager.tcs.tulane.edu/vwebv/{0}, \n'.format(link['href']))
    #                print(prepared_links2)
