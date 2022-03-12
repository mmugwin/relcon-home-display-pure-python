import pygame
from math import radians, sin, cos

pygame.init()
screen_width = 320*2
screen_height = 240*2
# screen = pygame.display.set_mode((screen_width, screen_height))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("RELCON InHome Display")

wifi_icon = pygame.image.load("./images/outline_wifi_black_24dp.png")
wifi_icon_x = 45*2
wifi_icon_y = 10*2

batt_icon = pygame.image.load("./images/battery_charging_full_black_24dp.svg")
batt_icon_x = 15*2
batt_icon_y = 10*2

background_img = pygame.image.load("./images/background.png")
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))
background_x = -5
background_y = 0
pygame.font.get_fonts()
['arial', 'arialblack', 'bahnschrift']

header_font = pygame.font.SysFont('bahnschrift', 28)
usage_font = pygame.font.SysFont('bahnschrift', 20*2)
footer_font = pygame.font.SysFont('bahnschrift', 12*2)

title = "RELCON Homebox #"
box_num = 4

######
batt_status = 0 
connection_status = 0

######

def render_icons(batt_status, connection_status):
    if batt_status:
        batt_icon = pygame.image.load("./images/sharp_battery_charging_full_black_24dp.png")
    else:
        batt_icon = pygame.image.load("./images/sharp_battery_3_bar_black_24dp.png")

    if connection_status:
        wifi_icon = pygame.image.load("./images/outline_wifi_black_24dp.png")
    else:
        wifi_icon = pygame.image.load("./images/outline_wifi_off_black_24dp.png")
    
    screen.blit(wifi_icon, (wifi_icon_x, wifi_icon_y))
    screen.blit(batt_icon, (batt_icon_x, batt_icon_y))

def render_text():
    header_x = 100*2
    header_y = 12*2
    usage_x = 130*2
    usage_y = 50*2
    footer_x = 130*2
    footer_y = 205*2

    header = header_font.render(title + str(box_num), True, (0,0,0))
    usage_tag = usage_font.render("USAGE", True, (255, 255, 255))
    footer_tag = footer_font.render("Limit: 300 W", True, (255, 255, 255))

    screen.blit(usage_tag, (usage_x, usage_y))
    screen.blit(footer_tag, (footer_x, footer_y))
    screen.blit(header, (header_x, header_y))

def drawArc(display, startAngle, endAngle, distance, pos, color, thickness=1):
    if startAngle > endAngle:
        theta = endAngle
        bigger = startAngle
    else:
        theta = startAngle
        bigger = endAngle
        
    while theta < bigger: 
        for t in range(thickness):
            x = round((cos(radians(theta)) * (distance-t)) + pos[0])
            y = round((-sin(radians(theta)) * (distance-t)) + pos[1])
            display.set_at((x, y), color)
            theta += 0.01

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(background_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    render_icons(batt_status, connection_status)
    render_text()
    drawArc(screen, 225, -45, 60*2, [screen_width/2, screen_height/2 + 22*2], (72, 72, 72), thickness = 15)
    drawArc(screen, 225, 225-30, 60*2, [screen_width/2, screen_height/2 + 22*2], (0, 128, 0), thickness = 15)
    
    pygame.display.update()