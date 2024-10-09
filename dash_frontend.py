import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import requests
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Health Monitoring Dashboard'),
    dcc.Interval(id='interval-component', interval=60000, n_intervals=0),
    html.Div(id='live-update-text'),
    dcc.Graph(id='live-update-graph')
])

@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_metrics(n):
    data = {
        'heart_rate': random.randint(60, 100),
        'temperature': round(random.uniform(36.0, 37.5), 1)
    }
    response = requests.post('http://localhost:5000/analyze', json=data)
    result = response.json().get('result')
    return f"Heart Rate: {data['heart_rate']}, Temperature: {data['temperature']} - {result}"

@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    conn = sqlite3.connect('health_data.db')
    df = pd.read_sql_query("SELECT * FROM health_metrics ORDER BY timestamp DESC LIMIT 60", conn)
    conn.close()
    fig = {
        'data': [
            {'x': df['timestamp'], 'y': df['heart_rate'], 'type': 'line', 'name': 'Heart Rate'},
            {'x': df['timestamp'], 'y': df['temperature'], 'type': 'line', 'name': 'Temperature'},
        ],
        'layout': {
            'title': 'Real-Time Health Metrics'
        }
    }
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

