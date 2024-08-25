from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# HTML template with enhanced CSS and Filtered Response format
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ roll_number }}</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f8f9fa;
            color: #333;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 700px;
            margin: 50px auto;
            padding: 20px;
            background: #ffffff;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #007bff;
        }
        textarea {
            width: 100%;
            height: 100px;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ced4da;
            border-radius: 5px;
            font-size: 16px;
            font-family: inherit;
            resize: none;
        }
        select {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ced4da;
            border-radius: 5px;
            font-size: 16px;
            font-family: inherit;
        }
        button {
            width: 100%;
            padding: 12px;
            background-color: #007bff;
            border: none;
            border-radius: 5px;
            color: white;
            font-size: 18px;
            font-family: inherit;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #0056b3;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            background: #e9ecef;
            border-radius: 5px;
            font-size: 16px;
            color: #212529;
            white-space: pre-wrap;
        }
        footer {
            margin-top: 40px;
            text-align: center;
            font-size: 14px;
            color: #6c757d;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Data Processor</h1>
        <form id="dataForm">
            <textarea id="jsonInput" placeholder='Enter JSON like {"data": ["A","1","b","2"]}'></textarea>
            <select id="filter">
                <option value="all">All</option>
                <option value="numbers">Numbers</option>
                <option value="alphabets">Alphabets</option>
                <option value="highest_lowercase_alphabet">Highest Lowercase Alphabet</option>
            </select>
            <button type="submit">Submit</button>
        </form>
        <div class="result" id="result"></div>
    </div>
    <footer>
        &copy; 2024 Your Name. All rights reserved.
    </footer>

    <script>
        document.getElementById('dataForm').addEventListener('submit', function(e) {
            e.preventDefault();
            let jsonInput = document.getElementById('jsonInput').value;
            let filter = document.getElementById('filter').value;
            fetch('/bfhl', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: jsonInput
            })
            .then(response => response.json())
            .then(data => {
                let result = '';
                if (filter === 'numbers') {
                    result = 'Filtered Response\\nNumbers: ' + JSON.stringify(data.numbers, null, 2);
                } else if (filter === 'alphabets') {
                    result = 'Filtered Response\\nAlphabets: ' + JSON.stringify(data.alphabets, null, 2);
                } else if (filter === 'highest_lowercase_alphabet') {
                    result = 'Filtered Response\\nHighest Lowercase Alphabet: ' + JSON.stringify(data.highest_lowercase_alphabet, null, 2);
                } else {
                    result = 'Filtered Response\\n' + JSON.stringify(data, null, 2);
                }
                document.getElementById('result').textContent = result;
            })
            .catch(error => {
                document.getElementById('result').textContent = 'Error: ' + error;
            });
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    # Replace with your roll number for the title
    return render_template_string(html_template, roll_number="your_roll_number")

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get('data', [])

        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]

        lowercase_alphabets = [item for item in alphabets if item.islower()]
        highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

        response = {
            "is_success": True,
            "user_id": "your_name_ddmmyyyy",
            "email": "your_email@domain.com",
            "roll_number": "your_roll_number",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
