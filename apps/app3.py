import pandas as pd
import plotly.express as px  # (version 4.7.0)

import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html

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

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',]
#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv")

df_continent = df['location'].value_counts().keys()
df_continent
df_Ind = df[df['location'] == 'India']
#print(df_Ind[:5])
layout = html.Div([html.Br(),
    dcc.Tabs([
        dcc.Tab(label='Global',style=tab_style, children=[
            html.H6('Daily Vaccination update in world', style={"textAlign": "center"}),
            dcc.Graph(
                figure=px.line(df, x="date", y="daily_vaccinations", color="location"),
            )
        ], selected_style=tab_selected_style),

        dcc.Tab(label='India', children=[
            html.H6('Daily Vaccination update in India', style={"textAlign": "center"}),
            dcc.Graph(
                figure=px.area(df_Ind, x="date", y="daily_vaccinations", color="location", line_group="location"),

            )
        ], style=tab_style, selected_style=tab_selected_style ,className="container"),
    ],style=tabs_styles)
])