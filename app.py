import streamlit as st
import numpy as np
import rasterio
import matplotlib.pyplot as plt


st.set_page_config(page_title="NDVIxplorer", page_icon="🛰️", layout="wide")


with st.sidebar:

    st.title("About NDVIxplorer")
    st.markdown("""
    **NDVIxplorer** is a web-based tool for visualizing vegetation health using satellite imagery.
                
     Uses the **NDVI formula**:  
    `(NIR - Red) / (NIR + Red)`

    **Who is this for?**
    - Students & researchers   
    - Urban planners 
    - Environmentalists   
    - Anyone curious about green spaces!
    
    ---
    Made with ❤️ by Anushka
    """)

# --- Title & Intro ---
st.title("🛰️ NDVIxplorer - Urban Green Cover Analyzer")
st.markdown("""
Welcome to **NDVIxplorer** – an intuitive tool to understand and visualize vegetation health from satellite imagery.

### 🌿 What is NDVI?
**NDVI (Normalized Difference Vegetation Index)** is a number between -1 and 1 that shows how green (and healthy) an area is. It’s used worldwide in:
-  Agriculture
-  Urban planning
-  Forestry
-  Disaster monitoring

NDVI is calculated from:
- **Red Band**: Plants absorb red light
- **NIR Band**: Healthy vegetation reflects near-infrared light

The formula is:  
`NDVI = (NIR - Red) / (NIR + Red)`
""")

# --- File Upload ---
st.markdown("### Upload your GeoTIFF satellite image (Red + NIR bands):")
uploaded_file = st.file_uploader("Supported format: `.tif`, `.tiff`", type=["tif", "tiff"])

if uploaded_file:
    with rasterio.open(uploaded_file) as src:
        st.success("✅ File uploaded successfully!")

        if src.count < 2:
            st.error(" This image must contain at least 2 bands: Red and NIR.")
        else:
            red = src.read(1).astype("float32")
            nir = src.read(2).astype("float32")

            # --- NDVI Calculation ---
            ndvi = np.where((nir + red) == 0, 0, (nir - red) / (nir + red))

            # --- NDVI Visualization ---
            st.markdown("### NDVI Visualization")
            fig, ax = plt.subplots(figsize=(10, 6))
            ndvi_plot = ax.imshow(ndvi, cmap='YlGn', vmin=-1, vmax=1)
            ax.set_title("NDVI Heatmap (YlGn colormap)", fontsize=16)
            fig.colorbar(ndvi_plot, ax=ax, label="NDVI Value")
            st.pyplot(fig)

            # --- Stats ---
            st.markdown("###  NDVI Statistics")
            col1, col2, col3 = st.columns(3)
            col1.metric("🌱 Min NDVI", f"{ndvi.min():.2f}")
            col2.metric("🌾 Max NDVI", f"{ndvi.max():.2f}")
            col3.metric("📈 Mean NDVI", f"{ndvi.mean():.2f}")

            # --- NDVI Meaning Table ---
            st.markdown("""
### 📚 NDVI Interpretation Guide

| NDVI Value     | Meaning                    |
|----------------|----------------------------|
| 0.6 to 1.0     | Dense, healthy vegetation  |
| 0.2 to 0.6     | Moderate vegetation   |
| 0.0 to 0.2     | Sparse plants or soil     |
| < 0.0          | Water, snow, or urban     |
""")


            st.markdown("""
---
> NDVIxplorer is your quick, accessible, and free way to explore Earth’s green footprint from space — no GIS expertise needed.
""")

else:
    st.info("👆 Upload a GeoTIFF image to begin your NDVI analysis.")
