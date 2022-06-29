import dash_html_components as html
from navbar import create_navbar

nav = create_navbar()

def create_dashboard_page():
    layout = html.Div([
        nav,
    ])


    return layout