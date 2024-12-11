from dash import Dash, html, dcc, Input, Output

import pandas as pd
import plotly.express as px
from random import randint, seed

app = Dash(name="simple_dashboard")

server = app.server

############################# VARIABLES #######################################
dark_blue = '#021736'
light_blue = '#05C0F0'
seed(11)

############################# DATASETS ########################################
df_dict = {
    '<10':[randint(0,9) for x in range(0,20)],
    '10-19':[randint(10,19) for x in range(0,20)],
    '20-29':[randint(20,29) for x in range(0,20)],
    '0-100':[randint(0,100) for x in range(0,20)],
}

index = [f'measure {x}' for x in range(0,20)]

df = pd.DataFrame(df_dict, index)

############################# GRAPHS ##########################################
def create_line(selection):
    return px.line(df, x=df.index, y=df[selection],
                   title='Fig 2: Representation of random numbers', 
                   labels={"index": "Sample", selection: "Value"}
                   )

def create_bar(selection):
    return px.bar(df, x=df.index, y=df[selection], 
                  title='Fig 2: Representation of random numbers', 
                  labels={"index": "Sample", selection: "Value"}
                  )

############################# WIDGETS #########################################
line_input = dcc.Dropdown([col for col in list(df.columns)], 
                          list(df.columns)[0], 
                          id='dropdown-line')

bar_input = dcc.Dropdown([col for col in list(df.columns)], 
                          list(df.columns)[0], 
                          id='dropdown-bar')

############################# APP LAYOUT ######################################
app.layout = html.Div(className='main-container', children=[
    html.Div(className='header', children=[
        html.Img(src='assets/your-logo-here-1.png', className='logo'),
        html.Div([
            html.H1('YOUR CUSTOM DASHBOARD'), 
            html.P('source logo: https://cultivatingdigital.com/wp-content/uploads/2023/12/your-logo-here-1.png', id='source'),
        ]),
    ]),
    html.Div(className='body', children=[
        dcc.Tabs(className="tabs", children=[
            dcc.Tab(className="tab", label='Hello Dash World!', children=[html.Div(className="center-text", children=[
                html.H2('Hello there!'), 
                html.P(["This dashboard is a simple to use-case with some minimal functionalities. And free of use!", 
                        html.Br(), 
                        "It will allow you to upload a simple CSV-file and present it in a line graph or bar chart."]),
                html.P(["If you are interested in more, please find all the documentation at ", 
                        html.A("Plotly Dash", href="https://dash.plotly.com/", target='_blank', rel="noopener noreferrer"),
                        "."]),
                html.P("Kind regards")])
            ]),    
            dcc.Tab(className="tab", label='Line Chart', children=[html.Div(id="line-chart", children=[
                line_input,
                dcc.Graph(id='line')])
            ]), 
            dcc.Tab(className="tab", label='Bar Graph', children=[html.Div(id="bar-chart", children=[
                bar_input,
                dcc.Graph(id='bar')])
            ]),
        ]),
    ]),
    html.Div(className='footer', children=[
        html.H2('Free display of a simple dash app')
    ]),
])
############################# CALLBACKS #######################################
@app.callback(
    Output('line', 'figure'),
    Input('dropdown-line', 'value')
)
def update_create_line(value):
    return create_line(value)

@app.callback(
    Output('bar', 'figure'),
    Input('dropdown-bar', 'value')
)
def update_create_bar(value):
    return create_bar(value)


if __name__ == '__main__':
    app.run(debug=True)