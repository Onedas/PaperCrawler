from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
import os


def get_cvpr_papers(years=2020, keyword=None):
	url = f'https://openaccess.thecvf.com/CVPR{years}'

	driver_path = 'chromedriver/chromedriver.exe'
	options = webdriver.ChromeOptions()
	options.add_argument('headless') # without window
	driver = webdriver.Chrome(driver_path, options=options)
	driver.get(url)

	os.makedirs('/SearchList', exist_ok = True)

	if keyword == None:
		for day in range(1,4):
			with open(f'SearchList/CVPR_{years}_day{day}.md', 'w', encoding = 'utf8') as f:
				# day click
				day_link = driver.find_element_by_partial_link_text(f'Day {day}')
				day_link.send_keys("\n")

				# title list
				titles = driver.find_elements_by_class_name('ptitle')
				for title in titles:
					# 링크 찾기
					paper_link = title.find_element_by_tag_name('a')
					# 새탭으로 열기
					paper_link.send_keys(Keys.CONTROL + '\n')
					# 탭 전환
					driver.switch_to.window(driver.window_handles[1])

					title = driver.find_element_by_id('papertitle').text
					abst = driver.find_element_by_id('abstract').text
					href = driver.find_element_by_link_text('pdf').get_attribute('href')
					driver.close()
					driver.switch_to.window(driver.window_handles[0])

					print(title)
					# write md
					f.write("### [{}]({})\n\n".format(title, href))
					f.write("#### Abstract\n\n")
					f.write("{}\n".format(abst))
					f.write("#### Summary\n\n")
					f.write('- task : \n- method : \n- data : \n')
					f.write("\n --- \n")

				# for next day
				driver.back()
		driver.quit()
	# if keyword exist
	else:
		# keyword 입력
		search_box = driver.find_element_by_tag_name('input')
		search_box.send_keys(f"{keyword}")
		search_box.send_keys('\n') #enter

		os.makedirs(f'SearchList/{keyword}', exist_ok = True)
		with open(f'SearchList/{keyword}/CVPR_{years:2}_{keyword}.md', 'w', encoding = 'utf8') as f:
			titles = driver.find_elements_by_class_name('ptitle')
			for title in titles:
				# 링크 찾기
				paper_link = title.find_element_by_tag_name('a')
				# 새탭으로 열기
				paper_link.send_keys(Keys.CONTROL + '\n')
				# 탭 전환
				driver.switch_to.window(driver.window_handles[1])

				title = driver.find_element_by_id('papertitle').text
				abst = driver.find_element_by_id('abstract').text
				href = driver.find_element_by_link_text('pdf').get_attribute('href')
				driver.close()
				driver.switch_to.window(driver.window_handles[0])

				print(title)
				# write md
				f.write("### [{}]({})\n".format(title, href))
				f.write("#### Abstract\n")
				f.write("{}\n".format(abst))
				f.write("#### Summary\n")
				f.write('- task : \n- method : \n- data : \n')
				f.write("\n --- \n")
		driver.quit()

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--years', help = "years", required = True)
	parser.add_argument('--keyword', help = 'keyword', default = None)
	args = parser.parse_args()

	get_cvpr_papers(args.years, args.keyword)