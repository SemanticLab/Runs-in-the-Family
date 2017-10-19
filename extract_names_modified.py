import bs4 as bs
import urllib.request
import csv
import json


with open('search_links.csv') as data:

    urls = csv.reader(data)

    all_data = []

    for url in urls:
        link = url[0]
        print("Working on",link)

        titles=[]
        authors=[]
        participant_performers=[]
        contents=[]
        other_authors=[]

        source = urllib.request.urlopen(link).read()
        soup = bs.BeautifulSoup(source, 'html.parser')

        for span in soup.find_all('span', id='Title:'):
            if span.text != None:
                titles.append(span.text)
            else:
                titles.append('N/A')
        for span in soup.find_all('span', id='Author:'):
            if 'tiste' in span.text:
                # I noticed the they are seperated with a double line break, so keep the names seperate by spliting the string on that and adding each one
                for a_author in span.text.split('\n\n'):
                    # not blank
                    if (a_author != ''):
                        authors.append(a_author)
            else:
                authors.append('N/A')
        for span in soup.find_all('span', id='Participant/Performer:'):
            if 'tiste' in span.text:
                participant_performers.append(span.text)
            else:
                participant_performers.append('N/A')
        for span in soup.find_all('span', id='Contents:'):
            if 'tiste' in span.text:
                contents.append(span.text)
            else:
                contents.append('N/A')
        for span in soup.find_all('span', id='Other Author(s):'):
            if 'tiste' in span.text:
                # I noticed the they are seperated with a double line break, so keep the names seperate by spliting the string on that and adding each one
                for a_other_author in span.text.split('\n\n'):
                    if a_other_author != '':
                        other_authors.append(a_other_author)
            else:
                other_authors.append('N/A')

        # add this to our list
        all_data.append({
            "url" : link,
            "titles": titles,
            "authors": authors,
            "participant_performers": participant_performers,
            "contents": contents,
            "other_authors": other_authors
            })

    json.dump(all_data, open('musician_names.json','w'), indent=4)

    # with open('musician_names.csv', 'w') as output:
    #     writer = csv.writer(output)

    #     rows = zip(title, authors, participant_performer, contents, other_authors)

    #     output.write('Title, Authors, Participant/Performer, Contents, Other_Authors,\n')
    #     for row in rows:
    #         writer.writerow(row)
