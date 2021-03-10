import pathlib

import pandas as pd
import numpy as np
import plotly.express as px  # (version 4.7.0)
import cdata.rss as mod

import dash_core_components as dcc
import dash_html_components as html
#from dash.dependencies import Output, Input

from app import app

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}
colors = {
    'background': '#111221',
    'text': '#7FDBFF'
}
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df = pd.read_csv(DATA_PATH.joinpath("covidreport.csv"))

df = df.dropna()
fig2 = px.sunburst(df, path=['Continents', 'Country'], values='Confirmed',
                   color='Deaths', hover_data=['Country'],
                   color_continuous_scale='RdBu',
                   color_continuous_midpoint=np.average(df['Deaths'], weights=df['Deaths']))
cnxn = mod.connect("URI=https://www.healthissuesindia.com/tag/coronavirus/feed/")
df_rss = pd.read_sql("SELECT * FROM ITEM ", cnxn)
description = []
Link = []
for t in df_rss['Description']:
    description.append(t)


df2_rest = pd.read_csv("https://s3.amazonaws.com/rawstore.datahub.io/9dc095afacc22888e66192aa23e71314.csv")

# App layout

layout = html.Div([

    html.H6("Continent-wise Covid cases", style={'text-align': 'center'}),

    html.Br(),
    html.Marquee(description, dir='rtl',title='Feed Elements',className='text-monospace mb-1'),
    html.Br(),
    html.Div([
        html.Div([
            dcc.Graph(
                id='graph2',
                figure=fig2,

            ),

        ])


    ],)

])
