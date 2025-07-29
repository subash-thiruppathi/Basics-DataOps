import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Load your transformed sales data
df = pd.read_csv('/home/finstein-emp/airflow/output/transformed_sales.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Analytics Dashboard"),

    html.Div([
        html.Div([
            html.H4("Net Revenue by Region"),
            dcc.Graph(
                figure=px.bar(
                    df.groupby('region')['net_revenue'].sum().reset_index(),
                    x='region', y='net_revenue', color='region',
                    labels={'net_revenue': 'Net Revenue'}, title="Net Revenue by Region"
                )
            )
        ], style={'width': '48%', 'display': 'inline-block'}),
        html.Div([
            html.H4("Product Distribution"),
            dcc.Graph(
                figure=px.pie(
                    df, names='product', values='quantity',
                    title="Product Wise Sales Quantity"
                )
            )
        ], style={'width': '48%', 'display': 'inline-block', 'float': 'right'})
    ]),

    html.Div([
        html.H4("Net Revenue Over Time"),
        dcc.Graph(
            figure=px.line(
                df.groupby('date')['net_revenue'].sum().reset_index(),
                x='date', y='net_revenue', markers=True,
                title="Net Revenue Trend Over Time"
            )
        )
    ]),

    html.Div([
        html.H4("Total Discounts by Region"),
        dcc.Graph(
            figure=px.bar(
                df.groupby('region')['discount_amount'].sum().reset_index(),
                x='region', y='discount_amount', color='region',
                title="Total Discount Amount by Region"
            )
        )
    ]),
])

if __name__ == "__main__":
    app.run(debug=True)

