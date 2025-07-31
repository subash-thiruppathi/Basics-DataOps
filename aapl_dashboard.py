import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
import plotly.graph_objects as go


# Load your stock data (update the file path as necessary)
df = pd.read_csv('./output/stock_data.csv')

# Clean up any blank or bad header rows
df = df[df['date'].str.match(r"\d{4}-\d{2}-\d{2}", na=False)]

# Convert columns to numeric
for col in ['close', 'high', 'low', 'open', 'volume']:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df['date'] = pd.to_datetime(df['date'])

app = Dash(__name__)
stock_symbol = "AAPL"
app.layout = html.Div([
    html.H2(f"{stock_symbol} Stock Dashboard (2025)", style={'textAlign': 'center'}),
    html.Div([
        html.Div([
    html.Div([
        dcc.Graph(
            figure=go.Figure(
                data=[
                    go.Candlestick(
                        x=df['date'],
                        open=df['open'],
                        high=df['high'],
                        low=df['low'],
                        close=df['close']
                    )
                ]
            ).update_layout(title=f"{stock_symbol} Daily Candlestick Chart")
        )
    ])
        ], style={'width': '48%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(
                figure=px.bar(df, x="date", y="volume", title=f"{stock_symbol} Daily Volume")
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),
    ]),

    html.Div([
        dcc.Graph(
            figure=px.area(df, x='date', y='close', title=f"{stock_symbol} Cumulative Close Price Trend")
        )
    ]),
])

if __name__ == '__main__':
    app.run(debug=True)
