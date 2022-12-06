picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

blank = " "
fill = "*"

for row in picture:
    for pixel in row:
        if pixel == 1:
            print(fill, end="") 
        else:
            print(blank, end="")
    print("") ## COLLUMS