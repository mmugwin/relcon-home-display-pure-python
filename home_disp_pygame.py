import pygame
from math import radians, sin, cos

pygame.init()
screen_width = 320
screen_height = 240
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("RELCON InHome Display")

wifi_icon = pygame.image.load("./images/wifi_black_24dp.svg")
wifi_icon_x = 45
wifi_icon_y = 10

batt_icon = pygame.image.load("./images/battery_charging_full_black_24dp.svg")
batt_icon_x = 15
batt_icon_y = 10

background_img = pygame.image.load("./images/background.svg")
background_img = pygame.transform.scale(background_img, (320, 240))
background_x = 0
background_y = 0
pygame.font.get_fonts()
['arial', 'arialblack', 'bahnschrift', 'calibri', 'cambriacambriamath', 'cambria', 'candara', 'comicsansms', 'consolas', 'constantia', 'corbel', 'couriernew', 'ebrima', 'franklingothicmedium', 'gabriola', 'gadugi', 'georgia', 'impact', 'inkfree', 'javanesetext', 'leelawadeeui', 'leelawadeeuisemilight', 'lucidaconsole', 'lucidasans', 'malgungothic', 'malgungothicsemilight', 'microsofthimalaya', 'microsoftjhengheimicrosoftjhengheiui', 'microsoftjhengheimicrosoftjhengheiuibold', 'microsoftjhengheimicrosoftjhengheiuilight', 'microsoftnewtailue', 'microsoftphagspa', 'microsoftsansserif', 'microsofttaile', 'microsoftyaheimicrosoftyaheiui', 'microsoftyaheimicrosoftyaheiuibold', 'microsoftyaheimicrosoftyaheiuilight', 'microsoftyibaiti', 'mingliuextbpmingliuextbmingliuhkscsextb', 'mongolianbaiti', 'msgothicmsuigothicmspgothic', 'mvboli', 'myanmartext', 'nirmalaui', 'nirmalauisemilight', 'palatinolinotype', 'segoemdl2assets', 'segoeprint', 'segoescript', 'segoeui', 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 'segoeuisemibold', 'segoeuisemilight', 'segoeuisymbol', 'simsunnsimsun', 'simsunextb', 'sitkasmallsitkatextsitkasubheadingsitkaheadingsitkadisplaysitkabanner', 'sitkasmallsitkatextboldsitkasubheadingboldsitkaheadingboldsitkadisplayboldsitkabannerbold', 'sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic', 'sitkasmallsitkatextitalicsitkasubheadingitalicsitkaheadingitalicsitkadisplayitalicsitkabanneritalic', 'sylfaen', 'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana', 'webdings', 'wingdings', 'yugothicyugothicuisemiboldyugothicuibold', 'yugothicyugothicuilight', 'yugothicmediumyugothicuiregular', 'yugothicregularyugothicuisemilight', 'dengxian', 'fangsong', 'kaiti', 'simhei', 'holomdl2assets', 'extra', 'fzshuti', 'fzyaoti', 'lisu', 'stcaiyun', 'stfangsong', 'sthupo', 'stkaiti', 'stliti', 'stsong', 'stxihei', 'stxingkai', 'stxinwei', 'stzhongsong', 'youyuan', 'haettenschweiler', 'msoutlook', 'bookantiqua', 'centurygothic', 'bookshelfsymbol7', 'msreferencesansserif', 'msreferencespecialty', 'garamond', 'monotypecorsiva', 'bookmanoldstyle', 'algerian', 'baskervilleoldface', 'bauhaus93', 'bell', 'berlinsansfb', 'berlinsansfbdemi', 'bernardcondensed', 'bodonipostercompressed', 'britannic', 'broadway', 'brushscript', 'californianfb', 'centaur', 'chiller', 'colonna', 'cooperblack', 'footlight', 'freestylescript', 'harlowsolid', 'harrington', 'hightowertext', 'jokerman', 'juiceitc', 'kristenitc', 'kunstlerscript', 'lucidabright', 'lucidacalligraphy', 'lucidafaxregular', 'lucidafax', 'lucidahandwriting', 'magneto', 'maturascriptcapitals', 'mistral', 'modernno20', 'niagaraengraved', 'niagarasolid', 'oldenglishtext', 'onyx', 'parchment', 'playbill', 'poorrichard', 'ravie', 'informalroman', 'showcardgothic', 'snapitc', 'stencil', 'tempussansitc', 'vinerhanditc', 'vivaldi', 'vladimirscript', 'widelatin', 'century', 'wingdings2', 'wingdings3', 'arialms', 'msmincho', 'acaderef', 'aigdt', 'amdtsymbols', 'geniso', 'amgdt', 'bankgothic', 'bankgothicmedium', 'cityblueprint', 'commercialpi', 'commercialscript', 'countryblueprint', 'dutch801roman', 'dutch801', 'dutch801extra', 'euroroman', 'euroromanoblique', 'monospace821', 'panroman', 'romantic', 'romans', 'sansserif', 'sansserifboldoblique', 'sansserifoblique', 'stylus', 'superfrench', 'swiss721', 'swiss721outline', 'swiss721condensed', 'swiss721condensedoutline', 'swiss721blackcondensed', 'swiss721extended', 'swiss721blackextended', 'swiss721black', 'swiss721blackoutline', 'technicbold', 'techniclite', 'technic', 'universalmath1', 'vineta', 'isocpeur', 'isocteur', 'proxy9', 'proxy8', 'proxy7', 'proxy6', 'proxy5', 'proxy4', 'proxy3', 'symusic', 'symeteo', 'symath', 'symap', 'syastro', 'romant', 'romand', 'romanc', 'italict', 'greeks', 'greekc', 'gothicg', 'gothice', 'txt', 'simplex', 'scripts', 'scriptc', 'proxy2', 'proxy1', 'monotxt', 'italicc', '', 'isoct3', 'isoct2', 'isoct', 'isocp3', 'isocp2', 'isocp', 'gothici', 'gdt', 'complex', 'thcadsymbsttf', 'thcadsymbs', 'zwadobef', 'eurosign', 'lucidabrightregular', 'lucidasansregular', 'lucidasanstypewriter', 'lucidasanstypewriterregular', 'adobeheitistdregular', 'adobemingstdlight', 'adobemyungjostdmedium', 'adobepistd', 'adobesongstdlight', 'courierstd', 'courierstdbold', 'courierstdboldoblique', 'courierstdoblique', 'kozgopr6nmedium', 'kozminpr6nregular', 'myriadcad', 'hyswlongfangsong', 'swastro', 'olfsimplesansocregular', 'swcomp', 'swgothe', 'swgothg', 'swgothi', 'swgrekc', 'swgreks', 'swisop1', 'swisop2', 'swisop3', 'swisot1', 'swisot2', 'swisot3', 'swital', 'switalc', 'switalt', 'swmap', 'swmath', 'swmeteo', 'swmono', 'swmusic', 'swromnc', 'swromnd', 'swromns', 'swromnt', 'swscrpc', 'swscrps', 'swsimp', 'swtxt', 'swgdt', 'swlink', 'dejavusansmono', 'dejavusansmonooblique', 'freesans']

header_font = pygame.font.SysFont('bahnschrift', 12)
usage_font = pygame.font.SysFont('bahnschrift', 20)
footer_font = pygame.font.SysFont('bahnschrift', 12)

title = "RELCON Homebox #"
box_num = 4

######
batt_status = 1 
connection_status = 0

######

def render_icons(batt_status, connection_status):
    if batt_status:
        batt_icon = pygame.image.load("./images/battery_charging_full_black_24dp.svg")
    else:
        batt_icon = pygame.image.load("./images/battery_5_bar_black_24dp.svg")

    if connection_status:
        wifi_icon = pygame.image.load("./images/wifi_black_24dp.svg")
    else:
        wifi_icon = pygame.image.load("./images/wifi_off_black_24dp.svg")
    
    screen.blit(wifi_icon, (wifi_icon_x, wifi_icon_y))
    screen.blit(batt_icon, (batt_icon_x, batt_icon_y))

def render_text():
    header_x = 100
    header_y = 12
    usage_x = 130 
    usage_y = 50
    footer_x = 130
    footer_y = 205

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
    drawArc(screen, 225, -45, 60, [screen_width/2, screen_height/2 + 22], (72, 72, 72), thickness=10)
    drawArc(screen, 225, 225-30, 60, [screen_width/2, screen_height/2 + 22], (0, 128, 0), thickness=10)
    
    pygame.display.update()