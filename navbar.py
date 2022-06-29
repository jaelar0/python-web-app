import dash_bootstrap_components as dbc
from dash import Dash, html, dcc


def create_navbar():
    navbar = html.Div([
        html.A([
            html.Img(id='logo-main', src='./assets/img/logo-JLR.svg')
        ]),
        html.A([
            "Home"
        ], href='/', className='nav-button'),
        html.A([
            "Resume"
        ], href='/page-3', className='nav-button'),
        html.A([
            "Dashboards"
        ], href='/page-3', className='nav-button'),
        html.A([
            "Contact"
        ], href='/page-2', className='split')
    ], className='topnav')
    
    return navbar


