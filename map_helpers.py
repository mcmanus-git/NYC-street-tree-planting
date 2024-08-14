from keplergl import KeplerGl
from pipelines.tree_data_etl import load_tree_data
import h3
from datetime import datetime
import os


def tree_count_map_config():

    """
    Creates configuration dictionary for number of tree kepler map loading state
    :return: Dictionary
    """

    config = {
        "version": "v1", "config": {
            "visState": {

                "filters": [

                ],
                "layers": [
                    {"id": "0rceopc",
                     "type": "hexagonId",
                     "config": {
                         "dataId": "value",
                         "label": "H3 Hexagon",
                         "color": [18, 147, 154],
                         "columns": {"hex_id": "Hex ID"},
                         "isVisible": True,
                         "visConfig": {
                             "opacity": 0.8,
                             "colorRange": {
                                 "name": "Uber Viz Diverging 3.5",
                                 "type": "diverging",
                                 "category": "Uber",
                                 "colors": [
                                     "#00939C",
                                     "#2FA7AE",
                                     "#5DBABF",
                                     "#8CCED1",
                                     "#BAE1E2",
                                     "#F8C0AA",
                                     "#EB9C80",
                                     "#DD7755",
                                     "#D0532B",
                                     "#C22E00"
                                 ]
                             }, "coverage": 0.95,
                             "enable3d": True,
                             "coverageRange": [0, 1],
                             "elevationScale": 10
                         }, "hidden": False,
                         "textLabel": [
                             {
                                 "field": None,
                                 "color": [255, 255, 255],
                                 "size": 18,
                                 "offset": [0, 0],
                                 "anchor": "start",
                                 "alignment": "center"
                             }
                         ]
                     },
                     "visualChannels": {

                         "colorField": {
                             "name": "value",
                             "type": "float"
                         },
                         "colorScale": "quantile",
                         "sizeField": {
                             "name": "value",
                             "type": "integer"
                         },
                         "sizeScale": "linear"
                     }
                     }
                ], "interactionConfig": {
                    "tooltip": {
                        "fieldsToShow": {"value": ["Hex ID", "value"]}, "enabled": True
                    },
                    "brush": {
                        "size": 27,
                        "enabled": False
                    },
                    "geocoder": {
                        "enabled": False  # <<< Bug Leave as False
                    },
                    "coordinate": {
                        "enabled": True
                    }
                }
            },
            "mapState": {
                "bearing": 0,
                "dragRotate": True,
                "latitude": 40.699206,
                "longitude": -73.996297,
                "pitch": 75,
                "zoom": 10.1,
                "isSplit": False
            },
            "mapStyle": {
                "styleType": "dark",
                "topLayerGroups": {},
                "visibleLayerGroups": {},
                "threeDBuildingColor": [
                    3.7245996603793508,
                    6.518049405663864,
                    13.036098811327728
                ],
                "mapStyles": {}
            }
        }
    }

    return config


def create_tree_count_map(tree_counts_df, filename):

    """
    Takes in NYC tree planting dataset dataframe, saves html created by KeplerGL, and returns KeplerGL map object
    :param tree_counts_df: Pandas Dataframe containing hex_id (H3 Hex ID) and value (number of trees) columns
    :param filename: String filename for html save data/kepler_n_trees_{today.strftime("%Y_%m_%d")}.html
    :return: KeplerGL map object
    """

    config_dict = tree_count_map_config()

    map_1 = KeplerGl(config=config_dict, height=600)
    map_1.add_data(tree_counts_df, name='hex_vals')
    map_1.save_to_html(data={'value': tree_counts_df},
                       file_name=filename,
                       config=config_dict
                       )

    return map_1


def geo_to_h3(row):
    """
    Helper function to fetch H3 Hex ID from Latitude and Longitude columns in Pandas Dataframe
    :param row: Pandas Dataframe columns 'lat' and 'lng'
    :return: String - H3 Hex ID
    """
    h3_res = 8
    return h3.geo_to_h3(lat=row.lat, lng=row.lng, resolution=h3_res)


def create_tree_count_map_html():
    """
    Sequence function - Check if KeplerGL map html exists for most recent data pull > If exists no update >
    If not exists > generates KeplerGL map and saves as html
    :return: String - Filename of most recent n_trees map containing most up-to-date data
    """
    today = datetime.now()
    today_file = f'data/kepler_n_trees_{today.strftime("%Y_%m_%d")}.html'

    if not os.path.exists(today_file):
        df = load_tree_data()

        df['hex_id'] = df.apply(geo_to_h3, axis=1)
        tree_counts_hex = (
            df[df['WOStatus'] == 'Completed']
            .value_counts('hex_id')
            .reset_index()
            .rename({'hex_id': 'Hex ID', 0: 'value'}, axis=1)
        )

        tree_counts_hex['value'] = tree_counts_hex['value'].astype(int)
        create_tree_count_map(tree_counts_df=tree_counts_hex, filename=today_file)

    return today_file
