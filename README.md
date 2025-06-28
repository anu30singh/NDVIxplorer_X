# 🛰️ NDVIxplorer - Urban Green Cover Analyzer

**NDVIxplorer** is a beginner-friendly web app that lets anyone analyze and visualize green cover using satellite imagery — no GIS experience required.

🌱 Powered by Streamlit, NDVIxplorer calculates the **Normalized Difference Vegetation Index (NDVI)** from GeoTIFF files and presents:
- A color-coded NDVI heatmap
- Interpretable vegetation stats
- A non-technical explanation of what NDVI means

---

## 🌍 Live Demo

[🔗 Click here to try the app](https://your-ndvixplorer-demo.streamlit.app) *(Replace with your actual Streamlit Cloud URL)*

---

## 🎯 Features

✅ Upload GeoTIFF files (Red + NIR bands)  
✅ Automatic NDVI calculation  
✅ Beautiful NDVI heatmap visualization using Matplotlib  
✅ Interpretable NDVI statistics (min, max, mean)  
✅ Beginner-friendly UI with explanations for non-GIS users  
✅ Sidebar "About" section for context and learning  
✅ Clean layout with Streamlit UI components  

---

## 🧠 What is NDVI?

> NDVI = (NIR - Red) / (NIR + Red)

NDVI is a remote sensing index that reflects vegetation health. It uses the Red and Near-Infrared (NIR) bands from satellite imagery. Values range from **-1 to +1**:

| NDVI Range  | Interpretation               |
|-------------|-------------------------------|
| 0.6 to 1.0  | Dense, healthy vegetation 🌳  |
| 0.2 to 0.6  | Moderate vegetation 🌾         |
| 0.0 to 0.2  | Sparse or stressed plants 🌿   |
| < 0.0       | Water, urban areas, clouds 🏙️ |

---

## 💡 Use Cases

- 👨‍🌾 Agriculture: monitor crop health
- 🌆 Urban planning: measure green cover
- 🌲 Forestry: detect deforestation
- 🔥 Disaster response: assess vegetation loss after fires/floods
- 🛰️ Education & awareness: introduce NDVI to non-experts

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8+
- pip


