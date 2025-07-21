import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# NanumGothic 폰트 파일 경로 지정
font_path = "./fonts/NanumGothic-Regular.ttf"
fontprop = fm.FontProperties(fname=font_path)

# 폰트 설정: matplotlib 전체에 적용
plt.rcParams['font.family'] = fontprop.get_name()
plt.rcParams['axes.unicode_minus'] = False   # 마이너스 깨짐 방지

st.title("Matplotlib 한글 그래프 예시")  # 페이지 제목

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, label='사인 곡선', color='blue')
ax.set_title('한글 제목: 사인 그래프', fontproperties=fontprop)
ax.set_xlabel('X축 (시간)', fontproperties=fontprop)
ax.set_ylabel('Y축 (진폭)', fontproperties=fontprop)
ax.legend(prop=fontprop)

st.pyplot(fig)  # Streamlit에 그래프 표시

st.info("NanumGothic 폰트를 직접 불러와 한글이 정상적으로 표시됩니다.")  # 안내 메시지