from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # HTML code directly in the Python function
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Web App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                text-align: center;
                padding-top: 50px;
            }
            h1 {
                color: #333;
            }
            p {
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to Flask Web App!</h1>
        <p>This is a simple Flask app with HTML directly inside Python.</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
