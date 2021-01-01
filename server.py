# flask for web app.
import flask as fl
from model import power_prediction

# Create a new web app.
app = fl.Flask(__name__,static_url_path = '',static_folder = 'static')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route("/<float:speed>")
def predict(speed):
    return power_prediction(speed)

if __name__ == "__main__":
    app.run(debug = True)