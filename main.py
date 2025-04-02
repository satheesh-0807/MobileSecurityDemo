from flask import Flask, make_response, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CTF Challenge - Welcome</title>
        <style>
            body {
                background-color: #0f0f0f;
                color: #39ff14;
                font-family: "Courier New", Courier, monospace;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                flex-direction: column;
            }
            h1 {
                font-size: 3rem;
                margin-bottom: 0.5rem;
            }
            p {
                font-size: 1.5rem;
            }
            .container {
                text-align: center;
                padding: 20px;
                border: 2px solid #39ff14;
                border-radius: 10px;
                box-shadow: 0px 0px 15px #39ff14;
                max-width: 600px;
                margin: auto;
            }
            .footer {
                margin-top: 20px;
                font-size: 1rem;
                color: #888;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to the CTF Challenge!</h1>
            <p>Test your hacking skills and capture the flag!</p>
            <div class="footer">Good luck! You're going to need it... 😈</div>
        </div>
    </body>
    </html>
    '''
    response = make_response(render_template_string(html_content), 200)
    response.headers['X-Flag'] = 'R3dT34m!ng_flag8'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
