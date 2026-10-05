import os
import time

STREAM_KEY = os.environ.get("YOUTUBE_STREAM_KEY")
VIDEO_URL = "https://www.mediafire.com/file/ir6xdja088p2vi3/hasil_combiner_compressed.mp4/file"

def start_streaming():
    command = (
        f"ffmpeg -re -stream_loop -1 -i \"{VIDEO_URL}\" "
        f"-c:v libx264 -preset ultrafast -b:v 2000k -maxrate 2000k -bufsize 4000k "
        f"-pix_fmt yuv420p -g 60 -c:a aac -b:a 128k -ar 44100 "
        f"-f flv rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"
    )
    
    print("Memulai live streaming otomatis...")
    os.system(command)

if __name__ == "__main__":
    start_streaming()
