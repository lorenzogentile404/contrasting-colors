# This script prints a series of contrasting colors uniformly distributed over the three dimensions of RGB
# RGB values of the starting color
r = 255
g = 0
b = 0
k = 50 # Number of contrasting colors to print

def print_rgb(r, g, b):
    text = "■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■"
    # Using ANSI escape codes to set RGB color
    print(f"\033[38;2;{r};{g};{b}m{text}\033[0m")

r_is_low = r < 255//k
g_is_low = g < 255//k
b_is_low = b < 255//k
for i in range(0, k+1):
    delta = 255//k*i
    r_c = (r+delta) % 256 if r_is_low else (r-delta) % 256
    g_c = (g+delta) % 256 if g_is_low else (g-delta) % 256
    b_c = (b+delta) % 256 if b_is_low else (b-delta) % 256  
    print("RGB_" + str(i) + " = (" + str(r_c) + ", " + str(g_c) + ", " + str(b_c) + ") delta = " + str(delta))
    print_rgb(r_c, g_c, b_c)