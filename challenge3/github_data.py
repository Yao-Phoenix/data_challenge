import pandas as pd
import requests

def issues(repo):
    url = 'https://api.github.com/repos/{}/issues'.format(repo)
    df = requests.get(url)
    issues_list = []
    for line in df.json():
        issues_dict = {
                'number': line['number'],
                'title': line['title'],
                'user_name': line['user']['login']
                }
        issues_list.append(issues_dict)

    issues_df = pd.DataFrame(issues_list)
    return issues_df

if __name__ == '__main__':
    issues('numpy/numpy')
