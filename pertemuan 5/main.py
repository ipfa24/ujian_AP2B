from flask import Flask, request, jsonify

app = Flask(__name__)

# contoh data sederhana
data = [
    {
        "id": 1, 
        "nama": "Imron", 
        "kelas": "2IA02", 
        "npm": "51421667",
        "Hobi": "Futsal",
        "Jurusan": "Informatika",
     }
]

@app.route('/')
def home():
    return "API Ready"

# route untuk metode GET
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

# route untuk metode POST
@app.route('/api/data', methods=['POST'])
def add_data():
    new_data = request.json
    data.append(new_data)
    return jsonify(new_data)

if __name__ == '__main__':
    app.run(debug=True)