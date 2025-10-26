from PIL import ImageGrab
import numpy as np
import pyautogui as at
import time
z=0
x='x'
n=1000000
at.click(245,435)
ss= ImageGrab.grab()
table=[]
row=[]
for i in range(318,640,40):
    for j in range (100,421,40):
        if ss.getpixel((j,i))==(0,0,255):
            row.append(1)
        elif ss.getpixel((j,i))==(0,123,0):
            row.append(2)
        elif ss.getpixel((j,i))==(255,0,0):
            row.append(3)
        elif ss.getpixel((j,i))==(0,0,123):
            row.append(4)
        else:
            if ss.getpixel((j,i-26))==(255,255,255):
                row.append(x)
            else:
                row.append(0)
    table.append(row)
    row=[]

def neighbour(matrix, row, col):
    neighbor_values = []
    neighbor_coords = []
    
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0
    
    neighbor_offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    for dr, dc in neighbor_offsets:
        nr, nc = row + dr, col + dc
        if 0 <= nr < num_rows and 0 <= nc < num_cols:
            neighbor_values.append(matrix[nr][nc])
            neighbor_coords.append((nr, nc))
    
    return neighbor_values, neighbor_coords

def coords(data, target_string):
    coords = [
        (row_index, col_index)
        for row_index, inner_list in enumerate(data)
        for col_index, value in enumerate(inner_list)
        if value == target_string
    ]
    return coords

def change(table, target_value, new_value):
    for r, row in enumerate(table):
        for c, val in enumerate(row):
            if val == target_value:
                table[r][c] = new_value

def close(c1, c2, tol=25):
    return all(abs(a - b) <= tol for a, b in zip(c1, c2))

a=coords(table,1)
b=coords(table,2)
c=coords(table,3)
d=coords(table,4)
while table.count('#')<10:
    while z<len(a):
        coord=a[z]
        values, coords_list = neighbour(table,coord[0],coord[1])
        print(coords_list)
        print(values)
        if values.count('x') + values.count('#') == 1:
            print('proceeded1')
            for (nr, nc), val in zip(coords_list, values):
                if table[nr][nc] == 'x':
                    table[nr][nc] = '#'
                    print(f"made ({nr},{nc}) '#'")
                    if table[nr][nc] != '#' and table[nr][nc] != 0:
                        screen_x = 100 + nc * 40
                        screen_y = 318 + nr * 40
                        at.click(screen_x, screen_y)
                        print(f"Clicked at ({nr}, {nc})")
                        ss= ImageGrab.grab()
                        if close(ss.getpixel((screen_x, screen_y)), (0,0,255)):
                            table[nr][nc] = 1
                            print('revealed 1')
                        elif close(ss.getpixel((screen_x, screen_y)), (0,123,0)):
                            table[nr][nc] = 2
                            print('revealed 2')
                        elif close(ss.getpixel((screen_x, screen_y)), (255,0,0)):
                            table[nr][nc] = 3
                            print('revealed 3')
                        elif close(ss.getpixel((screen_x, screen_y)), (0,0,123)):
                            table[nr][nc] = 4
                            print('revealed 4')
        elif values.count('#') == 1:
            print('proceeded12')
            for (nr, nc), val in zip(coords_list, values):
                if table[nr][nc] == 'x':
                    screen_x = 100 + nc * 40
                    screen_y = 318 + nr * 40
                    at.click(screen_x, screen_y)
                    print(f"Clicked at ({nr}, {nc})")
                    ss= ImageGrab.grab()
                    ss.save("screenshot.png")
                    if close(ss.getpixel((screen_x, screen_y)), (0,0,255)):
                        table[nr][nc] = 1
                        print('revealed 1')
                    elif close(ss.getpixel((screen_x, screen_y)), (0,123,0)):
                        table[nr][nc] = 2
                        print('revealed 2')
                    elif close(ss.getpixel((screen_x, screen_y)), (255,0,0)):
                        table[nr][nc] = 3
                        print('revealed 3')
                    elif close(ss.getpixel((screen_x, screen_y)), (0,0,123)):
                        table[nr][nc] = 4
                        print('revealed 4')
        z+=1
    z=0
    while z<len(b):
        coord=b[z]
        values, coords_list = neighbour(table,coord[0],coord[1])
        print(coords_list)
        print(values)
        if values.count('x') + values.count('#') == 2:
            print('proceeded2')
            for (nr, nc), val in zip(coords_list, values):
                if table[nr][nc] == 'x':
                    table[nr][nc] = '#'
                    print(f"made ({nr},{nc}) '#'")
                    if table[nr][nc] != '#' and table[nr][nc] != 0:
                        screen_x = 100 + nc * 40
                        screen_y = 318 + nr * 40
                        at.click(screen_x, screen_y)
                        print(f"Clicked at ({nr}, {nc})")
                        ss= ImageGrab.grab()
                        if close(ss.getpixel((screen_x, screen_y)), (0,0,255)):
                            table[nr][nc] = 1
                            print('revealed 1')
                        elif close(ss.getpixel((screen_x, screen_y)), (0,123,0)):
                            table[nr][nc] = 2
                            print('revealed 2')
                        elif close(ss.getpixel((screen_x, screen_y)), (255,0,0)):
                            table[nr][nc] = 3
                            print('revealed 3')
                        elif close(ss.getpixel((screen_x, screen_y)), (0,0,123)):
                            table[nr][nc] = 4
                            print('revealed 4')
        elif values.count('#') == 2:
            print('proceeded22')
            for (nr, nc), val in zip(coords_list, values):
                if table[nr][nc] == 'x':
                    screen_x = 100 + nc * 40
                    screen_y = 318 + nr * 40
                    at.click(screen_x, screen_y)
                    print(f"Clicked at ({nr}, {nc})")
                    ss= ImageGrab.grab()
                    if close(ss.getpixel((screen_x, screen_y)), (0,0,255)):
                        table[nr][nc] = 1
                        print('revealed 1')
                    elif close(ss.getpixel((screen_x, screen_y)), (0,123,0)):
                        table[nr][nc] = 2
                        print('revealed 2')
                    elif close(ss.getpixel((screen_x, screen_y)), (255,0,0)):
                        table[nr][nc] = 3
                        print('revealed 3')
                    elif close(ss.getpixel((screen_x, screen_y)), (0,0,123)):
                        table[nr][nc] = 4
                        print('revealed 4')
        z+=1
    z=0
    while z<len(c):
        coord=c[z]
        values, coords_list = neighbour(table,coord[0],coord[1])
        print(coords_list)
        print(values)
        if values.count('x') + values.count('#') == 3:
            print('proceeded3')
            for (nr, nc), val in zip(coords_list, values):
                if table[nr][nc] == 'x':
                    table[nr][nc] = '#'
                    print(f"made ({nr},{nc}) '#'")
                    if table[nr][nc] != '#' and table[nr][nc] != 0:
                        screen_x = 100 + nc * 40
                        screen_y = 318 + nr * 40
                        at.click(screen_x, screen_y)
                        print(f"Clicked at ({nr}, {nc})")
                        ss= ImageGrab.grab()
                        if close(ss.getpixel((screen_x, screen_y)), (0,0,255)):
                            table[nr][nc] = 1
                            print('revealed 1')
                        elif close(ss.getpixel((screen_x, screen_y)), (0,123,0)):
                            table[nr][nc] = 2
                            print('revealed 2')
                        elif close(ss.getpixel((screen_x, screen_y)), (255,0,0)):
                            table[nr][nc] = 3
                            print('revealed 3')
                        elif close(ss.getpixel((screen_x, screen_y)), (0,0,123)):
                            table[nr][nc] = 4
                            print('revealed 4')
        elif values.count('#') == 3:
            print('proceeded32')
            for (nr, nc), val in zip(coords_list, values):
                if table[nr][nc] == 'x':
                    screen_x = 100 + nc * 40
                    screen_y = 318 + nr * 40
                    at.click(screen_x, screen_y)
                    print(f"Clicked at ({nr}, {nc})")
                    ss= ImageGrab.grab()
                    if close(ss.getpixel((screen_x, screen_y)), (0,0,255)):
                        table[nr][nc] = 1
                        print('revealed 1')
                    elif close(ss.getpixel((screen_x, screen_y)), (0,123,0)):
                        table[nr][nc] = 2
                        print('revealed 2')
                    elif close(ss.getpixel((screen_x, screen_y)), (255,0,0)):
                        table[nr][nc] = 3
                        print('revealed 3')
                    elif close(ss.getpixel((screen_x, screen_y)), (0,0,123)):
                        table[nr][nc] = 4
                        print('revealed 4')
        z+=1
    z=0
    while z<len(d):
        coord=d[z]
        values, coords_list = neighbour(table,coord[0],coord[1])
        print(coords_list)
        print(values)
        if values.count('x') + values.count('#') == 4:
            print('proceeded4')
            for (nr, nc), val in zip(coords_list, values):
                if table[nr][nc] == 'x':
                    table[nr][nc] = '#'
                    print(f"made ({nr},{nc}) '#'")
                    if table[nr][nc] != '#' and table[nr][nc] != 0:
                        screen_x = 100 + nc * 40
                        screen_y = 318 + nr * 40
                        at.click(screen_x, screen_y)
                        print(f"Clicked at ({nr}, {nc})")
                        ss= ImageGrab.grab()
                        if close(ss.getpixel((screen_x, screen_y)), (0,0,255)):
                            table[nr][nc] = 1
                            print('revealed 1')
                        elif close(ss.getpixel((screen_x, screen_y)), (0,123,0)):
                            table[nr][nc] = 2
                            print('revealed 2')
                        elif close(ss.getpixel((screen_x, screen_y)), (255,0,0)):
                            table[nr][nc] = 3
                            print('revealed 3')
                        elif close(ss.getpixel((screen_x, screen_y)), (0,0,123)):
                            table[nr][nc] = 4
                            print('revealed 4')
        elif values.count('#') == 4:
            print('proceeded42')
            for (nr, nc), val in zip(coords_list, values):
                if table[nr][nc] == 'x':
                    screen_x = 100 + nc * 40
                    screen_y = 318 + nr * 40
                    at.click(screen_x, screen_y)
                    print(f"Clicked at ({nr}, {nc})")
                    ss= ImageGrab.grab()
                    if close(ss.getpixel((screen_x, screen_y)), (0,0,255)):
                        table[nr][nc] = 1
                        print('revealed 1')
                    elif close(ss.getpixel((screen_x, screen_y)), (0,123,0)):
                        table[nr][nc] = 2
                        print('revealed 2')
                    elif close(ss.getpixel((screen_x, screen_y)), (255,0,0)):
                        table[nr][nc] = 3
                        print('revealed 3')
                    elif close(ss.getpixel((screen_x, screen_y)), (0,0,123)):
                        table[nr][nc] = 4
                        print('revealed 4')
        z+=1
    z=0
ss= ImageGrab.grab()
table=[]
row=[]
for i in range(318,640,40):
    for j in range (100,421,40):
        color = ss.getpixel((j, i))
        if close(color, (0,0,255)):     
            row.append(1)
        elif close(color, (0,123,0)):    
            row.append(2)
        elif close(color, (255,0,0)):   
            row.append(3)
        elif close(color, (0,0,123)):    
            row.append(4)
        else:
            above = ss.getpixel((j, i-26))
            if close(above, (255,255,255)):
                row.append('x')
            else:
                row.append(0)
    row=[]
