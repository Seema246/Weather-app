from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = {}
    if request.method == 'POST':
        city = request.form['city']
        api_key = '522aff9a99cfcf5f4027283fbefcc695'  # Replace with your actual key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': city.title(),
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'].title(),
                'humidity': data['main']['humidity'],
                'wind': data['wind']['speed']
            }
        else:
            weather_data = {'error': 'City not found. Please try again.'}
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
