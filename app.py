from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)


# Serve the map page
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to receive location data
@app.route('/submit', methods=['POST'])
def submit_Form():
    data = request.get_json()
    print(data)
    latitude = data.get('latitude1')
    longitude = data.get('longitude1')
    latitude2 = data.get('longitude2')
    longitude2 = data.get('longitude2')
    days = data.get('days')
    time = data.get('time')
    
    # Save to SQLite database (as an example)
    conn = sqlite3.connect('locations.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS locations (latitudeStart REAL, longitudeStart REAL, latitudeFinal REAL, longitudeFinal REAL,  time TIME)')
    cursor.execute('INSERT INTO locations (latitudeStart, longitudeStart, latitudeFinal, longitudeFinal,  time) VALUES (?, ?, ?, ?, ?)', (latitude, longitude, latitude2, longitude2, time))
    conn.commit()
    conn.close()

    return jsonify({'status': 'success', 'latitude': latitude, 'longitude': longitude})

if __name__ == '__main__':
    app.run(debug=True)
