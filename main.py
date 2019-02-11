from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

# I
# draw_line(0,0,500,100,screen,color)

# II
# draw_line(0,0,100,500,screen,color)

# VIII
# draw_line(0,500,100,0,screen,color)

# VII
# draw_line(0,500,500,400,screen,color)


for i in range (0,500,10):
	for j in range (0,500,10):
		draw_line(250,250,i,j,screen, color)


display(screen)
save_extension(screen, 'img.png')
