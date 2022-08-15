from dash import html, dcc, callback, Input, Output, State
import dash
import dash_bootstrap_components as dbc
import pickle
from map_helpers import create_tree_count_map_html

dash.register_page(
    __name__,
    name='NYC Street Trees',
    top_nav=True,
    path='/'
)


def layout():

    map_filename = create_tree_count_map_html()

    kepler_n_trees_map = html.Iframe(
        srcDoc=open(map_filename, 'r').read(),
        width='100%',
        height='700'
    )

    layout = html.Div(
        [
            kepler_n_trees_map
        ],
        style={'margin': '5% 5% 5% 5%'}
    )
    return layout
