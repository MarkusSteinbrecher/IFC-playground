import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv('output.csv')

# Create a Dash application
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("IFC Data Dashboard"),
    dcc.Dropdown(
        id='property-dropdown',
        options=[{'label': i, 'value': i} for i in df.columns],
        value=df.columns[0]
    ),
    dcc.Graph(id='bar-chart')
])

# Define the callback to update the bar chart based on the selected property
@app.callback(
    dash.dependencies.Output('bar-chart', 'figure'),
    [dash.dependencies.Input('property-dropdown', 'value')]
)
def update_bar_chart(selected_property):
    fig = px.bar(df, x='GlobalId', y=selected_property)
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
