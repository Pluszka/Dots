from colorgram import extract

colors = extract('damien-hirst-bromobenzotrifluoride.jpg', 30)

rgb_colors = []

for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)