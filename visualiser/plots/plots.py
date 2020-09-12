from lifelines.fitters.kaplan_meier_fitter import KaplanMeierFitter
import plotly.graph_objects as go


def get_data(os_pfs_dataframe, os_pfs):
    df = os_pfs_dataframe.dropna()

    df_hrd_res = df.loc[df['HRD_RES'] == 1][['SAMPLE_ID', f'{os_pfs}']]
    df_hrd_non_res = df.loc[df['HRP_RES'] == 1][['SAMPLE_ID', f'{os_pfs}']]
    df_hrp_res = df.loc[df['HRD_NON_RES'] == 1][['SAMPLE_ID', f'{os_pfs}']]
    df_hrp_non_res = df.loc[df['HRP_NON_RES'] == 1][['SAMPLE_ID', f'{os_pfs}']]

    vect_hrd_res = getattr(df_hrd_res, os_pfs).str.replace(',', '.').astype('float')
    vect_hrd_non_res = getattr(df_hrd_non_res, os_pfs).str.replace(',', '.').astype('float')
    vect_hrp_res = getattr(df_hrp_res, os_pfs).str.replace(',', '.').astype('float')
    vect_hrp_non_res = getattr(df_hrp_non_res, os_pfs).str.replace(',', '.').astype('float')

    return vect_hrd_res, vect_hrd_non_res, vect_hrp_res, vect_hrp_non_res


def plot_main_graph(os_pfs, os_pfs_dataframe):
    vect_hrd_res, vect_hrd_non_res, vect_hrp_res, vect_hrp_non_res = get_data(os_pfs_dataframe, os_pfs)

    kmf1, kmf2, kmf3, kmf4 = KaplanMeierFitter(), KaplanMeierFitter(), KaplanMeierFitter(), KaplanMeierFitter()
    kmf1.fit(vect_hrd_res)
    kmf2.fit(vect_hrd_non_res)
    kmf3.fit(vect_hrp_res)
    kmf4.fit(vect_hrp_non_res)

    hrd_res_reset = kmf1.survival_function_.reset_index()
    hrd_non_res_reset = kmf2.survival_function_.reset_index()
    hrp_res_reset = kmf3.survival_function_.reset_index()
    hrp_non_res_reset = kmf4.survival_function_.reset_index()

    fig = go.Figure(
        {
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
            }
    )

    fig.add_trace(go.Scatter(x=hrd_res_reset['timeline'], y=hrd_res_reset['KM_estimate'], name="HRD_RES", line_shape='hv'))
    fig.add_trace(go.Scatter(x=hrd_non_res_reset['timeline'], y=hrd_non_res_reset['KM_estimate'], name="HRD_NON_RES", line_shape='hv'))
    fig.add_trace(go.Scatter(x=hrp_res_reset['timeline'], y=hrp_res_reset['KM_estimate'], name="HRP_RES", line_shape='hv'))
    fig.add_trace(go.Scatter(x=hrp_non_res_reset['timeline'], y=hrp_non_res_reset['KM_estimate'], name="HRP_NON_RES", line_shape='hv'))

    fig.update_xaxes(range=[0, 250], title_text='Survival [months]')
    fig.update_yaxes(range=[0, 1], title_text='[%] survived')
    
    return fig
