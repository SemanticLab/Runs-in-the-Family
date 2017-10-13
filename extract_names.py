import bs4 as bs
import urllib.request
import csv


with open('search_links.csv') as data:

    urls = csv.reader(data)

    title = []
    authors = []
    participant_performer = []
    contents = []
    other_authors = []

    for url in urls:
        link = url[0]

        source = urllib.request.urlopen(link).read()
        soup = bs.BeautifulSoup(source, 'lxml')

        for span in soup.find_all('span', id='Title:'):
            if span.text != None:
                title.append(span.text)
            else:
                title.append('N/A')
        for span in soup.find_all('span', id='Author:'):
            if 'tiste' in span.text:
                authors.append(span.text)
            else:
                authors.append('N/A')
        for span in soup.find_all('span', id='Participant/Performer:'):
            if 'tiste' in span.text:
                participant_performer.append(span.text)
            else:
                participant_performer.append('N/A')
        for span in soup.find_all('span', id='Contents:'):
            if 'tiste' in span.text:
                contents.append(span.text)
            else:
                contents.append('N/A')
        for span in soup.find_all('span', id='Other Author(s):'):
            if 'tiste' in span.text:
                other_authors.append(span.text)
            else:
                other_authors.append('N/A')

    with open('musician_names.csv', 'w') as output:
        writer = csv.writer(output)

        rows = zip(title, authors, participant_performer, contents, other_authors)

        output.write('Title, Authors, Participant/Performer, Contents, Other_Authors,\n')
        for row in rows:
            writer.writerow(row)
