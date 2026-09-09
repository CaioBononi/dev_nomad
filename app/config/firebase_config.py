import os
import firebase_admin
from firebase_admin import credentials

def initialize_firebase():
    """Initializes the Firebase Admin SDK."""
    if not firebase_admin._apps:
        # In a real environment, you'd use credentials.Certificate("path/to/serviceAccountKey.json")
        # Or credentials.ApplicationDefault() when running in GCP
        cert_path = os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH")
        if cert_path and os.path.exists(cert_path):
            cred = credentials.Certificate(cert_path)
            firebase_admin.initialize_app(cred)
        else:
            try:
                cred = credentials.ApplicationDefault()
                firebase_admin.initialize_app(cred, {
                    'projectId': 'dev-nomad',
                })
            except Exception as e:
                print(f"Warning: Could not initialize Firebase automatically. {e}")
