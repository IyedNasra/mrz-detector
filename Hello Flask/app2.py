import os
from flask import Flask, jsonify

app = Flask(__name__)

# Define the data fields
fields = {
    "surname": "SINGLETON",
    "name": "JAMES",
    "country": "GBR",
    "nationality": "GBR",
    "birth_date": "451024",
    "expiry_date": "160101",
    "sex": "M",
    "document_type": "P",
    "document_number": "697017735",
    "optional_data": "",
    "birth_date_hash": "4",
    "expiry_date_hash": "3",
    "document_number_hash": "9",
    "optional_data_hash": "0",
    "final_hash": "8",
}

# Define the list
data_list = [
    {"nom": fields.get("name")},
    {"anom": fields.get("name")},  # nom en arabe
    {"prenom": fields.get("surname")},
    {"aprenom": fields.get("surname")},  # prenom en arabe
    {"nationalite": fields.get("nationality")},
    {"numPass": fields.get("document_number")},
    {"numCin": ""},
    {"dateNais": fields.get("birth_date")},
    {"validite": ""},
    {"adresse": ""},
    {"aadresse": ""},  # adresse en arabe
    {"gouvernorat": fields.get("country")},
    {"agouvernorat": ""},
    {"ville": ""},
    {"sexe": fields.get("sex")},
    {"mois": ""},
    {"amois": ""},  # mois en arabe
    {"codePostale": ""},  # Fix: Added missing comma
    {"typeDuDocument": fields.get("document_type")},
    {"date_d'expiration": fields.get("expiry_date")}  # Fix: Fixed field name with single quote
]

# Define the route to serve the JSON file
@app.route('/output', methods=['POST'])
def serve_json_file():
    try:
        # Serve the list as JSON
        return jsonify(data_list)
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)