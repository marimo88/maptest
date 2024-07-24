import streamlit as st
import pandas as pd
import pydeck as pdk

# タイトルを設定
st.title("日本の主要な観光地（都道府県別フィルター）")

# データの準備（サンプルデータ）
df = pd.DataFrame({
    "観光地名": ["東京タワー", "清水寺", "厳島神社", "姫路城", "富士山"],
    "都道府県": ["東京都", "京都府", "広島県", "兵庫県", "山梨県"],
    "latitude": [35.658581, 34.994844, 34.294005, 34.837544, 35.360625],
    "longitude": [139.745433, 135.785012, 132.321111, 134.690889, 138.727363]
})

# 都道府県の選択ボックス（「全て」の選択肢を追加）
pref_options = ["全て"] + df["都道府県"].unique().tolist()
selected_pref = st.selectbox("都道府県を選択", pref_options)

# 選択された都道府県に応じてデータをフィルタリング
if selected_pref == "全て":
    filtered_df = df
else:
    filtered_df = df[df["都道府県"] == selected_pref]

# pydeckのレイヤーを作成
layer = pdk.Layer(
    "ScatterplotLayer",
    data=filtered_df,
    get_position=["longitude", "latitude"],
    get_radius=10000,
    pickable=True,
    auto_highlight=True,
    tooltip=True
)

# pydeckのビューを作成
if selected_pref == "全て":
    view_state = pdk.ViewState(
        latitude=35.689487,  # 初期表示の緯度（東京付近）
        longitude=139.691706,  # 初期表示の経度（東京付近）
        zoom=5,  # 初期表示のズームレベル
        pitch=0
    )
else:
    view_state = pdk.ViewState(
        latitude=filtered_df["latitude"].mean(),  # 選択された都道府県の中心に移動
        longitude=filtered_df["longitude"].mean(),
        zoom=7,  # ズームレベルを調整
        pitch=0
    )

# pydeckのツールチップを設定
tooltip = {
    "html": "<b>{観光地名}</b><br/>都道府県: {都道府県}<br/>緯度: {latitude}<br/>経度: {longitude}",
    "style": {"backgroundColor": "steelblue", "color": "white"},
}

# Streamlitでpydeckの地図を表示
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox-search-web/cl5l944i6000k14o4ing22srv",
    initial_view_state=view_state,
    layers=[layer],
    tooltip=tooltip
))
