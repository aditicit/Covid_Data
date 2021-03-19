import pandas as pd
import plotly.express as px  # (version 4.7.0)

import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}


df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv")

df_continent = df['location'].value_counts().keys()
df_continent
df_Ind = df[df['location'] == 'India']
#print(df_Ind[:5])
layout = html.Div([html.Br(),
    dcc.Tabs([
        dcc.Tab(label='Global',style=tab_style, children=[
            html.H6('Covid Vaccine update in world', style={"textAlign": "center"}),
        dcc.Dropdown(
            id="ticker1",
            options=[{"label": x, "value": x}
                     for x in df.columns[[3,7]]],
                               value = df.columns[3],
                                        clearable=False,
            style={"width": "40%"}
        ),
            dcc.Graph(
                id='vaccination-chart_1'
            )
        ], selected_style=tab_selected_style),

        dcc.Tab(label='India', children=[
            html.H6('Covid Vaccine update in India', style={"textAlign": "center"}),
        dcc.Dropdown(
            id="ticker2",
            options=[{"label": x, "value": x}
                     for x in df_Ind.columns[[3,7]]],
            value=df_Ind.columns[3],
            clearable=False,
            style={"width": "40%"}
        ),
            dcc.Graph(
                id='vaccination-chart_2'

            )
        ], style=tab_style, selected_style=tab_selected_style ,className="container"),
    ],style=tabs_styles)
])

@app.callback(Output('vaccination-chart_1', 'figure'),
              Output('vaccination-chart_2', 'figure'),
     [Input('ticker1', 'value'),
      Input('ticker2', 'value')])

def update_graph(ticker1,ticker2):
    fig1 = px.area(df, x='date', y=ticker1, title='Date tracking with Rangeslider',color='location')
    fig2 = px.area(df_Ind, x='date', y=ticker2, title='Date tracking with Rangeslider')
    fig1.update_xaxes(rangeslider_visible=True)
    fig2.update_xaxes(rangeslider_visible=True)

    return fig1,fig2