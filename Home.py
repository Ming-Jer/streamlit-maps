import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Customize page title
st.title("Streamlit for Geospatial Applications")

st.markdown(
    """
    This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). 
    It is an open-source project and you are very welcome to contribute to the [GitHub repository](https://github.com/opengeos/streamlit-map-template).
    此多頁應用程式範本展示了使用 [streamlit](https://streamlit.io) 和 [leafmap](https://leafmap.org) 建立的各種互動式網路應用程式。
    這是一個開源專案，歡迎您為 [GitHub儲存庫](https://github.com/opengeos/streamlit-map-template) 做出貢獻。
    """
)

st.header("Instructions")

markdown = """
1. For the [GitHub repository](https://github.com/opengeos/streamlit-map-template) or [use it as a template](https://github.com/opengeos/streamlit-map-template/generate) for your own project.
前往 [GitHub儲存庫](https://github.com/opengeos/streamlit-map-template) 或[將其作為範本](https://github.com/opengeos/streamlit-map-template/generate)用於您的專案。
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
透過修改每個Python檔案中的側邊欄文字和標誌來自訂側邊欄。
3. Find your favorite emoji from https://emojipedia.org. 從 https://emojipedia.org 尋找您喜愛的表情符號。
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.在 pages/ 目錄中新增一個檔案名稱含有表情符號的新應用程式

"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
