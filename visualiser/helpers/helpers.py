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
        df.columns = ['SAMPLE_ID', 'HRD', 'HRP', 'RESPONDER', 'OS', 'CAL1', 'PFS', 'CAL2']
        df, number_of_unknown = convert_dataframe(df)
    return df, number_of_unknown


def convert_dataframe(dataframe):
    cols = ['SAMPLE_ID', 'HRD_RES', 'HRD_NON_RES', 'HRP_RES', 'HRP_NON_RES', 'OS', 'CAL1', 'PFS', 'CAL2']
    new_df = pd.DataFrame(columns=cols)
    number_of_unknown = 0
    for _, row in dataframe.iterrows():
        if math.isnan(row.RESPONDER):
            number_of_unknown += 1
        else:
            if int(row.HRD) == 1 and int(row.RESPONDER) == 1:
                new_df = new_df.append(pd.DataFrame([[row.SAMPLE_ID, 1, 0, 0, 0, row.OS, row.CAL1, row.PFS, row.CAL2]], columns=cols))
            elif int(row.HRD) == 1 and int(row.RESPONDER) == 0:
                new_df = new_df.append(pd.DataFrame([[row.SAMPLE_ID, 0, 1, 0, 0, row.OS, row.CAL1, row.PFS, row.CAL2]], columns=cols))
            elif int(row.HRD) == 0 and int(row.RESPONDER) == 1:
                new_df = new_df.append(pd.DataFrame([[row.SAMPLE_ID, 0, 0, 1, 0, row.OS, row.CAL1, row.PFS, row.CAL2]], columns=cols))
            elif int(row.HRD) == 0 and int(row.RESPONDER) == 0:
                new_df = new_df.append(pd.DataFrame([[row.SAMPLE_ID, 0, 0, 0, 1, row.OS, row.CAL1, row.PFS, row.CAL2]], columns=cols))
    return new_df, number_of_unknown
