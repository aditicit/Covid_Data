import pathlib

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import plotly.express as px

from dash.dependencies import Input, Output

from app import app
from apps import app3, app1, app2

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df = pd.read_csv(DATA_PATH.joinpath("covidreport.csv"))


df = df.dropna()

fig = px.choropleth(
        data_frame=df,
        locationmode='country names',
        locations='Country',
        scope="world",
        color='Deaths',
        hover_data=['Country', 'Deaths', 'Confirmed'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Deaths': 'No. of Deaths'},
        width=1000, height=500,
        template='plotly_dark')

app.title = 'Covid 19 Dashboard'
app.layout = html.Div([

    dcc.Location(id='url', refresh=False),
    html.Div((
        dbc.NavLink(" Home ", href='/', active=True),
        dbc.NavLink('World Covid Cases ', href='/apps/app1'),
        dbc.NavLink('India Covid Cases ', href='/apps/app2'),
        dbc.NavLink('Vaccination', href='/apps/app3')
    ), className="row"),
    html.Br(),
    html.Div(id='page-content', children=[])

])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/':
        return [
            html.H5("Covid 19 Dashboard", style={'text-align': 'center'}),
            dcc.Graph(
            id='graph1',
            figure=fig,

        )]
    if pathname == '/apps/app1':
        return app1.layout
    if pathname == '/apps/app2':
        return app2.layout
    if pathname == '/apps/app3':
        return app3.layout
    else:
        return "404 error"


if __name__ == '__main__':
    app.run_server(debug=True)
