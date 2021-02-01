import requests
from bs4 import BeautifulSoup
import os
import argparse


def get_papers(url, keyword=None):
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, "html.parser")

    all = soup.find_all(attrs={"class":"ptitle"})

    if keyword is None:
        file_name = 'SearchList/ECCV.md'

    else:
        keyword = keyword.lower()
        os.makedirs(f'SearchList/{keyword}', exist_ok = True)
        file_name = f'SearchList/{keyword}/ECCV_{keyword}.md'

    count = 0
    with open(file_name, 'w', encoding = 'utf8') as f:
        for i, a_ in enumerate(all):
            title = a_.text.replace('\n', '')

            if keyword is not None:
                if keyword not in title.lower():
                    continue

            href = 'https://www.ecva.net/' + a_.find('a')['href']
            abstract = get_abstract(href)
            count += 1
            print(count, title)
            f.write("### [{}]({})\n\n".format(title, href))
            f.write("#### Abstract\n\n")
            f.write("{}\n".format(abstract))
            f.write("#### Summary\n\n")
            f.write('- task : \n- method : \n- data : \n')
            f.write("\n --- \n")


def get_abstract(paper_url):
    webpage = requests.get(paper_url)
    soup = BeautifulSoup(webpage.content, "html.parser")
    abstract = soup.find(attrs={"id":"abstract"})
    return abstract.text


if __name__ == '__main__':
    url = "https://www.ecva.net/papers.php"

    parser = argparse.ArgumentParser()
    parser.add_argument('--keyword', help = 'keyword', default = None)
    args = parser.parse_args()

    get_papers(url, args.keyword)
