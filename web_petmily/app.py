# streamlit 라이브러리 호출
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
matplotlib.use('Agg')       #서버에서, 화면에 표시하기 위해서 필요
import seaborn as sns
import altair as alt               ##https://altair-viz.github.io/
import plotly.express as px
petCon = pd.read_csv('../data/동물위탁관리업.csv')

# 마크다운을 기반으로 한 꾸미기 기능 작동
# 가장 간단한 웹 사이트를 만드는 방법


# """ """ 여러 줄을 묶어서 표시할 수 있는 문자열
# ''' ''' (동일 기능)

st.write(
    """
    ## 코딩 유튜브 채널 추천❗  
    ---
    """
)

import plotly.express as px
import streamlit as st

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)


st.sidebar.title('시간 순삭 유튜브 추천👇')

add_selectbox = st.sidebar.selectbox("주인장 추천 채널",
 ["지식한입", "ITSub잇섭", "느낌적인느낌","호갱구조대", "너 진짜 똑독하다", "슈카월드"])

values = st.sidebar.slider('추천 채널 만족도를 평가', 1, 5)
st.sidebar.write('평가 점수:', values)


col1,col2 = st.columns([1,1])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성

with col1 :
  # column 1 에 담을 내용
  st.markdown("**나에게 :blue[가장 도움이 될 것 같은] 유튜브**")

  st.image("https://user-images.githubusercontent.com/71927533/221650828-c1a86b95-99ac-4a85-a4cc-e398eaf2865f.jpg")
  st.info('추천 이유 : 신기하고 재밌는 인공지능을 쉽게, 짧게 설명해주는 유튜브 입니다!', icon="ℹ️")
  
  # Text Area
  message = st.text_area("소개해 드린 추천 채널의 느낀점을 입력해 주세요", "이곳에 입력하세요.")
  if st.button("Submit", key='message'):
    result = message.title()
    st.success(result)

  st.write(
    """
    > 출처: [빵형의 개발도상국](https://www.youtube.com/@bbanghyong/), [노마드 코더](https://www.youtube.com/@nomadcoders)
    
    """)


with col2 :
  # column 2 에 담을 내용
  st.markdown("**:red[남]이보면 좋을 것 같은 유튜브**")
  st.image("https://user-images.githubusercontent.com/71927533/221631810-b72fa62f-2c41-4a86-a105-2f4a0c1e1b2c.jpg")
  st.info('추천 이유 : IT 트렌드 흐름을 알기 쉽고 빠르게 설명해주고, 간단 명료합니다!', icon="ℹ️")
  



