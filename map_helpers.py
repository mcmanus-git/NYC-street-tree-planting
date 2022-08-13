from keplergl import KeplerGl
import pandas as pd
from pipelines.tree_data_etl import load_tree_data
import h3


def tree_count_map_config():

    config = {
        "version": "v1",
        "config": {
            "visState": {
                "layers": [
                    {
                        "id": "tn4tqvj",
                        "type": "hexagonId",
                        "config": {
                            "dataId": "value",
                            "label": "Hex ID",
                            "color": [
                                221,
                                178,
                                124
                            ],
                            "highlightColor": [
                                252,
                                242,
                                26,
                                255
                            ],
                            "columns": {
                                "hex_id": "Hex ID",
                                "value": "value"
                            },
                            "isVisible": True,
                            "visConfig": {
                                "opacity": 0.8,
                                "worldUnitSize": 1,
                                "colorRange": {
                                    "name": "Uber Viz Diverging 1.5",
                                    "type": "diverging",
                                    "category": "Uber",
                                    "colors": [
                                        "#00939C",
                                        "#5DBABF",
                                        "#BAE1E2",
                                        "#F8C0AA",
                                        "#DD7755",
                                        "#C22E00"
                                    ]
                                },
                                "coverage": 0.95,
                                "enable3d": True,
                                "sizeRange": [
                                    0,
                                    500
                                ],
                                "coverageRange": [
                                    0,
                                    1
                                ],
                                "elevationScale": 25,
                                "enableElevationZoomFactor": True
                            },
                            "hidden": False,
                            "textLabel": [
                                {
                                    "field": None,
                                    "color": [
                                        255,
                                        255,
                                        255
                                    ],
                                    "size": 18,
                                    "offset": [
                                        0,
                                        0
                                    ],
                                    "anchor": "start",
                                    "alignment": "center"
                                }
                            ]
                        },
                        "visualChannels": {
                            "colorField": {
                                "name": "value",
                                "type": "integer"
                            },
                            "colorScale": "quantile",
                            "sizeField": {
                                "name": "value",
                                "type": "integer"
                            },
                            "sizeScale": "linear",
                            "coverage": 0.95,
                            "coverageField": None,
                            "coverageScale": "linear",
                        }
                    }
                ],
                "filters": [],
                "interactionConfig": {
                    "tooltip": {
                        "fieldsToShow": {
                            "value": [
                                {
                                    "name": "Hex ID",
                                    "format": None
                                },
                                {
                                    "name": "value",
                                    "format": None
                                }
                            ]
                        },
                        "compareMode": False,
                        "compareType": "absolute",
                        "enabled": True
                    },
                    "brush": {
                        "size": 0.5,
                        "enabled": True
                    },
                    "geocoder": {
                        "enabled": True
                    },
                    "coordinate": {
                        "enabled": True
                    }
                },
                "layerBlending": "normal",
                "splitMaps": [],
                "animationConfig": {
                    "currentTime": None,
                    "speed": 1
                }
            },
            "mapState": {
                "bearing": 20,
                "dragRotate": True,
                "latitude": 40.71251981584756,
                "longitude": -73.97134402172449,
                "pitch": 75,
                "zoom": 10,
                "isSplit": False,
            },
            "mapStyle": {
                "styleType": "dark",
                "topLayerGroups": {},
                "visibleLayerGroups": {
                    "label": True,
                    "road": True,
                    "border": False,
                    "building": True,
                    "water": True,
                    "land": True,
                    "3d building": False
                },
                "threeDBuildingColor": [
                    9.665468314072013,
                    17.18305478057247,
                    31.1442867897876
                ],
                "mapStyles": {}
            }
        }
    }

    return config


def create_tree_count_map(tree_counts_df):
    config_dict = tree_count_map_config()
    # map_1 = KeplerGl(config=config_dict, height=600)
    # map_1.add_data(tree_counts_df, name='hex_vals')
    # map_1.save_to_html(data={'value': tree_counts_df}, config=config_dict, file_name='data/kepler_n_trees.html')


    map_1 = KeplerGl(config=config_dict, height=600)
    map_1.add_data(tree_counts_df, name='hex_vals')
    map_1.save_to_html(data={'value': tree_counts_df}, file_name='eda_and_scratches/Number of Trees Config2.html', config=config_dict)

    return map_1



def geo_to_h3(row):
    h3_res = 8
    return h3.geo_to_h3(lat=row.lat, lng=row.lng, resolution=h3_res)


def get_tree_count_map():
    df = load_tree_data()

    df['hex_id'] = df.apply(geo_to_h3, axis=1)
    tree_counts_hex = df[df['WOStatus'] == 'Completed'].value_counts('hex_id').reset_index().rename({'hex_id': 'Hex ID', 0: 'value'}, axis=1)
    tree_counts_hex['value'] = tree_counts_hex['value'].astype(int)
    map_n_trees = create_tree_count_map(tree_counts_hex)

    return map_n_trees#._repr_html_()
