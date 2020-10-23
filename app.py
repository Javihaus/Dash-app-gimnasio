# Import required libraries
import os
from random import randint
import pandas as pd
import plotly.express as px

import flask
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html


#Load csv data
df = pd.read_csv('gimnasio.csv') 
df = df.drop(columns=['Unnamed: 0', 'mes.1', 'mes.2', 'mes.3', 'mes.4'])
df['date']=pd.to_datetime(df['date'])


#Setup the app
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__)

#Setup server
server=app.server

#Dash code
available_indicators = df.columns.unique()

app.layout = html.Div([
    html.Div([html.H1('GYM VS. ECONOMY' ,style={
            'textAlign': 'center', 'font-family': 'helvetica',
            'padding-top':'10px', 'font-weight': '800', 
            'word-spacing': '5px'
        }),
        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='Intensity_economia'
            ),
            dcc.RadioItems(
                id='xaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ],
        style={'width': '45%', 'display': 'inline-block', 'padding': '15px'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='Intensity_gimnasio'
            ),
            dcc.RadioItems(
                id='yaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ], style={'width': '45%', 'float': 'right', 'display': 'inline-block', 
                  'padding': '15px'})
    ]),
        html.Div([
        dcc.Graph(
            id='indicator-graphic'
        )
    ], style={'width':'96%', 'height': '60%', 'display': 'inline-block', 'padding': '15px'}),
        
        html.Div([
        dcc.Graph(id='x-time-series'),
    ], style={'width': '46%', 'display': 'inline-block', 'padding': '15px'}),
  
  html.Div([
        dcc.Graph(id='y-time-series'),
    ], style={'width': '46%', 'display': 'inline-block', 'padding': '15px'})

])

@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value'),
     Input('xaxis-type', 'value'),
     Input('yaxis-type', 'value')])

def update_graph(xaxis_column, yaxis_column,
                 xaxis_type, yaxis_type):
    
    fig = px.density_heatmap(x=df[xaxis_column],
                     y=df[yaxis_column])
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    fig.update_xaxes(title=xaxis_column) 
    fig.update_yaxes(title=yaxis_column) 
    return fig

@app.callback(
    Output('x-time-series', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value')])

def update_y_timeseries(xaxis_column, yaxis_column):
    
    fig = px.scatter(x=df['date'], y=df[xaxis_column],
                    trendline='lowess', trendline_color_override='crimson')
    fig.update_layout(margin={'l': 10, 'b': 10, 't': 10, 'r': 0}, hovermode='closest')
    fig.update_xaxes(title_text="Time") 
    fig.update_yaxes(title=xaxis_column)
    return fig


@app.callback(
    Output('y-time-series', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value')])

def update_y_timeseries(xaxis_column, yaxis_column):
    
    fig = px.scatter(x=df['date'], y=df[yaxis_column],
                    trendline='lowess', trendline_color_override='crimson')
    fig.update_layout(margin={'l': 10, 'b': 10, 't': 10, 'r': 0}, hovermode='closest')
    fig.update_xaxes(title_text="Time") 
    fig.update_yaxes(title=yaxis_column)
    return fig


# Run the Dash app
if __name__ == '__main__':
    app.server.run(debug=True)
