import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

def plot_api_trafic():
    try:
        df = pd.read_csv('/shared/track.csv')
        new_df = df['call_timestamp'].value_counts().rename_axis('day').reset_index(name='calls')
        return px.bar(new_df, x="day", y="calls", color="calls")
    except Exception as ex:
        return px.bar()

@app.callback(
    Output("scatter", "figure"),
    Input("dropdown", "value"))
def update_scatter_matrix(dims):
    try:
        df = pd.read_csv('/shared/track.csv')
        return px.scatter_matrix(df, dimensions=dims, color="prediction")
    except:
        return None

def update_boxplot_fraud_vs_amount():
    try:
        df = pd.read_csv('/shared/track.csv')
        return px.box(df, x="prediction", y="amount", color="prediction", notched=True)
    except:
        return px.box()

app.layout = html.Div([

    html.H1('Analysis of Fraud'),
    
    html.H2('API Trafic'),
    dcc.Graph(id='trafic', figure=plot_api_trafic()),
    
    html.H2('Scatter Matrix'),
    dcc.Dropdown(
        id="dropdown",
        options=['step', 'type', 'amount', 'device', 'connection_time', 'oldbalanceOrg',
       'age', 'newbalanceOrig', 'zone', 'user_number', 'user_connections',
       'security_alert', 'oldbalanceDest', 'newbalanceDest'],
        value=['prediction', 'amount'],
        multi=True
    ),
    dcc.Graph(id="scatter"),
    
    html.H2('Distribution of Fraud vs Amount'),
    dcc.Graph(id='boxplot', figure=update_boxplot_fraud_vs_amount())

])


app.run_server(host='0.0.0.0', port=5001, debug=True)

