#import os
#import string
#import textwrap
#import time
import io
from typing import Dict, List, Sequence, Union
import yaml

import gspread
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.service_account import Credentials


class Downloader:
    # The Folder ID is the part of the URL after */folders/
    FOLDER_ID = "1foq0SmSYHUqJjb0yhBc8aA9XC6I_U0qg"

    def __init__(self, credentials: Credentials) -> None:
        self.drive_service = build("drive", "v3", credentials=credentials)
        #self.sheets_service = build("sheets", "v4", credentials=credentials)
        self.sheets_client = gspread.authorize(credentials)

    def _fetch_drive_items(self) -> List[Dict]:
        results = (
            self.drive_service.files()
            .list(
                q=f'"{Downloader.FOLDER_ID}" in parents and trashed=false',
                pageSize=100,  # number of files downloaded
                fields="nextPageToken, files(id, name, mimeType)",
            )
            .execute()
        )
        return results.get("files", [])
                
    def ingest_cards(self):
        items = self._fetch_drive_items()
        print(f"Fetching {len(items)} items from Google Drive")
        for item in items:
            print(f'==> Downloaded {item["name"]} ==== ({item["id"]}) ==== ({item["mimeType"]})')  # debugging

            if item["mimeType"] == "application/vnd.google-apps.spreadsheet":
                print(f'{item["name"]} is a Google Sheets file.')

                # Open the Google Sheet
                sheet = self.sheets_client.open_by_key(item["id"])

                # Extract names of all worksheets
                worksheets = sheet.worksheets()

                # Iterate through all sheets
                for worksheet in worksheets:
                    print(worksheet.title)

                    # Get all values from the worksheet
                    # This function counts as a single API Read Request
                    # The limit on these for free users is 500 requests per 100 seconds per project, and 100 reqeuests per 100 seconds per user
                    data = worksheet.get_all_records()

                    # Print the downloaded data
                    for row in data:
                        for key, value in row.items():
                            print(key, "\t\t", value)
                        print("=============================================")

            elif item["mimeType"] == "application/vnd.google-apps.document":
                print(f'{item["name"]} is a Google Docs file.')
                # Add your code to handle Google Docs files here

            else:
                print(f'{item["name"]} is a file of type {item["mimeType"]}.')
                # Add your code to handle other types of files here
