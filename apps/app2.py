import pandas as pd
import plotly.express as px  # (version 4.7.0)

import plotly.graph_objects as go
import numpy as np

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output



from app import app


df1 = pd.read_csv("https://raw.githubusercontent.com/datasets/covid-19/main/data/time-series-19-covid-combined.csv")
df_Ind = df1[df1['Country/Region'] == 'India']

# ------------------------------------------------------------------------------
# App layout
layout = html.Div([

    html.Div([

        html.H6("Daily covid detail in India", style={'text-align': 'center'}),
        dcc.Dropdown(
            id="ticker",
            options=[{"label": x, "value": x}
                     for x in df_Ind.columns[3:]],
            value=df_Ind.columns[4],
            clearable=False,
            style={"width": "40%"}
        ),
        dcc.Graph(id='time-series-chart')
    ])

])

@app.callback(Output('time-series-chart', 'figure'),
     [Input('ticker', 'value')])

def update_graph(ticker):
    fig = px.area(df_Ind, x='Date', y=ticker, title='Date tracking with Rangeslider',line_group='Country/Region')
    fig.update_xaxes(rangeslider_visible=True)

    return fig