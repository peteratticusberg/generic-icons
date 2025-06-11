import os
import random
from PIL import Image

# Configuration
input_dir = os.path.dirname(os.path.abspath(__file__))  # Set to current script directory
output_dir = f"{input_dir}/output"
brightness_threshold = (153, 153, 153)  # RGB equivalent of #999999

#hex_colors = ["#FF0000", "#FF4000", "#FF8000", "#FFBF00", "#FFFF00", "#BFFF00", "#80FF00", "#40FF00", "#00FF00", "#00FF40", "#00FF80", "#00FFBF", "#00FFFF", "#00BFFF", "#0080FF", "#0040FF", "#0000FF", "#4000FF", "#8000FF", "#BF00FF", "#FF00FF", "#FF00BF", "#FF0080", "#FF0040", "#FF3333", "#FF6633", "#FF9933", "#FFCC33", "#CCFF33", "#99FF33", "#66FF33", "#33FF33", "#33FF66", "#33FF99", "#33FFCC", "#33FFFF", "#3399FF", "#3366FF", "#3333FF", "#6633FF", "#9933FF", "#CC33FF"]
rgb_colors = [(255, 0, 0), (255, 64, 0), (255, 128, 0), (255, 191, 0), (255, 255, 0), (191, 255, 0), (128, 255, 0), (64, 255, 0), (0, 255, 0), (0, 255, 64), (0, 255, 128), (0, 255, 191), (0, 255, 255), (0, 191, 255), (0, 128, 255), (0, 64, 255), (0, 0, 255), (64, 0, 255), (128, 0, 255), (191, 0, 255), (255, 0, 255), (255, 0, 191), (255, 0, 128), (255, 0, 64), (255, 51, 51), (255, 102, 51), (255, 153, 51), (255, 204, 51), (204, 255, 51), (153, 255, 51), (102, 255, 51), (51, 255, 51), (51, 255, 102), (51, 255, 153), (51, 255, 204), (51, 255, 255), (51, 153, 255), (51, 102, 255), (51, 51, 255), (102, 51, 255), (153, 51, 255), (204, 51, 255)]
# Make output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Process each PNG file
i = 0
for filename in os.listdir(input_dir):
    if filename.lower().endswith('.png'):
        img_path = os.path.join(input_dir, filename)
        img = Image.open(img_path).convert('RGBA')  # Ensure alpha channel is preserved

        pixels = img.load()
        width, height = img.size
        print(f"hello {i}")
        new_color = rgb_colors[i-1]

        for y in range(height):
            for x in range(width):
                r, g, b, a = pixels[x, y]
                if (r, g, b) > brightness_threshold:
                    pixels[x, y] = (*new_color, a)

        output_path = os.path.join(output_dir, f"{filename}")
        img.save(output_path)
        i += 1

print("Processing complete.")