import yt_dlp

url = "https://youtu.be/MrVB8ZktFIs?si=NedaIEPtBYzIIUKe"

try:
    # Create options for yt-dlp
    ydl_opts = {}

    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("Downloading video...")
        ydl.download([url])
        
    print("Download complete!")
except Exception as e:
    print(f"An error occurred: {e}")
