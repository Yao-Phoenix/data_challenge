import requests
from lxml import html

def user_info(user_id):
    url = 'https://www.shiyanlou.com/users/{}'.format(user_id)
    df = requests.get(url)
    if df.status_code == 200:
        tree = html.fromstring(df.text)
        user_name = tree.xpath('//div[@class="user-meta"]/span/text()')[0].strip()
        user_level = int(tree.xpath('//div[@class="user-meta"]/span/text()'
            )[1].strip()[1:])
        join_date = tree.xpath('//span[@class="user-join-date"]/text()'
                )[0].strip().split(' ')[0]
    else:
        user_name, user_level, join_date = None, None, None
    return user_name, user_level, join_date

if __name__ == '__main__':
    print(user_info('214893'))
    print(user_info('1234567890'))
