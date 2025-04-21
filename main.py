window_y = 900
window_x = 1400
window = display.set_mode((window_x, window_y))

finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
