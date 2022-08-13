import dash_bootstrap_components as dbc
import dash.html as html
from dash import dcc


def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink([html.I(className="fab fa-facebook")],
                                    href="https://www.facebook.com/HDBestimate/",
                                    target="_blank")
                        ),
            dbc.NavItem(dbc.NavLink([html.I(className="fab fa-instagram")],
                                    href="https://www.instagram.com/hdbestimate/",
                                    target="_blank")
                        ),
            dbc.NavItem(dbc.NavLink([html.I(className="fab fa-twitter")],
                                    href="https://twitter.com/HDBestimate",
                                    target="_blank")
                        ),
            dbc.NavItem(dbc.NavLink([html.I(className="fab fa-linkedin")],
                                    href="https://www.linkedin.com/company/hdbestimate/",
                                    target="_blank")
                        ),
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                children=[
                    dbc.DropdownMenuItem("Home", href='/'),
                    dbc.DropdownMenuItem(divider=True),
                    # dbc.DropdownMenuItem("Blog", href='/blog'), # commented out until we can revisit the blog
                    dbc.DropdownMenuItem("Explore", href='/explore'),
                    dbc.DropdownMenuItem("Contact Us", href='/contact-us'),
                ],
            ),
        ],
        brand="NYC Street Trees",
        brand_href="/",
        sticky="top",
        # color='#D91800',
        color="primary",  # Change this to change color of the navbar e.g. "primary", "secondary", "dark" etc.
        dark=True,  # Change this to change color of text within the navbar (False for dark text)
    )

    return navbar
