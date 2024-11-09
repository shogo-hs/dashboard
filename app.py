import pandas as pd
import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer

# Streamlitページの幅を調整する
st.set_page_config(page_title="Streamlit Test", layout="wide")

# タイトルを追加
st.title("Streamlit Test")

# データをインポートする
df = pd.read_csv(
    "https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv"
)


# コピーしたPygwalkerチャートのコードをここに貼り付ける
vis_spec = r"""{"config":[{"config":{"defaultAggregated":true,"geoms":["bar"],"coordSystem":"generic","limit":-1},"encodings":{"dimensions":[{"fid":"date","name":"date","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"month","name":"month","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"season","name":"season","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"year","name":"year","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"holiday","name":"holiday","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"work yes or not","name":"work yes or not","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"am or pm","name":"am or pm","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"Day of the week","name":"Day of the week","semanticType":"quantitative","analyticType":"dimension","offset":0}],"measures":[{"fid":"hour","name":"hour","semanticType":"quantitative","analyticType":"measure","offset":0},{"fid":"temperature","name":"temperature","semanticType":"quantitative","analyticType":"measure","offset":0},{"fid":"feeling_temp","name":"feeling_temp","semanticType":"quantitative","analyticType":"measure","offset":0},{"fid":"humidity","name":"humidity","semanticType":"quantitative","analyticType":"measure","offset":0},{"fid":"winspeed","name":"winspeed","semanticType":"quantitative","analyticType":"measure","offset":0},{"fid":"casual","name":"casual","semanticType":"quantitative","analyticType":"measure","offset":0},{"fid":"registered","name":"registered","semanticType":"quantitative","analyticType":"measure","offset":0},{"fid":"count","name":"count","semanticType":"quantitative","analyticType":"measure","offset":0},{"fid":"gw_count_fid","name":"Row count","analyticType":"measure","semanticType":"quantitative","aggName":"sum","computed":true,"expression":{"op":"one","params":[],"as":"gw_count_fid"}}],"rows":[{"fid":"count","name":"count","semanticType":"quantitative","analyticType":"measure","offset":0}],"columns":[{"fid":"month","name":"month","semanticType":"quantitative","analyticType":"dimension","offset":0}],"color":[],"opacity":[],"size":[],"shape":[],"radius":[],"theta":[],"longitude":[],"latitude":[],"geoId":[],"details":[],"filters":[],"text":[]},"layout":{"showActions":false,"showTableSummary":false,"stack":"none","interactiveScale":false,"zeroScale":true,"size":{"mode":"auto","width":320,"height":200},"format":{},"geoKey":"name","resolve":{"x":false,"y":false,"color":false,"opacity":false,"shape":false,"size":false}},"visId":"3b699f356e859","name":"Chart 1"}],"chart_map":{},"workflow_list":[{"workflow":[{"type":"view","query":[{"op":"raw","fields":["month","count"]}]}]}],"version":"0.4.9.13"}"""

pyg_app = StreamlitRenderer(df, spec=vis_spec)

pyg_app.explorer()
