import streamlit as st
from transparent_background import Remover
from PIL import Image
import io

st.set_page_config(page_title="Background Remover", layout="centered")

st.header("🧼 BACKGROUND REMOVER")

uploaded_files = st.file_uploader(
    "Upload Image",
    accept_multiple_files=True,
    type=["png", "jpeg", "jpg"]
)

if uploaded_files:
    remover = Remover()

    for file in uploaded_files:
        st.subheader(f"Preview: {file.name}")

        image = Image.open(file)
        st.image(image, caption="Original Image", use_column_width=True)

        # Remove background
        image_remove = remover(image, type="rgba")

        # Convert to bytes for download
        buffer = io.BytesIO()
        image_remove.save(buffer, format="PNG")
        buffer.seek(0)

        st.image(image_remove, caption="Background Removed", use_column_width=True)

        remove_name = f"{file.name.split('.')[0]}_no_bg.png"

        st.download_button(
            label="⬇ Download Image",
            data=buffer,
            file_name=remove_name,
            mime="image/png"
        )



