import dash
import dash_bootstrap_components as dbc
from dash import html, dcc


dash.register_page(
    __name__,
    name='About',
    top_nav=True,
    path='/about'
)


def layout():

    layout = html.Div(
        [
            'PLace'
        ],
        style={'margin': '5% 10% 5% 10%'}
    )

    return layout