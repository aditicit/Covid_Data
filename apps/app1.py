import pathlib

import pandas as pd
import numpy as np
import plotly.express as px  # (version 4.7.0)
import cdata.rss as mod

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

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
cnxn = mod.connect("URI=https://medicalnewsbulletin.com/tag/coronavirus/feed/")
df_rss = pd.read_sql("SELECT * FROM ITEM ", cnxn)
title = df_rss['Title']
Link = df_rss['Link']


df2_rest = pd.read_csv("https://s3.amazonaws.com/rawstore.datahub.io/9dc095afacc22888e66192aa23e71314.csv")

# App layout
layout = html.Div([

    html.H6("Continent-wise Covid cases", style={'text-align': 'center'}),

    html.Br(),

    html.Div([

        html.Div(id='output_container', children=[]),

        html.Div([
            dcc.Graph(
                id='graph2',
                figure=fig2,

            ),

            # html.Marquee(title="This text will scroll from bottom to top",data=)

        ])

    ], className="row")

])


@app.callback(
    Output(component_id='output_container', component_property='children'),
    [Input(component_id='title', component_property='value'),
     Input(component_id='Link', component_property='value')]
)
def set_display_children(title, Link):
    return "The Data chosen by user was: {}".format(title)
