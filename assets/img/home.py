import dash_html_components as html
from navbar import create_navbar

nav = create_navbar()

header = html.H3(['Welcome to my personal page!'], className='welcome')


def create_page_home():
    layout = html.Div([
        nav,
        html.Img(src='./assets/img/logo-lower.svg', id='logo-lower'),
        html.Div([
            html.Div([
                html.H1('Data, Visuals, and Dashboards'),
                html.P('Hundreds of data points feed several dashboards with data coming from sports, finance' + 
                ', and current events. Feel free to explore dashboards, my resume, or hit the contact page and leave me a message.'),
                html.Button('About', id='about', n_clicks=0),
            ], className='container')
        ], className='card')
    ], className='home')
    
    return layout



    