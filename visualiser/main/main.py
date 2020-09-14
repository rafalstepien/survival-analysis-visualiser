#!/bin/python3

import numpy as np
import pandas as pd
import sys, os

import base64
import dash
import dash_html_components as html
import dash_table as dt
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from flask import Flask, request, Response

sys.path[0] = '/home/survival-analysis-visualiser/'
print(sys.path[0])

from helpers.helpers import parse_input_file
from styles.styles import *
from plots.plots import *

# --------------------------- STYLESHEETS AND APP SETUP ---------------------------
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
external_stylesheets = [dbc.themes.LUX, FONT_AWESOME]

server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

# --------------------------- BODY ---------------------------
km_plot = html.Div(dcc.Graph(
            figure={
                'data': [
                    {'x': [],
                    'y': [],
                    }
                ],
                'layout': {
                    "height": 850,
                    'plot_bgcolor': 'white',
                    'paper_bgcolor': 'white',
                    'font': {
                        'color': 'black'
                    }
                }
            },
        ), id="km-plot")

radios = html.Div(dcc.RadioItems(
            id='os-pfs-radio',
            options=[{'label': i, 'value': i} for i in ['OS', 'PFS']],
            value='OS',
            ),style={'width': '48%', 'float': 'right', 'size': 20})

# --------------------------- LAYOUT ---------------------------
app.layout = html.Div([
    dbc.Col([
        dbc.Row([
            dcc.Upload(id='upload-data', children = [dbc.Button("Upload file", color='primary')]),
            dbc.Col(radios, width=1),
            dbc.Col(html.H5(id='info-div'), width=8),
        ])
    ]),
    km_plot,
])

# --------------------------- CALLBACKS ---------------------------
@app.callback(
    Output('info-div', 'children'),
    [Input('upload-data', 'contents'),
     Input('upload-data', 'filename')])
def update_unknown(content, filename):
    if content is not None:
        _, uknown = parse_input_file(content, filename)
        return html.Div(f'Number of other/no info about response: {uknown}')

@app.callback(
    Output('km-plot', 'children'),
    [Input('os-pfs-radio', 'value'),
     Input('upload-data', 'contents'),
     Input('upload-data', 'filename')]
)
def update_plot(os_pfs, file_content, filename):
    if file_content is not None:
        os_pfs_dataframe, _ = parse_input_file(file_content, filename)
        figure = plot_main_graph(os_pfs, os_pfs_dataframe)
        graph_to_update = dcc.Graph(figure=figure)
        return graph_to_update

if __name__ == "__main__":
    app.run_server(debug=True)
