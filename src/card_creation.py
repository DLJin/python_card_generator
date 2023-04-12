import yaml
from PIL import Image, ImageDraw, ImageFont

NAME_FONT = ImageFont.truetype("assets/fonts/PTSerif-Bold.ttf", size = 36)
STATS_FONT = ImageFont.truetype("assets/fonts/PTSerif-Bold.ttf", size = 21)

def create_character_card(character_name):
    # setup image template
    template = Image.open("assets/template/character_card_template.png")
    draw = ImageDraw.Draw(template)

    # open card structure information
    with open("data/templates/character_template.yaml", "r") as structure_yaml_file:
        try:
            sy = yaml.safe_load(structure_yaml_file)
            #print(yaml.dump(sy))
        except yaml.YAMLError as exec:
            print(exc)

    # open character attribute information
    processed_char_name = character_name.replace(" ", "_").lower()
    with open("data/characters/" + processed_char_name + ".yaml", "r") as attribute_yaml_file:
        try:
            ay = yaml.safe_load(attribute_yaml_file)
            #print(yaml.dump(ay))
        except yaml.YAMLError as exc:
            print(exc)        

    # print character name
    font = NAME_FONT
    msg = character_name
    w, h = draw.textsize(msg, font = font)
    draw.text((sy['name']['x'] - w/2, sy['name']['y']), msg, font = font, fill = "white")

    # print character splash art
    face = Image.open("assets/character_art/" + processed_char_name + ".png").resize((sy['splash_art']['w'], sy['splash_art']['h']), Image.ANTIALIAS)
    template.paste(face, (sy['splash_art']['x'], sy['splash_art']['y']))

    # print character attributes
    font = STATS_FONT

    # first row
    msg = "SUR: " + str(ay['attr']['sur'])
    w, h = draw.textsize(msg, font = font)
    draw.text((sy['attr_1']['x'] - (3 * w)/2 - sy['attr_1']['offset'], sy['attr_1']['y']), msg, font = font, fill = sy['attr_1']['sur_color'])
    msg = "TEN: " + str(ay['attr']['ten'])
    w, h = draw.textsize(msg, font = font)
    draw.text((sy['attr_1']['x'] - w/2, sy['attr_1']['y']), msg, font = font, fill = sy['attr_1']['ten_color'])
    msg = "MIG: " + str(ay['attr']['mig'])
    w, h = draw.textsize(msg, font = font)
    draw.text((sy['attr_1']['x'] + w/2 + sy['attr_1']['offset'], sy['attr_1']['y']), msg, font = font, fill = sy['attr_1']['mig_color'])
    msg = "INT: " + str(ay['attr']['int'])
    w, h = draw.textsize(msg, font = font)

    # second row
    draw.text((sy['attr_2']['x'] - w/2 - sy['attr_2']['offset'], sy['attr_2']['y']), msg, font = font, fill = sy['attr_2']['int_color'])
    msg = "WIT: " + str(ay['attr']['wit'])
    w, h = draw.textsize(msg, font = font)
    draw.text((sy['attr_2']['x'] - w/2 + sy['attr_2']['offset'], sy['attr_2']['y']), msg, font = font, fill = sy['attr_2']['wit_color'])

    # third row
    msg = "HP: " + str(ay['attr']['hp'])
    w, h = draw.textsize(msg, font = font)
    draw.text((sy['attr_3']['x'] - w/2 - sy['attr_3']['offset'], sy['attr_3']['y']), msg, font = font, fill = sy['attr_3']['hp_color'])
    msg = "RES: " + str(ay['attr']['res'])
    w, h = draw.textsize(msg, font = font)
    draw.text((sy['attr_3']['x'] - w/2 + sy['attr_3']['offset'], sy['attr_3']['y']), msg, font = font, fill = sy['attr_3']['res_color'])

    template.save("out/final_" + processed_char_name + ".png")