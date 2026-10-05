import os
import time

STREAM_KEY = os.environ.get("YOUTUBE_STREAM_KEY")
# Link video sample untuk uji coba awal
VIDEO_URL = "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4"

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
```[cite: 6]

3. Geser layar ke pojok kanan atas, klik tombol hijau **Commit changes...**, lalu klik sekali lagi **Commit changes** pada jendela kecil yang muncul.

Jika sudah selesai, kabari saya ya agar kita bisa lanjut membuat file konfigurasi otomatisnya yang kedua!
