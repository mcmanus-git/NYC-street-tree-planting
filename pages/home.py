from dash import html, dcc, callback, Input, Output, State
import dash
import dash_bootstrap_components as dbc
import pickle
from map_helpers import get_tree_count_map

dash.register_page(
    __name__,
    name='NYC Street Trees',
    top_nav=True,
    path='/'
)

def layout():
    map = get_tree_count_map()
    html_lines = ''.join(open('eda_and_scratches/Number of Trees.html', 'r').readlines())
    return html.Div([html.Iframe(srcDoc=html_lines, width='100%', height='700')], style={'margin': '5% 5% 5% 5%'})
    # return html.Div(dcc.Graph(figure=get_tree_count_map()))
    # return dbc.Container(open(get_tree_count_map(), 'rb').read()) #html.Iframe(srcDoc=open('eda_and_scratches/kepler_n_trees.html', 'rb').readlines())

# def layout():
#
#     layout = html.Div(
#         [
#             html.Div(
#                 [
#                     "something child 1"
#                 ]
#             ),
#             html.Div(
#                 [
#                     html.Iframe(
#                         id='tree_count_map',
#                         # srcDoc=open('eda_and_scratches/kepler_n_trees.html', 'r').read(),
#                         srcDoc=get_tree_count_map(),
#                         width='100%',
#                         height='600'
#                     )
#                 ]
#             )
#         ]
#     )
#
#     return layout
