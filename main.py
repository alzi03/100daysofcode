import requests
from bs4 import BeautifulSoup

# grabs html contents
request = requests.get(url='https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
text = request.text
soup = BeautifulSoup(text, 'html.parser')

# printer = soup.prettify() --> copied over to text.html

# plan to add years, need to account for missing years
titles = [i.string.rstrip() for i in soup.find_all('h3', class_='title')[::-1]]
descr = [i.p.text for i in soup.find_all('p', class_='description')[::-1]]

# gets rid of years
for i in range(len(descr)):
    try:
        if int(descr[i][0]) > 0:
            descr[i] = descr[i][4:]
    except:
        continue

movies = dict()

n = 0
while n != 100:
    if n < 10:
        movies[n+1] = {'Name': titles[n][3:],
                    #'Year Made': years[n-1], --> Need to debug and find a better route to this, since some are empty
                    'Description': descr[n]}
    elif n <= 100:
        movies[n + 1] = {'Name': titles[n][4:],
                         # 'Year Made': years[n-1], --> Need to debug and find a better route to this, since some are empty
                         'Description': descr[n]}

    n += 1

# for i, v in movies.items():
    # print(i, v)






