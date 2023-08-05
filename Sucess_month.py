import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string
db = client["PSU_NWMS"]  # Replace "mydatabase" with the name of your database
collection = db["test4"]  # Replace "mycollection" with the name of your collection

# Create the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Function to calculate the total people and count of days for each date
def calculate_total_people_by_date(data):
    summary = {}
    day_count = {}
    for item in data:
        date = item['date'].strftime('%Y-%m')  # Fix date condition
        people = item['x']
        if date in summary:
            summary[date] += people
            day_count[date] += 1
        else:
            summary[date] = people
            day_count[date] = 1
    return summary, day_count

# Fetch data from MongoDB and calculate the summary result
data_from_mongodb = list(collection.find())  # Fetch all documents from the collection
summary_result, day_count = calculate_total_people_by_date(data_from_mongodb)

# Function to get the image based on the total people count
def get_image(total_people, date):
    if total_people <= 50 and date == '2023-01':
        return '/assets/green1.png'
    elif total_people > 50 and date == '2023-01':
        return '/assets/red1.png'
    if total_people <= 50 and date == '2023-02':
        return '/assets/green2.png'
    elif total_people > 50 and date == '2023-02':
        return '/assets/red2.png'
    if total_people <= 50 and date == '2023-03':
        return '/assets/green3.png'
    elif total_people > 50 and date == '2023-03':
        return '/assets/red3.png'
    if total_people <= 50 and date == '2023-04':
        return '/assets/green4.png'
    elif total_people > 50 and date == '2023-04':
        return '/assets/red4.png'
    if total_people <= 50 and date == '2023-05':
        return '/assets/green5.png'
    elif total_people > 50 and date == '2023-05':
        return '/assets/red5.png'
    if total_people <= 50 and date == '2023-06':
        return '/assets/green6.png'
    elif total_people > 50 and date == '2023-06':
        return '/assets/red6.png'
    if total_people <= 50 and date == '2023-07':
        return '/assets/green7.png'
    elif total_people > 50 and date == '2023-07':
        return '/assets/red7.png'
    if total_people <= 50 and date == '2023-08':
        return '/assets/green8.png'
    elif total_people > 50 and date == '2023-08':
        return '/assets/red8.png'
    if total_people <= 50 and date == '2023-09':
        return '/assets/green9.png'
    elif total_people > 50 and date == '2023-09':
        return '/assets/red9.png'
    if total_people <= 50 and date == '2023-10':
        return '/assets/green10.png'
    elif total_people > 50 and date == '2023-10':
        return '/assets/red10.png'
    if total_people <= 50 and date == '2023-11':
        return '/assets/green11.png'
    elif total_people > 50 and date == '2023-11':
        return '/assets/red11.png'
    if total_people <= 50 and date == '2023-12':
        return '/assets/green12.png'
    elif total_people > 50 and date == '2023-12':
        return '/assets/red12.png'

# Define the layout of the app
app.layout = dbc.Container([
    html.H1("Summary Result", className='text-center', style={'margin-top': '20px'}),
    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardImg(src=get_image(total_people, date), top=True, style={'width': '100px', 'height': '100px'}),
                        dbc.CardBody([
                            #html.H5(f"Date: {date}", className='card-title'),
                            #html.P(f"Total People: {total_people}, Average: {average_people:.2f}", className='card-text')
                        ])
                    ],
                    style={'margin': '10px', 'text-align': 'center', 'border': 'none'}  # Remove the border
                ),
                width=1
            )
            for date, total_people in summary_result.items()
            for average_people in [total_people / day_count[date]]
        ],
        justify='center'
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string
db = client["PSU_NWMS"]  # Replace "mydatabase" with the name of your database
collection = db["test4"]  # Replace "mycollection" with the name of your collection

# Create the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Function to calculate the total people and count of days for each date
def calculate_total_people_by_date(data):
    summary = {}
    day_count = {}
    for item in data:
        date = item['date'].strftime('%Y-%m')  # Fix date condition
        people = item['x']
        if date in summary:
            summary[date] += people
            day_count[date] += 1
        else:
            summary[date] = people
            day_count[date] = 1
    return summary, day_count

# Fetch data from MongoDB and calculate the summary result
data_from_mongodb = list(collection.find())  # Fetch all documents from the collection
summary_result, day_count = calculate_total_people_by_date(data_from_mongodb)

# Function to get the image based on the total people count
def get_image(total_people, date):
    if total_people <= 50 and date == '2023-01':
        return '/assets/green1.png'
    elif total_people > 50 and date == '2023-01':
        return '/assets/red1.png'
    if total_people <= 50 and date == '2023-02':
        return '/assets/green2.png'
    elif total_people > 50 and date == '2023-02':
        return '/assets/red2.png'
    if total_people <= 50 and date == '2023-03':
        return '/assets/green3.png'
    elif total_people > 50 and date == '2023-03':
        return '/assets/red3.png'
    if total_people <= 50 and date == '2023-04':
        return '/assets/green4.png'
    elif total_people > 50 and date == '2023-04':
        return '/assets/red4.png'
    if total_people <= 50 and date == '2023-05':
        return '/assets/green5.png'
    elif total_people > 50 and date == '2023-05':
        return '/assets/red5.png'
    if total_people <= 50 and date == '2023-06':
        return '/assets/green6.png'
    elif total_people > 50 and date == '2023-06':
        return '/assets/red6.png'
    if total_people <= 50 and date == '2023-07':
        return '/assets/green7.png'
    elif total_people > 50 and date == '2023-07':
        return '/assets/red7.png'
    if total_people <= 50 and date == '2023-08':
        return '/assets/green8.png'
    elif total_people > 50 and date == '2023-08':
        return '/assets/red8.png'
    if total_people <= 50 and date == '2023-09':
        return '/assets/green9.png'
    elif total_people > 50 and date == '2023-09':
        return '/assets/red9.png'
    if total_people <= 50 and date == '2023-10':
        return '/assets/green10.png'
    elif total_people > 50 and date == '2023-10':
        return '/assets/red10.png'
    if total_people <= 50 and date == '2023-11':
        return '/assets/green11.png'
    elif total_people > 50 and date == '2023-11':
        return '/assets/red11.png'
    if total_people <= 50 and date == '2023-12':
        return '/assets/green12.png'
    elif total_people > 50 and date == '2023-12':
        return '/assets/red12.png'

# Define the layout of the app
app.layout = dbc.Container([
    html.H1("Summary Result", className='text-center', style={'margin-top': '20px'}),
    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardImg(src=get_image(total_people, date), top=True, style={'width': '100px', 'height': '100px'}),
                        dbc.CardBody([
                            #html.H5(f"Date: {date}", className='card-title'),
                            #html.P(f"Total People: {total_people}, Average: {average_people:.2f}", className='card-text')
                        ])
                    ],
                    style={'margin': '10px', 'text-align': 'center', 'border': 'none'}  # Remove the border
                ),
                width=1
            )
            for date, total_people in summary_result.items()
            for average_people in [total_people / day_count[date]]
        ],
        justify='center'
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
