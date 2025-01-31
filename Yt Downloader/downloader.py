import validators
from pytubefix import YouTube

def valid_URL(link: str) -> bool:
    return validators.url(link)

def yt_downloader(link):
    if valid_URL(link):
        print("Valid URL.")
        try:
            print(" Proceeding with download.")
            yt = YouTube(link)
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path='C:/Users/hp/Documents/Python Training/Yt Downloader', filename= "test.mp4")
            print("Successful download.")
        except Exception as e:
            print(f"Error occurred: {e}")
            
    else:
        print("Invalid URL. Try again.")

link = str(input("Enter your youtube link: "))
yt_downloader(link)

