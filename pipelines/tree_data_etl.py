import pandas as pd
from urllib import request
from datetime import datetime
import os
import requests


def get_most_recent_upload_date():
    """
    Fetches most recent data update from NYC Street Tree Planting csv dataset via url
    :return: datetime object YYYY-MM-DD HH:MM:SS - most recent date NYC Street Tree Planting data was updated
    """

    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
        'referer':'https://www.google.com/'
    }

    r = request.Request('https://www.nycgovparks.org/tree-work-orders/street_tree_planting.csv', headers=header)
    response = request.urlopen(r)

    last_build_date = response.readlines()[5].decode('utf-8').split(',')[1].strip('\n')

    last_build_date = datetime.strptime(last_build_date.strip('"'), '%Y-%m-%d %H:%M:%S')

    return last_build_date


def download_new_data():
    """
    Downloads new csv dataset from url and returns clean version in Pandas DataFrame
    :return: Pandas DataFrame
    """
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
        'referer':'https://www.google.com/'
    }

    req = requests.get('https://www.nycgovparks.org/tree-work-orders/street_tree_planting.csv', headers=header)
    content = req.content

    with open('./data/street_tree_planting.csv', 'wb') as f:
        f.write(content)

    df = pd.read_csv('./data/street_tree_planting.csv', skiprows=7)
    df['CompletedDate'] = pd.to_datetime(df['CompletedDate'])
    df['PlantingSeason'] = pd.to_datetime(df['PlantingSeason'])

    return df


def load_tree_data(save=True, return_data=True):
    """
    Determines whether most recent dataset available has already been retrieved.
        If True: Fetches Pickle;
        If False: ETL New Data from URL
    :param save: Default=True save DataFrame to Pickle once Retrieved and Cleaned
    :param return_data: Default=True return Pandas DataFrame object
    :return: Pandas DataFrame
    """
    today = datetime.now()
    today_file = f'data/street_tree_planting_{today.strftime("%Y_%m_%d")}.pkl'

    if os.path.exists(today_file):
        df = pd.read_pickle(today_file)

    elif not os.path.exists(today_file):
        most_recent_web = get_most_recent_upload_date()
        if most_recent_web < today:
            most_recent_file = f'data/street_tree_planting_{most_recent_web.strftime("%Y_%m_%d")}.pkl'
            if os.path.exists(most_recent_file):
                df = pd.read_pickle(most_recent_file)
            elif not os.path.exists(most_recent_file):
                df = download_new_data()
                if save:
                    df.to_pickle(f'data/street_tree_planting_{most_recent_web.strftime("%Y_%m_%d")}.pkl')
        elif most_recent_web == today:
            df = get_most_recent_upload_date()
            if save:
                df.to_pickle(today_file)

    if return_data:
        return df


if __name__ == '__main__':
    load_tree_data()
