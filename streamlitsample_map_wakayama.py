import streamlit as st
import pandas as pd
import pydeck as pdk

# タイトルを設定
st.title("日本の主要な観光地")

# データの準備（サンプルデータ）
df = pd.DataFrame({
    "観光地名": ["東京タワー", "清水寺", "厳島神社", "姫路城", "富士山"],
    "latitude": [35.658581, 34.994844, 34.294005, 34.837544, 35.360625],
    "longitude": [139.745433, 135.785012, 132.321111, 134.690889, 138.727363]
})

# pydeckのレイヤーを作成
layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position=["longitude", "latitude"],
    get_radius=10000,  # 表示する点の半径（メートル）
    pickable=True,  # マウスオーバーで選択可能にする
    auto_highlight=True,  # マウスオーバーでハイライトする
    tooltip=True,  # ツールチップを表示する
)

# pydeckのビューを作成
view_state = pdk.ViewState(
    latitude=35.689487,  # 初期表示の緯度（東京付近）
    longitude=139.691706,  # 初期表示の経度（東京付近）
    zoom=5,  # 初期表示のズームレベル
    pitch=0,  # 俯瞰角度
)

# pydeckのツールチップを設定
tooltip = {
    "html": "<b>{観光地名}</b><br/>緯度: {latitude}<br/>経度: {longitude}",
    "style": {"backgroundColor": "steelblue", "color": "white"},
}

# Streamlitでpydeckの地図を表示
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox-search-web/cl5l944i6000k14o4ing22srv",  # 地図のスタイル
    initial_view_state=view_state,
    layers=[layer],
    tooltip=tooltip
))
