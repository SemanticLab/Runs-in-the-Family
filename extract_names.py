import bs4 as bs
import urllib.request
import csv, re, json

three_families_union = re.compile(' [B,b]a{0,1}[a,p,t]tiste')
four_digit_year = re.compile('[0-9]{4}')
discography_dict_list = []

authors = 'N/A'
# def find_the_batiste (html_content, output_list):
#     batiste_search = three_families_union.search(html_content)
#     if batiste_search != None:
#         output_list.append(html_content.text)
#     else:
#         output_list.append('N/A')

with open('search_links.csv') as data:

    urls = csv.reader(data)

    for url in urls:
        link = url[0]

        source = urllib.request.urlopen(link).read()
        soup = bs.BeautifulSoup(source, 'html.parser')

        batiste_info = []

        for span in soup.find_all('span', id='Title:'):
            title = span.text

            batiste_title = three_families_union.search(span.text)
            if batiste_title != None:
                batiste_info.append('title: {0}'.format(span.text))


        for span in soup.find_all('span', id='Author:'):
            authors = span.text

            batiste_author = three_families_union.search(span.text)
            if batiste_author != None:
                batiste_info.append('authors: {0}'.format(span.text))

        for span in soup.find_all('span', id='Participant/Performer:'):
            participants_performers = span.text

            batiste_participant_performer = three_families_union.search(span.text)
            if batiste_participant_performer != None:
                batiste_info.append('participants performers: {0}'.format(span.text))

        for span in soup.find_all('span', id='Contents:'):
            contents = span.text

            batiste_contents = three_families_union.search(span.text)
            if batiste_contents != None:
                batiste_info.append('contents: {0}'.format(span.text))

        for span in soup.find_all('span', id='Other Author(s):'):
            other_authors = span.text

            batiste_other_authors = three_families_union.search(span.text)
            if batiste_other_authors != None:
                batiste_info.append('other authors: {0}'.format(span.text))

        for span in soup.find_all('span', id='Published:'):
            published = span.text

            publication_date = four_digit_year.search(published)
            publication_date = int(publication_date[0])

        discography_dict = {'url': link,
        'title': title,
        'authors': authors,
        'publication date': publication_date,
        'participants performers': participants_performers,
        'contents': contents,
        'other authors': other_authors,
        'batiste info': batiste_info}

        print(discography_dict)

        discography_dict_list.append(discography_dict)

# disc_dict_list_dedupe = [dict(t) for t in set([tuple(d.items()) for d in discography_dict_list])]

json.dump(discography_dict_list, open('musician_names.json', 'w'), indent=4)

















    # with open('musician_names.csv', 'w') as output:
    #     writer = csv.writer(output)
    #
    #     rows = zip(title, authors, participants_performers, contents, other_authors)
    #
    #     output.write('Title, Authors, Participants/Performers, Contents, Other_Authors,\n')
    #     for row in rows:
    #         writer.writerow(row)
