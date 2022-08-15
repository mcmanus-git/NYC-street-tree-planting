import pandas as pd
from urllib import request
from datetime import datetime
import os


def get_most_recent_upload_date():
    """
    Fetches most recent data update from NYC Street Tree Planting csv dataset via url
    :return: datetime object YYYY-MM-DD HH:MM:SS - most recent date NYC Street Tree Planting data was updated
    """
    r = request.urlopen('https://www.nycgovparks.org/tree-work-orders/street_tree_planting.csv')

    last_build_date = r.readlines()[5].decode('utf-8').split(',')[1].strip('\n')

    last_build_date = datetime.strptime(last_build_date.strip('"'), '%Y-%m-%d %H:%M:%S')

    return last_build_date


def download_new_data():
    """
    Downloads new csv dataset from url and returns clean version in Pandas DataFrame
    :return: Pandas DataFrame
    """
    df = pd.read_csv('https://www.nycgovparks.org/tree-work-orders/street_tree_planting.csv', skiprows=7)
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
