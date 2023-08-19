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
def get_month(date):
     if date == '2023-01':
        return "JAN"
     elif date == '2023-02':
        return "FEB"
     elif date == '2023-03':
        return "MAR"
     elif date == '2023-04':
        return "APR"
     elif date == '2023-05':
        return "MAY"
     elif date == '2023-06':
        return "JUN"
     elif date == '2023-07':
        return "JUL"
     elif date == '2023-08':
        return "AUG"
     elif date == '2023-09':
        return "SEP"
     elif date == '2023-10':
        return "OCT"
     elif date == '2023-11':
        return "NOV"
     elif date == '2023-12':
        return "DEC"

def get_color(total_people):
   if total_people < 50:
      return "success"
   else:
      return "danger"

# Define the layout of the app
app.layout = dbc.Container([
   #  html.H1("Summary Result", className='text-center', style={'margin-top': '20px'}),
    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H4(get_month(date), className="card-title"),
                    ],
                    className=f"text-white bg-{get_color(total_people)}")  # Set the color class
                ),
                style={'margin': '2px', 'text-align': 'center', 'border': 'none' , 'width': '120px', 'height': '80px'}  # Remove the border
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
