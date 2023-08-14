
script = f"""/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

def set_wallpaper(file_path):
        import subprocess
        subprocess.Popen(script%file_path, shell=True)
        print('Wallpaper set to ' + file_path)
