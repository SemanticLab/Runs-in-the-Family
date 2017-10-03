from bs4 import BeautifulSoup
import csv, lxml

with open("search_links2.csv", 'w') as links_spreadsheet2:
    with open("search_page2.htm") as results:


        soup2 = BeautifulSoup(results, "lxml")

        links2 = soup2.find_all


        for link2 in links2('a', href=True):
            if 'holdingsInfo' in link2['href']:
                links_spreadsheet2.write('http://voyager.tcs.tulane.edu/vwebv/{0}, \n'.format(link2['href']))
