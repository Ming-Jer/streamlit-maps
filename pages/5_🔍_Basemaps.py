import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)


st.title("Searching Basemaps尋找基本圖")
st.markdown(
    """
This app is a demonstration of searching and loading basemaps from [xyzservices](https://github.com/geopandas/xyzservices) and [Quick Map Services (QMS)](https://github.com/nextgis/quickmapservices). Selecting from 1000+ basemaps with a few clicks.
此應用程式展示了如何從 [xyzservices](https://github.com/geopandas/xyzservices) 和 [Quick Map Services (QMS)](https://github.com/nextgis/quickmapservices) 搜尋和載入底圖。只需點擊幾下，即可從超過1000種底圖中進行選擇。
"""
)

with st.expander("See demo"):
    st.image("https://i.imgur.com/0SkUhZh.gif")

row1_col1, row1_col2 = st.columns([3, 1])
width = None
height = 800
tiles = None

with row1_col2:

    checkbox = st.checkbox("Search Quick Map Services (QMS) 尋找快速地圖服務(QMS)")
    keyword = st.text_input("Enter a keyword to search and press Enter:輸入關鍵字後按下Enter鍵")
    empty = st.empty()

    if keyword:
        options = leafmap.search_xyz_services(keyword=keyword)
        if checkbox:
            options = options + leafmap.search_qms(keyword=keyword)

        tiles = empty.multiselect("Select XYZ tiles to add to the map:選擇XYZ圖磚到地圖內", options)

    with row1_col1:
        m = leafmap.Map()

        if tiles is not None:
            for tile in tiles:
                m.add_xyz_service(tile)

        m.to_streamlit(width, height)
