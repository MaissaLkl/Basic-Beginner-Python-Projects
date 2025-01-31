import validators
import yt_dlp

def valid_URL(link: str) -> bool:
    return validators.url(link)

def yt_downloader(link):
    if valid_URL(link):
        print("Valid URL.")
        try:
            print(" Proceeding with download.")
            ydl_opts = {'format': 'best', 
                        'outtmpl': 'C:/Users/hp/Documents/Python Training/Yt Downloader/%(title)s.%(ext)s',  # Use video title for filename
                        'postprocessors':  [{
                                            'key': 'FFmpegVideoConvertor',
                                            'preferedformat': 'mp4',
                                            'preferedquality': 'best',  # Attempt to keep the best quality
                                           }],
                        'noplaylist': True,
                        }
            yt = yt_dlp.YoutubeDL(ydl_opts)
            yt.download(link)
            print("Successful download.")
        except Exception as e:
            print(f"Error occurred: {e}")
            
    else:
        print("Invalid URL. Try again.")

link = str(input("Enter your YouTube link: "))
yt_downloader(link)

