
from flask import Flask, render_template, request
import pandas as pd

# Load CSV data
prayer_data = pd.read_csv('Monthly prayer times.csv')

app = Flask(__name__)

@app.route('/')
def index():
    # Display all data
    return render_template('index.html', tables=[prayer_data.to_html(classes='data', index=False)])

@app.route('/search', methods=['POST'])
def search():
    day = request.form.get('day')
    if day:
        filtered_data = prayer_data[prayer_data['Day'] == day]
    else:
        filtered_data = prayer_data
    return render_template('index.html', tables=[filtered_data.to_html(classes='data', index=False)])

if __name__ == '__main__':
    app.run(debug=True)
