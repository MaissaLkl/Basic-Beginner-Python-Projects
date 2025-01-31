# 🎥 YouTube Video Downloader

A lightweight and efficient Python-based YouTube video downloader with two implementation options:
* **PyTubeFix** – Simple and lightweight
* **yt-dlp** – Feature-rich and well-maintained

Both versions validate URLs before downloading and fetch videos in the highest available quality.

## ✨ Features

* **Supports two implementations:**
  * PyTubeFix – Basic functionality, lightweight
  * yt-dlp – More features, better maintenance
* **High-quality downloads** – Fetches the best available resolution
* **Custom output directory** – Save videos anywhere on your system
* **MP4 conversion** (yt-dlp version) – Ensures compatibility
* **Robust error handling** – Handles invalid URLs, network failures, and file issues

## 📌 Prerequisites

Before using this downloader, ensure you have:

* Python 3.x installed
* FFmpeg (required for the yt-dlp version)
* Required Python packages (listed in requirements.txt)

## 🛠 FFmpeg Installation

* **Windows**: Download from FFmpeg's website
* **Linux**: Install via terminal:
  ```bash
  sudo apt-get install ffmpeg
  ```
* **macOS**: Install using Homebrew:
  ```bash
  brew install ffmpeg
  ```

## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/youtube-video-downloader.git
cd youtube-video-downloader
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 🎬 Usage

Choose between the PyTubeFix or yt-dlp version:

### PyTubeFix Version
```bash
python pytube_downloader.py
```

### yt-dlp Version
```bash
python ytdlp_downloader.py
```

Steps:
1. Run the script
2. Enter the YouTube video URL when prompted
3. Wait for the download to complete
4. Find the downloaded video in the output directory

## ⚙️ Configuration

### Default Output Path
Both versions store downloads in:

```bash
C:/Users/hp/Documents/Python Training/Yt Downloader
```

### PyTubeFix Version
* Saves as test.mp4
* Modify output path in pytube_downloader.py:
  ```python
  stream.download(output_path='YOUR_CUSTOM_PATH')
  ```

### yt-dlp Version
* Saves as %(title)s.%(ext)s (video title as filename)
* Downloads in the best available format
* Converts to MP4 automatically
* Modify output path in ytdlp_downloader.py:
  ```python
  'outtmpl': 'YOUR_CUSTOM_PATH/%(title)s.%(ext)s'
  ```

### Additional yt-dlp Options
The yt-dlp version supports:
* Custom format selection
* Post-processing (e.g., audio extraction)
* Playlist downloading
* Quality preferences

Modify ytdlp_downloader.py to tweak these settings.

## 🛠 Error Handling

Both versions include robust error handling for:
* Invalid URLs
* Download failures
* Network issues
* File system errors

## 🔍 Version Comparison

| Feature | PyTubeFix | yt-dlp |
|---------|-----------|--------|
| Ease of Use | ✅ Simple | ⚠️ More setup required |
| Maintenance | ❌ Less active | ✅ Actively maintained |
| Feature Set | ❌ Basic | ✅ Advanced options |
| FFmpeg Required | ❌ No | ✅ Yes |
| Reliability | ⚠️ May break due to YouTube updates | ✅ More stable |

## ⚠️ Known Issues

* Some videos may not be downloadable due to restrictions
* YouTube's terms of service should be reviewed before using this tool
* Download speed varies based on network conditions

## 📜 Legal Notice

This tool is provided for educational purposes only. Users are responsible for ensuring compliance with YouTube's Terms of Service and local laws regarding video downloads.

## 🤝 Contributing

Want to contribute? Follow these steps:

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Submit a pull request for review
