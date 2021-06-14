import os
from api import save_website
import sys

if __name__ == '__main__':
    url = 'https://www.baseball-reference.com'
    try:
        url = sys.argv[1]
    except IndexError:
        print("main.py expects some arguments")
        quit()
    download_folder = os.getcwd()
    project_name = url.replace('https://', '').replace('http://', '')

    kwargs = {'bypass_robots': True}

    save_website(url, download_folder, project_name, **kwargs)





#  scrapped


# from urllib.request import urlopen
# from selenium import webdriver

# def get_url_content(raw_url):
#     try:
#         content = urlopen(raw_url)
#     except:
#         options = webdriver.ChromeOptions()  # move to get url
#         options.add_argument('--headless')
#         options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
#         driver = webdriver.Chrome('../../upwork-1/chromedriver.exe', options=options)
#         driver.get(raw_url)
#         content = driver.page_source
#         driver.quit()
#     return content
#
# def script(url, page):
#     subFolder = url.replace('https://', "").replace('http://', "")
#     if not os.path.exists(subFolder):
#         os.mkdir(subFolder)
#     scripts = soup.find_all('script')
#     for tag in scripts:
#         try:
#             File = tag["src"]
#             page = page.replace(File, f"./{File.replace(':','_').replace('/','_').split('?')[0]}")
#             completeName = os.path.join(subFolder + f"/{File.replace(':','_').replace('/','_').split('?')[0]}")
#             r = requests.get(File, allow_redirects=True)
#             with open(completeName, 'w+') as sc:
#                 sc.write(r.text)
#         except:
#             print("no source")
#     css = soup.find_all('link')
#     for tag in css:
#         try:
#             File = tag["href"]
#             page = page.replace(File, f"./{File.replace(':','_').replace('/','_').split('?')[0]}")
#             completeName = os.path.join(subFolder + f"/{File.replace(':','_').replace('/','_').split('?')[0]}")
#             r = requests.get(File, allow_redirects=True)
#             with open(completeName, 'w+') as cs:
#                 cs.write(r.text)
#         except:
#             print("no source")
#     with open(os.path.join(subFolder + f"/{subFolder.replace('/', '_')}.html"), 'w+') as html:
#         html.write(page)
#     return page
#
#
#
# def get_url():
#     url = input("Website URL --->  ").lower()
#     url = 'https://' + url if not url.startswith('http') else url
#     return url
#
#
# def get_url_content(raw_url):
#     # try:
#     content = urlopen(raw_url)
#     # except:
#     #     driver = webdriver.Chrome('../upwork-1/chromedriver.exe', options=options)
#     #     driver.get(urlInput)
#     #     content = driver.page_source
#     #     driver.quit()
#     return content
#
#
# def create_resources(url):
#     """It creates a new resource inside a path, ignores if already exists"""
#     output_path = url.split('.')[1]
#     resources = url.split('.')[2].split('/')[1:]
#     for i in resources:
#         create_new_folder(output_path, i)
#
#
# def create_new_folder(output_path, folder_name):
#     """It creates a new folder inside a path, ignores if already exists"""
#     if not output_path:
#         output_path = os.getcwd()
#     if not os.path.exists(os.path.join(output_path, folder_name)):
#         os.mkdir(os.path.join(output_path, folder_name))
#
#
# if __name__ == "__main__":
#
#     # urlInput = get_url()
#     urlInput = 'https://home.frankspeech.com/'
#     options = webdriver.ChromeOptions()    # move to get url
#     options.add_argument('--headless')
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
#     driver = webdriver.Chrome('../upwork-1/chromedriver.exe', options=options)
#     driver.get(urlInput)
#     content = driver.page_source
#     driver.quit()
#     soup = BeautifulSoup(content, 'lxml')
#
#     tags = soup('a')
#     images = soup('img')
#     urls = set()
#     finalUrls = set()
#     content = script(urlInput, content)
#
#
#     for tag in tags:
#         urls.add(urljoin(urlInput, tag.get('href')))
#
#     for url in urls:
#         if re.match(urlInput, url):
#             finalUrls.add(url)
#     # for url in finalUrls:
#     #     if '/#' in url:    # skip jump to tags
#     #         continue
#     #     # create_resources(url)
#     #     try:
#     #         script(url)
#     #         css(url)
#     #         print("\n")
#     #     except:
#     #         print('none')