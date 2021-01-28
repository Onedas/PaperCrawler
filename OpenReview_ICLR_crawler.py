from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
import os
import time


def get_iclr_papers(years = 2020, keyword = None):

    url = f'https://openreview.net/group?id=ICLR.cc/{years}/Conference'
    session_types = ['Oral', 'Spotlight', 'Poster']

    driver_path = 'chromedriver/chromedriver.exe'
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')  # without window
    driver = webdriver.Chrome(driver_path, options = options)
    os.makedirs('/SearchList', exist_ok = True)

    for session in session_types:
        driver.get(url)
        time.sleep(5)
        session_ = driver.find_element_by_partial_link_text(f'{session}')
        session_.click()
        time.sleep(3)

        papers = driver.find_elements_by_class_name('note')

        if keyword == None:
            with open(f'SearchList/ICLR_{years}_{session}.md', 'w', encoding='utf8') as f:

                for paper in papers:
                    paper = paper.find_elements_by_tag_name('a')[0]
                    title = paper.text

                    # new tab
                    paper.send_keys(Keys.CONTROL + '\n')
                    driver.switch_to.window(driver.window_handles[1])

                    # title = driver.find_element_by_class_name("note_content_title").text
                    href = driver.find_element_by_class_name("note_content_pdf").get_attribute('href')
                    abst = driver.find_elements_by_class_name('note_content_value')[3].text

                    print(title)
                    # write md
                    f.write("### [{}]({})\n".format(title, href))
                    f.write("#### Abstract\n")
                    f.write("{}\n".format(abst))
                    f.write("#### Summary\n")
                    f.write('- task : \n- method : \n- data : \n')
                    f.write("\n --- \n")

                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

        # keyword exist:
        else:
            os.makedirs(f'SearchList/{keyword}', exist_ok = True)
            with open(f'SearchList/{keyword}/ICLR_{years}_{session}.md', 'w', encoding = 'utf8') as f:
                for paper in papers:
                    paper = paper.find_elements_by_tag_name('a')[0]
                    title = paper.text

                    if keyword.lower() in title.lower():
                        # new tab
                        paper.send_keys(Keys.CONTROL + '\n')
                        driver.switch_to.window(driver.window_handles[1])

                        href = driver.find_element_by_class_name("note_content_pdf").get_attribute('href')
                        abst = driver.find_elements_by_class_name('note_content_value')[3].text

                        print(title)
                        # write md
                        f.write("### [{}]({})\n".format(title, href))
                        f.write("#### Abstract\n")
                        f.write("{}\n".format(abst))
                        f.write("#### Summary\n")
                        f.write('- task : \n- method : \n- data : \n')
                        f.write("\n --- \n")

                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
    driver.quit()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--years', help = "years", required = True)
    parser.add_argument('--keyword', help = 'keyword', default = None)
    args = parser.parse_args()

    get_iclr_papers(args.years, args.keyword)