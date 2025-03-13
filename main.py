 
# # Auto-generated Python Script

# # Required Imports
# from flask import Request, jsonify

# import requests.sessions


# # Function Definitions
# def hello_world10(request: Request):
#     """Function to handle API requests"""

#     # Parse the JSON body
#     request_json = request.get_json(silent=True)

#     # Extract required parameters dynamically
    
#     url = request_json.get("url")
    
#     params = request_json.get("params")
    

#     try:
#         # Make API request dynamically
#         response = requests.api.get(url, params)
#         return jsonify(response.json()), response.status_code  # Ensure JSON response with status code
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500  # Handle errors properly



# from flask import Flask, request, jsonify

# app = Flask(__name__)

# def function_one():
#     return "Hello from Function One!"

# def function_two():
#     return "Hello from Function Two!"

# def function_three():
#     return "Hello from Function Three!"

# @app.route('/invoke', methods=['POST'])
# def dispatcher():
#     data = request.get_json()
#     function_name = data.get("function")

#     functions = {
#         "function_one": function_one,
#         "function_two": function_two,
#         "function_three": function_three,
#     }

#     if function_name in functions:
#         return jsonify({"result": functions[function_name]()})
#     else:
#         return jsonify({"error": "Function not found"}), 404

# if __name__ == "__main__":
#     app.run(port=8080)



# ==============================================================

from flask import Flask, request, jsonify

app = Flask(__name__)

def function_one():
    return "Hello from Function One!"

def function_two():
    return "Hello from Function Two!"

def function_three():
    return "Hello from Function Three!"

@app.route('/invoke', methods=['POST'])
def dispatcher():
    data = request.get_json()
    function_name = data.get("function")

    functions = {
        "function_one": function_one,
        "function_two": function_two,
        "function_three": function_three,
    }

    if function_name in functions:
        return jsonify({"result": functions[function_name]()})
    else:
        return jsonify({"error": "Function not found"}), 404

@app.route('/one', methods=['GET'])
def call_function_one():
    return jsonify({"result":function_one})
   

if __name__ == "__main__":
    app.run(port=8080)

