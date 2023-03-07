import dash_html_components as html
from navbar import create_navbar

nav = create_navbar()

def create_page_2():
    layout = html.Div([
        nav,

    ])
    return layout