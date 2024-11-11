import pandas as pd
import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer
from io import StringIO

# Streamlitページの幅を調整する
st.set_page_config(page_title="Streamlit Test", layout="wide")

st.title("データフレーム操作アプリ")

# 初期化: セッション状態に結合結果がなければ None で初期化
if "merged_df" not in st.session_state:
    st.session_state["merged_df"] = None

# ファイルアップロード
uploaded_files = st.file_uploader("CSVファイルをアップロードしてください", accept_multiple_files=True, type="csv")

dataframes: dict[str, pd.DataFrame] = {}

# アップロードされたファイルを読み込む
for uploaded_file in uploaded_files:
    try:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        dataframes[uploaded_file.name] = pd.read_csv(stringio)
    except UnicodeDecodeError:
        try:
            stringio = StringIO(uploaded_file.getvalue().decode("shift-jis"))
            dataframes[uploaded_file.name] = pd.read_csv(stringio)
        except UnicodeDecodeError:
            st.error(f"ファイル {uploaded_file.name} の読み込みに失敗しました。エンコーディングを確認してください。")

# データフレームが2つ以上ある場合は結合を行う
if len(dataframes) >= 2:
    st.subheader("データフレーム結合")
    
    # 結合するデータフレームを選択
    df1_name = st.selectbox("1つ目のデータフレームを選択", list(dataframes.keys()), key="df1_name")
    df2_name = st.selectbox("2つ目のデータフレームを選択", list(dataframes.keys()), key="df2_name")
    
    # 結合方法を選択
    join_type = st.selectbox("結合方法を選択", ["inner", "outer", "left", "right"], key="join_type")
    
    # 結合キーを選択
    join_key = st.selectbox("結合キーを選択", dataframes[df1_name].columns, key="join_key")
    
    if st.button("結合実行"):
        # 結合結果をセッション状態に保存
        st.session_state["merged_df"] = pd.merge(dataframes[df1_name], dataframes[df2_name], on=join_key, how=join_type)
        st.write("結合結果:")
        st.dataframe(st.session_state["merged_df"])
elif len(dataframes) == 1:
    # ファイルが1つだけアップロードされた場合、そのデータフレームを直接使用
    st.session_state["merged_df"] = list(dataframes.values())[0]
    st.write("アップロードされたデータフレーム:")
    st.dataframe(st.session_state["merged_df"])

# Pygwalkerでの可視化
if st.session_state["merged_df"] is not None:
    # Pygwalkerのビジュアライゼーションを表示
    vis_spec = r""""""
    pyg_app = StreamlitRenderer(st.session_state["merged_df"], spec=vis_spec)
    pyg_app.explorer()
