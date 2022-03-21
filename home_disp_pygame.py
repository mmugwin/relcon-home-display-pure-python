'''
    This script displays electrical measurements read as serial data from the homebox.
    Author:
        Ngoni Mugwisi - 11/03/2022
'''

import pygame
import random
import time
import serial
import json
from math import radians, sin, cos

pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("RELCON InHome Display")

path = "/home/pi/Desktop/relcon-home-display-pure-python"
#path = "."             # uncomment this for testing on Windows

# initialize the default icons (wifi, battery) and background images
wifi_icon = pygame.image.load(path + "/images/outline_wifi_black_24dp.png")
wifi_icon_x = 90
wifi_icon_y = 20

batt_icon = pygame.image.load(path + "/images/battery_charging_full_black_24dp.svg")
batt_icon_x = 30
batt_icon_y = 20

background_img = pygame.image.load(path + "/images/background.svg")
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))
background_x = -5
background_y = 0

pygame.font.get_fonts()
['arial', 'arialblack', 'bahnschrift']

# Declare the fonts and font sizes for the text on the screen
header_font = pygame.font.SysFont('dejavusansmono', 35)
usage_font = pygame.font.SysFont('dejavusansmono', 47)
footer_font = pygame.font.SysFont('dejavusansmono', 30)
curr_power_font = pygame.font.SysFont('liberationmono', 60)
welcome_font = pygame.font.SysFont('liberationmono', 31)

# Display a placeholder welcome message while the system turns on. Sleep for 10 seconds
pygame.mouse.set_visible(False)
screen.fill((255, 255, 255))
welcome_x = 180
welcome_y = 24

welcome_tag = curr_power_font.render("Welcome!", True, (0, 0, 0))
welcome_tag1 = welcome_font.render("Please wait. System loading.", True, (0, 0, 0))
welcome_tag2 = welcome_font.render("This may take up to 1 minute...", True, (0, 0, 0))

screen.blit(welcome_tag, (welcome_x, welcome_y))
screen.blit(welcome_tag1, (welcome_x - 120, welcome_y+120))
screen.blit(welcome_tag2, (welcome_x - 150, welcome_y+170))

pygame.mouse.set_visible(False)
pygame.display.update()


title = "RELCON Homebox #"

time.sleep(10)


def render_icons(batt_status, connection_status, batt_percent):
    print("Rendered Icons")
    if batt_status == 1:
        batt_icon = pygame.image.load(path + "/images/battery_charging_full_black_36dp.svg")
    else:
        if batt_percent > 90:
            batt_icon = pygame.image.load(path + "/images/battery_charging_full_black_36dp.svg")
        elif batt_percent > 70:
            batt_icon = pygame.image.load(path + "/images/battery_5_bar_black_36dp.svg")
        elif batt_percent > 60:
            batt_icon = pygame.image.load(path + "/images/battery_4_bar_black_36dp.svg")
        elif batt_percent > 50:
            batt_icon = pygame.image.load(path + "/images/battery_3_bar_black_36dp.svg")
        elif batt_percent > 30:
            batt_icon = pygame.image.load(path + "/images/battery_2_bar_black_36dp.svg")
        elif batt_percent > 10:
            batt_icon = pygame.image.load(path + "/images/battery_1_bar_black_36dp.svg")
        else:
            batt_icon = pygame.image.load(path + "/images/battery_unknown_black_36dp.svg")

    if connection_status == 1:
        wifi_icon = pygame.image.load(path + "/images/sharp_wifi_black_24dp.png")
    else:
        wifi_icon = pygame.image.load(path + "/images/sharp_wifi_off_black_24dp.png")
    
    screen.blit(wifi_icon, (wifi_icon_x, wifi_icon_y))
    screen.blit(batt_icon, (batt_icon_x, batt_icon_y))

def render_text(box_num):
    header_x = 180
    header_y = 24
    usage_x = 250
    usage_y = 100
    footer_x = 215
    footer_y = 410

    header = header_font.render(title + str(box_num), True, (0,0,0))
    usage_tag = usage_font.render("USAGE", True, (255, 255, 255))
    footer_tag = footer_font.render("Limit: 300 W", True, (255, 255, 255))

    screen.blit(usage_tag, (usage_x, usage_y))
    screen.blit(footer_tag, (footer_x, footer_y))
    screen.blit(header, (header_x, header_y))

def draw_arc(display, start_angle, end_angle, distance, pos, color, thickness = 1):
    if start_angle > end_angle:
        theta = end_angle
        larger_angle = start_angle
    else:
        theta = start_angle
        larger_angle = end_angle
        
    while theta < larger_angle: 
        for t in range(thickness):
            x = round((cos(radians(theta)) * (distance-t)) + pos[0])
            y = round((-sin(radians(theta)) * (distance-t)) + pos[1])
            display.set_at((x, y), color)
            theta += 0.01

def check_keys(data):
    '''
        checks whether all the keys in the serial string are present
        Returns True if so, False otherwise 
    '''
    keys = ['"error"','"curr_power"', '"link_status"', '"conn"', '"box_num"', '"batt_percent"']
    for key in keys:
        if key not in data:
            print(key)
            return False
    return True

def check_val_type(data):
    '''
        checks that all the data in the JSON serial string is of the correct type.
        Returns True if so, False otherwise 
    '''
    keys = {"error": "<class 'int'>","curr_power": "<class 'float'>", "link_status": "<class 'int'>", "conn": "<class 'int'>", "box_num": "<class 'int'>", "batt_percent": "<class 'float'>"}
    for key in keys:
        tmp = str(type(data[key]))
        if tmp != keys[key]:
            print('bad val')
            return False
    return True

def check_power_status(curr_power_usage):
    '''
        assigns the x coordinate and RBG color of the current power reading based on the value
    '''

    power_status = []
    if curr_power_usage > 270:
        power_status.append((200, 0, 0))
    elif curr_power_usage > 220:
        power_status.append((255, 191, 0))
    else:
        power_status.append((0, 128, 0))

    if curr_power_usage < 10:
        curr_power_x = 260
    elif curr_power_usage < 100:
        curr_power_x = 250
    elif curr_power_usage < 200:
        curr_power_x = 230
    else:
        curr_power_x = 230  
    power_status.append(curr_power_x)
    return power_status

def render_error_message(error):
    '''
        Displays the error code if there is an error.
        The display does not recover from this state, unless the homebox is rebooted
    '''

    error_x = 70
    error_y = 24
    error = hex(error)
    error_font = pygame.font.SysFont('dejavusansmono', 30)
    error_tag = error_font.render("An internal error occurred!", True, (255, 0, 0))
    recover_tag = error_font.render("Error Code: " + str(error), True, (255, 255, 255))
    screen.blit(error_tag, (error_x, error_y))
    screen.blit(recover_tag, (error_x + 30, 100))

def update_data():
    power_limit = 300

    try:
        ser = serial.Serial(port='/dev/ttyS0',
            baudrate = 115200,
            timeout = 4
        )
        
#         Uncomment to test on Windows
#         ser = serial.Serial(port='COM10',
#             baudrate=115200,
#             timeout=4
#         )

        data = ser.read_until(b'\n').decode('ascii', 'ignore')
        print(data)

        if check_keys(data) == False:
            ser.close()
            return 0

        data =  list(data)
        data = ''.join(data)
        data = json.loads(data)

        if check_val_type(data) == False:
            ser.close()
            return 0

        error = int(data["error"])
        if error != 0:
            render_error_message(error)
            ser.close()
            return 1

        curr_power_usage = round(float(data['curr_power']), 0)
        curr_power_usage = int(curr_power_usage)
        power_status = check_power_status(curr_power_usage)
        comms_connection = data['link_status']
        hub_connection = data['conn']
        box_num = data['box_num']
        batt_percent = float(data['batt_percent'])

        render_text(box_num)
        print("Trying to render icons")
        render_icons(hub_connection, comms_connection, batt_percent)

        color = power_status[0]    
        curr_power_x = power_status[1]
        curr_power_y = 250    
        curr_power_tag = curr_power_font.render(str(curr_power_usage) + " W", True, (255, 255, 255))
        screen.blit(curr_power_tag, (curr_power_x, curr_power_y))
        draw_arc(screen, 225, 225-curr_power_usage, 120, [screen_width/2, screen_height/2 + 40 + 10], color, thickness = 15)      

        ser.close()
        return 1

    except:
        pass

pygame.mouse.set_visible(False)
running = True
while running:
    pygame.mouse.set_visible(False)
    screen.fill((255, 255, 255))
    screen.blit(background_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # draw the default grey arc
    draw_arc(screen, 225, -45, 120, [screen_width/2, screen_height/2 + 40 + 10], (72, 72, 72), thickness = 15)
    
    # read the serial line and return 1 if the data is valid
    update_screen = update_data()
    pygame.mouse.set_visible(False)
    
    # if valid data has been read on the serial line, refresh the screen. 
    # otherwise, continue displaying the last valid reading
    if update_screen:
        pygame.display.update()
    time.sleep(4)
