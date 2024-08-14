from dash import html, dcc
import dash
from map_helpers import create_tree_count_map_html

dash.register_page(
    __name__,
    name='NYC Street Trees',
    top_nav=True,
    path='/'
)


def layout():

    """
    Generates home page html
    :return: HTML/Dash Object(s)
    """

    map_filename = create_tree_count_map_html()
    dt_parts = map_filename.strip('.html').split('_')[-3:]

    kepler_n_trees_map = html.Iframe(
        srcDoc=open(map_filename, 'r').read(),
        width='100%',
        height='700'
    )

    layout = html.Div(
        [
            kepler_n_trees_map,
            dcc.Markdown(f"[Data](https://www.nycgovparks.org/trees/street-tree-planting/locations) "
                         f"Updated as of {dt_parts[1]}/{dt_parts[2]}/{dt_parts[0]}", style={'fontSize': 10}),
            dcc.Markdown(f"""This map shows where the trees have been planted through the 
            [NYC Street Tree Planting initiative](https://www.nycgovparks.org/trees/street-tree-planting). The number 
            of trees planted in each area is indicated by the height and color of the hexagons on the map. For more 
            information please see our [About](/about) page. The toggle in the upper left corner of the map will allow 
            you to explore the data more thoroughly and the settings of the map can be tuned to your preference.""")
        ],
        style={'margin': '5% 5% 5% 5%'}
    )
    return layout
