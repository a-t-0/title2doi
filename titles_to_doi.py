# pip install habanero
from habanero import Crossref
import re


def titletodoi(keyword):
    cr = Crossref()
    result = cr.works(query=keyword)
    items = result["message"]["items"]
    item_title = items[0]["title"]
    tmp = ""
    for it in item_title:
        tmp += it
    title = keyword.replace(" ", "").lower()
    title = re.sub(r"\W", "", title)
    # print('title: ' + title)
    tmp = tmp.replace(" ", "").lower()
    tmp = re.sub(r"\W", "", tmp)
    # print('tmp: ' + tmp)
    if title == tmp:
        doi = items[0]["DOI"]
        return doi
    else:
        return None


def get_dois(titles):
    dois = []
    for title in titles:
        try:
            doi = titletodoi(title)
            print(f"doi={doi}, title={title}")
            if not doi is None:
                dois.append(doi)
        except:
            pass
            # print("An exception occurred")
    print(f"dois={dois}")
    return dois


def read_titles_from_file(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()
    split_lines = splits_lines(lines)
    return split_lines


def splits_lines(lines):
    split_lines = []
    for line in lines:
        new_lines = line.split(";")
        for new_line in new_lines:
            split_lines.append(new_line)
    return split_lines


def write_dois_to_file(dois, filename, separation_char):
    textfile = open(filename, "w")
    for doi in dois:
        textfile.write(doi + separation_char)
    textfile.close()


filepath = "list_of_titles.txt"
titles = read_titles_from_file(filepath)
dois = get_dois(titles)
write_dois_to_file(dois, "dois_space.txt", " ")
write_dois_to_file(dois, "dois_per_line.txt", "\n")
