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
pygame.display.set_caption("RELCON InHome Display")

path = "/home/pi/Desktop/relcon-home-display-pure-python"
# path = "."

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

header_font = pygame.font.SysFont('dejavusansmono', 35)
usage_font = pygame.font.SysFont('dejavusansmono', 47)
footer_font = pygame.font.SysFont('dejavusansmono', 30)
curr_power_font = pygame.font.SysFont('liberationmono', 60)

##########################
title = "RELCON Homebox #"
##########################

def render_icons(batt_status, connection_status):
    if batt_status:
        batt_icon = pygame.image.load(path + "/images/sharp_battery_charging_full_black_24dp.png")
    else:
        batt_icon = pygame.image.load(path + "/images/sharp_battery_3_bar_black_24dp.png")

    if connection_status:
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
        bigger = start_angle
    else:
        theta = start_angle
        bigger = end_angle
        
    while theta < bigger: 
        for t in range(thickness):
            x = round((cos(radians(theta)) * (distance-t)) + pos[0])
            y = round((-sin(radians(theta)) * (distance-t)) + pos[1])
            display.set_at((x, y), color)
            theta += 0.01

def check_keys(data):
    keys = ['"curr_power"', '"link_status"', '"conn"', '"box_num"', '"batt_percent"']
    for key in keys:
        if key not in data:
            print(key)
            return False
    return True

def check_val_type(data):
    keys = {"curr_power": "<class 'float'>", "link_status": "<class 'int'>", "conn": "<class 'int'>", "box_num": "<class 'int'>", "batt_percent": "<class 'float'>"}
    for key in keys:
        tmp = str(type(data[key]))
        if tmp != keys[key]:
            print('bad val')
            return False
    return True

def check_power_status(curr_power_usage):
    power_status = []
    if curr_power_usage > 270:
        power_status.append((200, 0, 0))
    elif curr_power_usage > 220:
        power_status.append((255, 191, 0))
    else:
        power_status.append((0, 128, 0))

    if curr_power_usage < 100:
        curr_power_x = 250
    elif curr_power_usage < 200:
        curr_power_x = 230
    else:
        curr_power_x = 230  
    power_status.append(curr_power_x)
    return power_status

def update_data():
    power_limit = 300
    try:
        ser = serial.Serial('/dev/ttyS0',
                            baudrate = 9600)
        data = ser.read_until(b'\n').decode('ascii', 'ignore')
        print(data)

        if check_keys(data) == False:
            ser.close()
            return

        data =  list(data)
        data = ''.join(data)
        data = json.loads(data)

        if check_val_type(data) == False:
            ser.close()
            return

        curr_power_usage = data['curr_power']
        power_status = check_power_status(curr_power_usage)
        comms_connection = data['link_status']
        hub_connection = data['conn']
        box_num = data['box_num']
        render_text(box_num)
        render_icons(hub_connection, comms_connection)

        color = power_status[0]    
        curr_power_x = power_status[1]
        curr_power_y = 250    
        curr_power_tag = curr_power_font.render(str(curr_power_usage) + " W", True, (255, 255, 255))
        screen.blit(curr_power_tag, (curr_power_x, curr_power_y))
        draw_arc(screen, 225, 225-curr_power_usage, 120, [screen_width/2, screen_height/2 + 40 + 10], color, thickness = 15)      

        ser.close()

    except:
        curr_power_usage = random.randint(1, power_limit)
        curr_power_usage = int(curr_power_usage/power_limit * 270)
        power_status = check_power_status(curr_power_usage)
        connection_status = 0
        box_num = 2

        comms_connection = 0
        hub_connection = 0
        render_text(box_num)
        render_icons(hub_connection, comms_connection)

        color = power_status[0]    
        curr_power_x = power_status[1]
        curr_power_y = 250    
        curr_power_tag = curr_power_font.render(str(curr_power_usage) + " W", True, (255, 255, 255))
        screen.blit(curr_power_tag, (curr_power_x, curr_power_y))
        draw_arc(screen, 225, 225-curr_power_usage, 120, [screen_width/2, screen_height/2 + 40 + 10], color, thickness = 15)
   
running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(background_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_arc(screen, 225, -45, 120, [screen_width/2, screen_height/2 + 40 + 10], (72, 72, 72), thickness = 15)
    update_data()
    pygame.display.update()
    time.sleep(4)