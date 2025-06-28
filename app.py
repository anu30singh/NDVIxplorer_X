import streamlit as st
import numpy as np
import rasterio
import matplotlib.pyplot as plt
import leafmap.foliumap as leafmap
import tempfile

st.set_page_config(page_title="NDVIxplorer", page_icon="🛰️", layout="wide")
st.title("🛰️ NDVIxplorer - Urban Green Cover Analyzer")

st.markdown("Upload a **GeoTIFF** file, and this tool will calculate and visualize the **NDVI (Normalized Difference Vegetation Index)**.")

uploaded_file = st.file_uploader("📤 Upload GeoTIFF", type=["tif", "tiff"])

def save_ndvi_to_tif(ndvi_array, transform, crs):
    with tempfile.NamedTemporaryFile(suffix=".tif", delete=False) as tmpfile:
        with rasterio.open(
            tmpfile.name,
            "w",
            driver="GTiff",
            height=ndvi_array.shape[0],
            width=ndvi_array.shape[1],
            count=1,
            dtype=ndvi_array.dtype,
            crs=crs,
            transform=transform,
        ) as dst:
            dst.write(ndvi_array, 1)
        return tmpfile.name

if uploaded_file:
    with rasterio.open(uploaded_file) as src:
        st.success("File uploaded successfully!")

        bands = src.count
        if bands < 2:
            st.warning("The image must have at least 2 bands: Red and NIR.")
        else:
            # Note: NDVI = (NIR - Red) / (NIR + Red)

            red = src.read(1).astype("float32")  
            nir = src.read(2).astype("float32")  

            # Avoid divide-by-zero
            ndvi = np.where(
                (nir + red) == 0,
                0,
                (nir - red) / (nir + red)
            )

            # Plot NDVI
            fig, ax = plt.subplots(figsize=(10, 6))
            ndvi_plot = ax.imshow(ndvi, cmap='YlGn', vmin=-1, vmax=1)
            ax.set_title("NDVI Visualization")
            fig.colorbar(ndvi_plot, ax=ax, label="NDVI Value")
            st.pyplot(fig)

            # Show basic NDVI stats
            st.markdown("### 🌿 NDVI Stats")
            st.write(f"Min NDVI: {ndvi.min():.2f}")
            st.write(f"Max NDVI: {ndvi.max():.2f}")
            st.write(f"Mean NDVI: {ndvi.mean():.2f}")

            # Save NDVI as temporary GeoTIFF
            ndvi_tif_path = save_ndvi_to_tif(ndvi, src.transform, src.crs)

            st.subheader("🗺️ NDVI Map Overlay (Interactive)")

            # Create map centered on data bounds
            bounds = src.bounds
            center_lat = (bounds.top + bounds.bottom) / 2
            center_lon = (bounds.left + bounds.right) / 2

            m = leafmap.Map(center=(center_lat, center_lon), zoom=10)
            m.add_raster(ndvi_tif_path, layer_name="NDVI", colormap="YlGn")
            m.to_streamlit(height=500)
