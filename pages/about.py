import dash
import dash_bootstrap_components as dbc
from dash import html, dcc


dash.register_page(
    __name__,
    name='About',
    top_nav=True,
    path='/about'
)

line_break = html.Div([dcc.Markdown("""___""")], style={'margin': '5% 0% 5% 0%'})

about_header = html.H1('About the Project', style={'textAlign': 'center', 'margin': '10% 0% 5% 0%'})
contact_creator_header = html.H4('-   Contact Me   -', style={'textAlign': 'center'})
about_the_project1 = dcc.Markdown("""This project was inspired by a colleague who turned me on to [Uber's Hexagonal 
Hierarchical Spatial Index](https://www.uber.com/blog/h3/), better known as H3. While working on a project together, my
colleague showed how this spacial index would be invaluable to us. I was instantly impressed with how easy geospatial 
analysis became using this grid system which was a heavy part of the project we were working on. What made things even 
more exciting was this colleague used [Kepler.gl](https://kepler.gl/) to show off the benefits of H3. The only thing 
missing from the presentation was how we could use these libraries and tools programmatically as my colleague was 
dragging csv files into Kepler UI to show case how we could make use of these tools. So, I set out how to learn H3 and 
Kepler.gl.   """)

#![title](assets/kepler_screen.jpg)

about_the_project2 = dcc.Markdown("""The dataset used in this project is from a publication I subscribe to called 
[data is plural](https://www.data-is-plural.com/).  It's a weekly subscription which the author sends out interesting
datasets that can be used for analysis.  One dataset that caught my eye was the 
[NYC Street Tree Planting](https://www.nycgovparks.org/trees/street-tree-planting/locations) dataset. I saw instantly 
how this dataset could be used to satisfy my desire to learn H3 and Kepler.gl.  The map you see on the [home page](/) 
is created using both the H3 library to create the hexagonal indexes and Kepler to create the beautiful map.  The only 
thing left for me to do was to work out some bugs and figure out how to create these maps programmatically to avoid 
the ol' "drag and drop" method.  All my code is available on my 
[GitHub](https://github.com/mcmanus-git/NYC-street-tree-planting) page for review in case you're curious to learn. Hope 
you enjoy.  Cheers!  

**If you're interested in working on a project together, or you have need of some data science wizardry, please visit my 
[contact page](/contact-us) for more details.**  
""")



def layout():

    """
    Generates about page html
    :return: HTML/Dash Object(s)
    """

    layout = html.Div(
        [
            about_header,
            html.Br(),
            about_the_project1,
            html.Br(),
            html.Br(),
            html.Div(
                html.Img(
                    src='assets/kepler_screen.jpg',
                    title="Kepler.gl Home",
                    style={'height': '75%', 'width': '75%'}
                ),
                style={'textAlign': 'center'}
            ),
            html.P('Keppler.gl Home Captured 8/15/2022 by Author', style={'fontSize': 10}),
            html.Br(),
            html.Br(),
            about_the_project2,
            html.Br(),
            html.Br(),
        ],
        style={'margin': '5% 10% 5% 10%'}
    )

    return layout
