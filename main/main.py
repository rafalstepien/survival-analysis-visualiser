#!/bin/python3

import numpy as np
import sys, os

import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
# import dash_table as dt
# import dash_dangerously_set_inner_html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from flask import Flask, request, Response

home = os.getenv('HOME')
project_path = f"{home}/Dash/survival_analysis_tool"
sys.path[0] = f'{project_path}'

from styles.styles import *


# --------------------------- STYLESHEETS AND APP SETUP ---------------------------
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
external_stylesheets = [dbc.themes.LUX, FONT_AWESOME]

server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

# --------------------------- BODY ---------------------------
body = html.Div('SIEMA')
# --------------------------- LAYOUT ---------------------------
app.layout = html.Div([
    body
])

# --------------------------- CALLBACKS ---------------------------
if __name__ == "__main__":
    app.run_server(debug=True)