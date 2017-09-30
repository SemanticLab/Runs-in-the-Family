from bs4 import BeautifulSoup
import csv, lxml

with open("search_links.csv", 'w') as links_spreadsheet:
    with open("search_page.htm") as results:


        soup = BeautifulSoup(results, "lxml")

        links = soup.find_all


        for link in links('a', href=True):
            if 'holdingsInfo?searchId=7&recCount=50&recPointer=' in link['href']:
                links_spreadsheet.write('http://voyager.tcs.tulane.edu/vwebv/{0}, \n'.format(link['href']))
