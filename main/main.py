#!/bin/python3

import numpy as np
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

home = os.getenv('HOME')
project_path = f"{home}/Dash/survival-analysis-visualiser"
sys.path[0] = f'{project_path}'

from helpers.helpers import parse_input_file
from styles.styles import *

# --------------------------- STYLESHEETS AND APP SETUP ---------------------------
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
external_stylesheets = [dbc.themes.LUX, FONT_AWESOME]

server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

# --------------------------- BODY ---------------------------
default = dcc.Graph(
            figure={
                'data': [
                    {'x': [],
                    'y': [],
                    }
                ],
                'layout': {
                    "height": 900,
                    'plot_bgcolor': 'white',
                    'paper_bgcolor': 'white',
                    'font': {
                        'color': 'black'
                    }
                }
            },
            id="default-plot"
        )

table = html.Div(dbc.Table(), id='km_table')

# --------------------------- LAYOUT ---------------------------
app.layout = html.Div([
    dbc.Col([
        dbc.Row([
            dcc.Upload(id='upload-data', children = [dbc.Button("Upload file", color='primary')]),
            html.Div(id='tmp_div'),
        ])
    ]),
    default,
    dbc.Col(table),
])

# --------------------------- CALLBACKS ---------------------------
@app.callback(
    Output('km_table', 'children'),
    [Input('upload-data', 'contents'),
     Input('upload-data', 'filename')])
def update_output(content, filename):
    if content is not None:
        df, _ = parse_input_file(content, filename)
        return html.Div(dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, responsive=True), style={'maxHeight': '800px', 'overflow': 'scroll'})

@app.callback(
    Output('tmp_div', 'children'),
    [Input('upload-data', 'contents'),
     Input('upload-data', 'filename')])
def update_unknown(content, filename):
    if content is not None:
        _, uknown = parse_input_file(content, filename)
        return html.Div(f'Number of other/no info about response: {uknown}')

if __name__ == "__main__":
    app.run_server(debug=True)
