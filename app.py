
import os

def set_wallpaper(image_path):
    script = f"""
    tell application "System Events"
        tell current desktop
            set picture to "{image_path}"
        end tell
    end tell
    """
    os.system(f"osascript -e '{script}'")

# # Replace this with the actual path to your image file
# image_path = "img.jpeg"

# set_wallpaper(image_path)
