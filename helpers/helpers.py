import os
import io
import base64
import dash
import math
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import pandas as pd


def parse_input_file(content, filename):
    _, content_string = content.split(',')
    decoded = base64.b64decode(content_string)
    if 'csv' in filename:
        df = pd.read_csv(
            io.StringIO(decoded.decode('utf-8')), sep=';')
        df.columns = ['SAMPLE_ID', 'HRD', 'HRP', 'RESPONDER']
        df, number_of_unknown = convert_dataframe(df)
    return df, number_of_unknown


def convert_dataframe(dataframe):
    new_df = pd.DataFrame(columns=['SAMPLE_ID', 'HRD_RES', 'HRD_NON_RES', 'HRP_RES', 'HRP_NON_RES'])
    number_of_unknown = 0
    for _, row in dataframe.iterrows():
        if math.isnan(row.RESPONDER):
            # DO NOT ADD IF WE DONT KNOW IF PATIENT IS RESPONDER OR NONRESPONDER
            number_of_unknown += 1
        else:
            if int(row.HRD) == 1 and int(row.RESPONDER) == 1:
                # HRD RES
                new_df = new_df.append(pd.DataFrame([[row.SAMPLE_ID, 1, 0, 0, 0]], columns=['SAMPLE_ID', 'HRD_RES', 'HRD_NON_RES', 'HRP_RES', 'HRP_NON_RES']))
            elif int(row.HRD) == 1 and int(row.RESPONDER) == 0:
                # HRD NONRES
                new_df = new_df.append(pd.DataFrame([[row.SAMPLE_ID, 0, 1, 0, 0]], columns=['SAMPLE_ID', 'HRD_RES', 'HRD_NON_RES', 'HRP_RES', 'HRP_NON_RES']))
            elif int(row.HRD) == 0 and int(row.RESPONDER) == 1:
                # HRP RES
                new_df = new_df.append(pd.DataFrame([[row.SAMPLE_ID, 0, 0, 1, 0]], columns=['SAMPLE_ID', 'HRD_RES', 'HRD_NON_RES', 'HRP_RES', 'HRP_NON_RES']))
            elif int(row.HRD) == 0 and int(row.RESPONDER) == 0:
                # HRP NONRES
                new_df = new_df.append(pd.DataFrame([[row.SAMPLE_ID, 0, 0, 0, 1]], columns=['SAMPLE_ID', 'HRD_RES', 'HRD_NON_RES', 'HRP_RES', 'HRP_NON_RES']))
    return new_df, number_of_unknown
