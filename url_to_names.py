from urllib.request import urlopen
import bs4 as BeautifulSoup
import lxml

with open('pages.html', 'w') as output:
    with open('search_links.csv') as urls:
        for url in urls:
            response = urlopen(url)
            html = response.read()
            soup = BeautifulSoup.BeautifulSoup(html, 'html.parser')
            bib_data = soup.find_all(attrs={'class': 'bibliographicData'})

            print(bib_data)



#            for batiste in soup('a', href=True):

#                print(batiste)



    #    soup1 = BeautifulSoup(results, "lxml")

    #    links1 = soup1.find_all


    #    for link1 in links1('a', href=True):
    #        if 'holdingsInfo' in link1['href']:
    #            links_spreadsheet1.write('http://voyager.tcs.tulane.edu/vwebv/{0}, \n'.format(link1['href']))



        #    for link2 in links2('a', href=True):
        #        if 'holdingsInfo' in link2['href']:
        #            links_spreadsheet2.write('http://voyager.tcs.tulane.edu/vwebv/{0}, \n'.format(link2['href']))