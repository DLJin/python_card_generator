import yaml as py
from PIL import Image, ImageDraw, ImageFont
import card_creation as cc
from ingest_cards.credential_access import Authenticator
from ingest_cards.download_data import Downloader

def main():
    creds = Authenticator.get_credentials()
    downloader = Downloader(creds)
    downloader.ingest_cards()
    #cc.create_character_card("Skanda Palani")
    #cc.create_character_card("Artyom")
    #cc.create_character_card("Setsuko")
    
if __name__ == "__main__":
    main()