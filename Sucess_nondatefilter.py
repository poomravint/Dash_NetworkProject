import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import pymongo

# Create the Dash app
app = dash.Dash(__name__)

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["PSU_NWMS"]
collection = db["test2"]

# Sample data for the number of people using the phone at different dates and times
data = collection.find({}, {"_id": 0})

# Convert data to a DataFrame
df = pd.DataFrame(data)
df['y'] = pd.to_datetime(df['y'])

# Define the app layout
app.layout = html.Div([
    html.H1('โปรเจคกระดอหน้าส้นตีน กุอยากกลับไปทำดาวเทียมไอ้เหี้ย'),
    dcc.Graph(id='phone-usage-plot'),
    dcc.Interval(
        id='interval-component',
        interval=60*1000,  # in milliseconds, set to update every minute
        n_intervals=0
    )
])

# Define the app callback
@app.callback(
    Output('phone-usage-plot', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_plot(n_intervals):
    selected_date = pd.to_datetime('2023-07-23')  # Replace '2022-01-03' with the date you want to filter by

    filtered_df = df[df['y'].dt.date == selected_date.date()]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=filtered_df['y'],
        y=filtered_df['x'],
        mode='lines+markers',  # Use 'lines+markers' for line plot with dots
        marker=dict(
            size=10,
            color='blue',
            line=dict(width=2, color='DarkSlateGrey')
        ),
        line=dict(color='blue', width=2)
    ))

    fig.update_layout(   
        xaxis=dict(
            title='Time', #! Y-asis tittle
            showgrid=True,
            showline=True,
            showticklabels=True,
            #dtick='M1',  # Show a tick for each month
            tickformat='%Y-%m-%d %H:%M'  # Format the tick labels
        ),
        yaxis=dict(
            title='Number of people', #! Y-asis tittle
            showgrid=True,
            showline=True,
            showticklabels=True,
        ),
        margin=dict(l=50, r=50, t=50, b=50),
        hovermode='x',
    )

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
