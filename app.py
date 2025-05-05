import os
import subprocess
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants
UPLOAD_DIR = Path("data/uploaded")
SUPPORTED_FORMATS = ["mp4"]
USERNAME = os.getenv("MAPILLARY_USERNAME")


def save_uploaded_file(file, destination_path):
    with open(destination_path, "wb") as f:
        f.write(file.read())


def upload_to_mapillary(video_path):
    command = [
        "mapillary_tools",
        "process_and_upload",
        str(video_path),
        "--user_name",
        USERNAME,
    ]
    st.info(f"Running: {' '.join(command)}")

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        st.success("Video uploaded to Mapillary successfully.")
    else:
        st.error("Mapillary upload failed.")
        st.text(result.stderr)


# Streamlit UI
st.title("GoPro Video Upload for Mapillary")
st.markdown(
    """
    Upload your GoPro video (MP4 format) to process and upload it to Mapillary.

    Thank you for your collaboration. This tool saves your video and uploads it to the Mapillary dataset.
    """,
)

video_file = st.file_uploader("Upload MP4 video", type=SUPPORTED_FORMATS)

if USERNAME is None:
    st.error("MAPILLARY_USERNAME environment variable is not set.")
elif video_file:
    user_folder = UPLOAD_DIR / USERNAME
    user_folder.mkdir(parents=True, exist_ok=True)

    video_path = user_folder / video_file.name
    save_uploaded_file(video_file, video_path)

    st.success(f"Video uploaded successfully to {video_path}")

    if st.button("Upload to Mapillary"):
        try:
            upload_to_mapillary(video_path)
        except Exception as error:
            st.error("An error occurred during the upload process.")
            st.exception(error)
else:
    st.warning("Please upload a video file.")
