from datetime import datetime
import pytz
from pymongo.errors import CollectionInvalid
from utils.db import db
from bson import ObjectId

def create_collections():
    try:
        if 'users' not in db.list_collection_names():
            db.create_collection('users')
            print("Collection 'users' created.")
        else:
            print("Collection 'users' already exists.")

        if 'studies' not in db.list_collection_names():
            db.create_collection('studies')
            print("Collection 'studies' created.")
        else:
            print("Collection 'studies' already exists.")

        if 'messages' not in db.list_collection_names():
            db.create_collection('messages')
            print("Collection 'messages' created.")
        else:
            print("Collection 'messages' already exists.")

        if 'data_entries' not in db.list_collection_names():
            db.create_collection('data_entries')
            print("Collection 'data_entries' created.")
        else:
            print("Collection 'data_entries' already exists.")

        if 'audit_trail' not in db.list_collection_names():
            db.create_collection('audit_trail')
            print("Collection 'audit_trail' created.")
        else:
            print("Collection 'audit_trail' already exists.")

        if 'dashboard_metrics' not in db.list_collection_names():
            db.create_collection('dashboard_metrics')
            print("Collection 'dashboard_metrics' created.")
        else:
            print("Collection 'dashboard_metrics' already exists.")
        
    except CollectionInvalid as e:
        print(f"Error creating collection: {e}")

def test_connection_and_crud():
    now = datetime.now(pytz.utc)

    # Test d'insertion d'un utilisateur
    user_data = {
        "id": ObjectId(),
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "password_hash": "hashed_password",
        "phone": "1234567890",
        "created_at": now,
        "updated_at": now,
        "roles": "owner"
    }

    result = db.users.insert_one(user_data)
    print(f"User created with ID: {result.inserted_id}")

    # Test de récupération de l'utilisateur
    user = db.users.find_one({"_id": result.inserted_id})
    print(f"User retrieved: {user}")

if __name__ == "__main__":
    create_collections()
    test_connection_and_crud()