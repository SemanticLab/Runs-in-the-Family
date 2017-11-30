from bs4 import BeautifulSoup
import csv, lxml

# create empty list where links will be deposited
csv_list = []

def grab_links(page_html, link_list):
    page_html = BeautifulSoup(page_html, "lxml")
    page_html = page_html.find_all

    for x in page_html('a', href=True):
        if 'holdingsInfo' in x['href']:
            link_list.append(x)


with open("search_page1.htm") as results:
    grab_links(results, csv_list)

with open("search_page2.htm") as results2:
    grab_links(results2, csv_list)

with open("search_page3.htm") as results3:
    grab_links(results3, csv_list)

with open("search_page4.htm") as results4:
    grab_links(results4, csv_list)


with open("search_links.csv", 'w') as links_spreadsheet:
        # write each link in list to output file and add absolute url reference to make searchable
    for row in csv_list:
        links_spreadsheet.write('http://voyager.tcs.tulane.edu/vwebv/{0} \n'.format(row['href']))
