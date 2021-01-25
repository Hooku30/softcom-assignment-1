import requests
import bs4
import os
import lxml
import textwrap

# location and name of folders
location = r"C:\Users\sivis\OneDrive\Desktop"
directories = ["India", "World", "Business", "Homepage"]

# creating all four folders
for _ in range(len(directories)):
    path = os.path.join(location, directories[_])
    os.mkdir(path)

# Link of all folders
link_arr = [r"https://timesofindia.indiatimes.com/india",
            r"https://timesofindia.indiatimes.com/world",
            r"https://timesofindia.indiatimes.com/business",
            r"https://timesofindia.indiatimes.com/"]

# loop for all four folders
for i in range(len(link_arr)):

    # creating array for link storing for further purpose
    link_collect = []

    # finding links of news
    web_link = link_arr[i]
    req = requests.get(web_link)
    soup = bs4.BeautifulSoup(req.text, 'lxml')

    link_all = []
    link_all = soup.find('div', {'class': ['main-content', 'content', 'latestNewContainer']})
    if link_all is not None:
        link_all = link_all.find_all('span', {'class': ['w_tle']})
    Other = soup.find('ul', class_=['wrapper clearfix', 'top-story', 'list8', 'list9', 'latestNewContainer'])
    if Other is not None:
        Others = Other.find_all('li')
        for items in Others:
            link_all.append(items)

    # putting in link_collect
    if len(link_all) > 0:
        for j in range(len(link_all)):
            if link_all[j] is not None:
                link = link_all[j].find('a').get('href')
                if link[0:4] != "http":
                    link_collect.append(r"https://timesofindia.indiatimes.com/" + link)
                else:
                    link_collect.append(link)

        # loop for date para and title for valid links
        count = 0
        for k in range(len(link_collect)):
            rq = requests.get(link_collect[k])
            soup2 = bs4.BeautifulSoup(rq.text, 'lxml')
            # for the links which doesn't have videos in it
            if (link_collect[k])[38] != 'v':
                title = soup2.find('div', class_='_2NFXP')
                if title is not None:
                    # making file to store information
                    path_new = os.path.join(location, directories[i])
                    file = f"{count + 1}.txt"

                    # extracting title
                    title = title.find('h1').getText()

                    # extracting date
                    date = soup2.find('div', class_='_3Mkg- byline')
                    date = date.getText()
                    x = len(date)
                    date = date[x - 24:x]

                    # extracting para
                    para = soup2.find('div', class_='ga-headlines')
                    para = para.getText()

                    # wrapping the text of para
                    wrapper = textwrap.TextWrapper(width=130)
                    string = wrapper.fill(text=para)

                    # here in open first argument is filename along with location to save file there
                    # encoding used to tackle errors
                    with open(os.path.join(path_new, file), 'w', encoding='utf-8') as fp:
                        fp.write("Title : ")
                        fp.write("\n")
                        fp.write(title)
                        fp.write("\n")
                        fp.write("\n")
                        fp.write("\n")
                        fp.write("Link :")
                        fp.write("\n")
                        fp.write(link_collect[k])
                        fp.write("\n")
                        fp.write("\n")
                        fp.write("\n")
                        fp.write("Date and time: ")
                        fp.write("\n")
                        fp.write(date)
                        fp.write("\n")
                        fp.write("\n")
                        fp.write("\n")
                        fp.write("Paragraph: ")
                        fp.write("\n")
                        fp.write(string)
                        fp.write("\n")
                        fp.write("\n")
                        fp.write("\n")
                    count += 1

            # for the case when inside the link videos is there
            else:
                if title is not None:
                    title = soup2.find('div', class_='_2GHni')

                    # extracting title
                    title = title.find('h1').getText()

                    # extracting date
                    date = soup2.find('div', class_='_3Mkg- byline')
                    date = date.getText()
                    x = len(date)
                    date = date[x - 24:x]

                    # extracting para
                    para = soup2.find('div', class_='ga-headlines')
                    para = para.getText()

                    # wrapping the text of para
                    wrapper = textwrap.TextWrapper(width=130)
                    string = wrapper.fill(text=para)

                    # here in open first argument is filename along with location to save file there
                    # encoding used to tackle errors
                    with open(os.path.join(path_new, file), 'w', encoding='utf-8') as fp:
                        fp.write("Title : ")
                        fp.write("\n")
                        fp.write(title)
                        fp.write("\n")
                        fp.write("\n")
                        fp.write("\n")
                        fp.write("Link :")
                        fp.write("\n")
                        fp.write(link_collect[k])
                        fp.write("\n")
                        fp.write("\n")
                        fp.write("\n")
                        fp.write("Date and time: ")
                        fp.write("\n")
                        fp.write(date)
                        fp.write("\n")
                        fp.write("\n")
                        fp.write("\n")
                        fp.write("Paragraph: ")
                        fp.write("\n")
                        fp.write(string)
                        fp.write("\n")
                        fp.write("\n")
                        fp.write("\n")
                    count += 1
