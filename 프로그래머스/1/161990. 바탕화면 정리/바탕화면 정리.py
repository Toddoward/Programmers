def solution(wallpaper):
    lux = len(wallpaper)
    luy = len(wallpaper[0])
    rdx = 0
    rdy = 0
    
    for j in range(0, len(wallpaper[0])):
        for i in range(0, len(wallpaper)):
            if wallpaper[i][j] == "#":
                if i > rdx:rdx = i
                if i < lux:lux = i
                if j > rdy:rdy = j
                if j < luy:luy = j
    answer = [lux, luy, rdx + 1, rdy + 1]
    return answer