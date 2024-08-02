import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
print(res)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline')
votes = soup.select('.score')

def sort_stories_vote(hnList):

       return sorted(hnList, key=lambda k:k['vote'], reverse=True)



def create_custom_hacker(link, vote):
    hn = []
    for idx, item in enumerate(links):
        title = link[idx].getText()
        url = link[idx].a.get('href')

        try:
            points = int(vote[idx].getText().replace('points', ''))

        except:
            continue

        if points > 100:
            hn.append({'title': title, 'link': url, 'vote': points})
        else:
            continue

    return sort_stories_vote(hn)


hn_ret = (create_custom_hacker(links, votes))
# print(hn_ret)


print(hn_ret)
for i in hn_ret:
    print(i['vote'], '\t', i['title'], i['link'])
