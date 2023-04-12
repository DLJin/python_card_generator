import yaml as py
from PIL import Image, ImageDraw, ImageFont
import card_creation as cc

def main():
    cc.create_character_card("Skanda Palani")
    cc.create_character_card("Artyom")
    cc.create_character_card("Setsuko")
    
if __name__ == "__main__":
    main()