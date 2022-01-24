from colorgram import extract

colors = extract('damien-hirst-bromobenzotrifluoride.jpg', 30)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))


print(rgb_colors)