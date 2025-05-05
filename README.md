# GoPro to Mapillary Uploader

This is a simple Streamlit app that allows users to upload GoPro MP4 video files and submit them to the [Mapillary](https://www.mapillary.com/) dataset.

## 🔧 Features

- Web interface to upload `.mp4` videos
- Videos are saved locally in `data/uploaded/<username>`
- Uses `mapillary_tools` to process and upload videos

## 🚀 How to Run

1. **Clone this repository**

```bash
git clone https://github.com/your-username/gopro-mapillary-uploader.git
cd gopro-mapillary-uploader
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up your `.env` file**

Create a `.env` file in the root directory with your Mapillary username:

```env
MAPILLARY_USERNAME=your_mapillary_username
```

4. **Run the Streamlit app**

```bash
streamlit run app.py
```

The app will launch in your browser at `http://localhost:8501`.

## ✅ Requirements

* Python 3.10+
* `mapillary_tools` CLI installed and authenticated
* FFmpeg (optional, for video processing)

## 💡 Notes

* Be sure to run `mapillary_tools authenticate` before uploading for the first time.
* Maximum upload file size can be configured in `.streamlit/config.toml`.
