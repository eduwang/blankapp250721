import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("성적 분석 및 시각화")  # 페이지 제목

# 파일 업로드 위젯
uploaded_file = st.file_uploader("학생 성적 CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # CSV 파일을 데이터프레임으로 읽기
    df = pd.read_csv(uploaded_file)
    st.success("파일 업로드 성공!")  # 성공 메시지

    # 데이터프레임 미리보기
    st.subheader("데이터 미리보기")
    st.dataframe(df)

    # 학생별 평균 점수 계산
    score_cols = ["수학", "영어", "과학"]  # 컬럼명에 맞게 수정
    if all(col in df.columns for col in score_cols + ["이름"]):
        df["평균 점수"] = df[score_cols].mean(axis=1)
        st.subheader("학생별 평균 점수")
        st.dataframe(df[["이름", "평균 점수"]])

        # 과목별 석차 계산 및 표시
        st.subheader("과목별 석차")
        rank_df = pd.DataFrame()
        rank_df["이름"] = df["이름"]
        for col in score_cols:
            rank_df[f"{col} 석차"] = df[col].rank(ascending=False, method="min").astype(int)
        st.dataframe(rank_df)

        # 학생별 평균 점수 시각화
        st.subheader("학생별 평균 점수 막대 그래프")
        fig, ax = plt.subplots()
        ax.bar(df["이름"], df["평균 점수"])
        ax.set_xlabel("이름")
        ax.set_ylabel("평균 점수")
        ax.set_title("학생별 평균 점수")
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # 과목별 성적 분포 시각화
        st.subheader("과목별 성적 분포")
        fig2, ax2 = plt.subplots()
        for col in score_cols:
            ax2.plot(df["이름"], df[col], marker='o', label=col)
        ax2.set_xlabel("이름")
        ax2.set_ylabel("점수")
        ax2.set_title("과목별 성적 분포")
        plt.xticks(rotation=45)
        ax2.legend()
        st.pyplot(fig2)
    else:
        st.error("필요한 컬럼(이름, 수학, 영어, 과학)이 모두 포함되어야 합니다.")
else:
    st.info("CSV 파일을 업로드하면 성적 분석 결과와 시각화가 표시됩니다.")

# 각 단계마다 주석을 추가했습니다.