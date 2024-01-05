import gspread
import pickle
from oauth2client.service_account import ServiceAccountCredentials

class Authenticator:
    # These are the permissions the script will ask for.
    # These permissions must be manually given to the email associated with this service in the drive folder
    SCOPES = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]

    @staticmethod
    def get_credentials() -> ServiceAccountCredentials:
        # Path to service account credentials JSON file
        credentials_file = 'credentials/coop-roguelite-deckbuilder-5a8932b7f3a9.json'

        # Authenticate using the service account credentials
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, Authenticator.SCOPES)
        
        return credentials
