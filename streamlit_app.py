import streamlit as st

st.title("🎈 My new app")  # 페이지 제목

st.header("헤더 예시")  # 큰 제목

st.subheader("서브헤더 예시")  # 작은 제목

st.text("텍스트 예시: 일반 텍스트를 표시합니다.")  # 일반 텍스트

st.markdown("**마크다운 예시:** _굵게, 이탤릭, 링크 등 지원합니다._ [Streamlit Docs](https://docs.streamlit.io/)")  # 마크다운 지원

st.code("print('Hello, Streamlit!')", language='python')  # 코드 블록

st.latex(r"\int_a^b f(x)dx")  # LaTeX 수식

st.write("write 함수는 다양한 타입을 자동으로 렌더링합니다.", {"key": "value"}, [1, 2, 3])  # 다양한 타입 지원

st.divider()  # 구분선

st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", caption="이미지 예시")  # 이미지 표시

st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")  # 오디오 재생

st.video("https://www.youtube.com/watch?v=B2iAodr0fOo")  # 비디오 재생

st.button("버튼 예시")  # 버튼

st.checkbox("체크박스 예시")  # 체크박스

st.radio("라디오 버튼 예시", ["옵션 1", "옵션 2", "옵션 3"])  # 라디오 버튼

st.selectbox("셀렉트박스 예시", ["선택 1", "선택 2", "선택 3"])  # 드롭다운 셀렉트박스

st.multiselect("멀티셀렉트 예시", ["A", "B", "C"])  # 여러 개 선택 가능한 셀렉트박스

st.slider("슬라이더 예시", 0, 100, 50)  # 슬라이더

st.number_input("숫자 입력 예시", min_value=0, max_value=100, value=10)  # 숫자 입력

st.text_input("텍스트 입력 예시")  # 텍스트 입력

st.text_area("텍스트 영역 예시")  # 여러 줄 텍스트 입력

st.date_input("날짜 입력 예시")  # 날짜 입력

st.time_input("시간 입력 예시")  # 시간 입력

st.file_uploader("파일 업로더 예시")  # 파일 업로드

st.progress(0.5)  # 진행률 표시 (0~1)

st.spinner("로딩 중...")  # 로딩 스피너

st.success("성공 메시지 예시")  # 성공 메시지

st.info("정보 메시지 예시")  # 정보 메시지

st.warning("경고 메시지 예시")  # 경고 메시지

st.error("에러 메시지 예시")  # 에러 메시지

import pandas as pd
df = pd.DataFrame({
    "컬럼1": [1, 2, 3],
    "컬럼2": ["A", "B", "C"]
})
st.dataframe(df)  # 데이터프레임 표시

st.table(df)  # 테이블 표시

import numpy as np
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(chart_data)  # 라인 차트

st.bar_chart(chart_data)  # 바 차트

st.area_chart(chart_data)  # 영역 차트

# 각 요소마다 주석으로 설명을 달았습니다.