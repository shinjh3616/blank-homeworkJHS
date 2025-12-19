import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 페이지 설정
st.set_page_config(page_title="Streamlit UI 요소 모음", layout="wide")

# ==================== 텍스트 요소 ====================
st.title("📚 Streamlit UI 요소 종합 가이드")
st.markdown("---")

# 마크다운 텍스트
st.markdown("## 1️⃣ 텍스트 요소")
st.write("**st.write()**: 가장 기본적인 텍스트 및 데이터 출력 함수")
st.header("헤더 텍스트 (st.header)")
st.subheader("서브헤더 텍스트 (st.subheader)")
st.caption("캡션 텍스트 (st.caption) - 작고 회색")
st.code("print('코드 블록 (st.code)')", language="python")
st.text("일반 텍스트 (st.text)")
st.markdown("""
**마크다운 텍스트 (st.markdown)**
- 리스트 항목 1
- 리스트 항목 2
  - 중첩 항목
""")

st.markdown("---")

# ==================== 입력 요소 ====================
st.markdown("## 2️⃣ 입력 요소")

col1, col2 = st.columns(2)

with col1:
    # 텍스트 입력
    name = st.text_input(
        "이름 입력 (st.text_input)",
        placeholder="이름을 입력하세요"
    )
    if name:
        st.write(f"안녕하세요, {name}님!")
    
    # 텍스트 영역
    message = st.text_area(
        "메시지 입력 (st.text_area)",
        placeholder="여러 줄의 텍스트를 입력하세요",
        height=100
    )

with col2:
    # 숫자 입력
    age = st.number_input(
        "나이 입력 (st.number_input)",
        min_value=0,
        max_value=150,
        value=25
    )
    
    # 슬라이더
    price = st.slider(
        "가격 선택 (st.slider)",
        min_value=0,
        max_value=100000,
        value=50000,
        step=1000
    )
    st.write(f"선택된 가격: ₩{price:,}")

# 선택 입력
st.markdown("### 선택 요소")
col3, col4, col5 = st.columns(3)

with col3:
    # 드롭다운 선택
    category = st.selectbox(
        "카테고리 선택 (st.selectbox)",
        ["선택해주세요", "전자제품", "의류", "음식", "책"]
    )

with col4:
    # 멀티 선택
    options = st.multiselect(
        "복수 선택 (st.multiselect)",
        ["파이썬", "자바", "자바스크립트", "C++", "Go"],
        default=["파이썬"]
    )

with col5:
    # 라디오 버튼
    choice = st.radio(
        "라디오 버튼 (st.radio)",
        ["옵션 A", "옵션 B", "옵션 C"]
    )

# 체크박스
st.markdown("### 토글 및 체크박스")
col6, col7 = st.columns(2)

with col6:
    agree = st.checkbox(
        "동의합니다 (st.checkbox)",
        value=False
    )
    if agree:
        st.success("✅ 감사합니다!")

with col7:
    toggle = st.toggle(
        "알림 켜기/끄기 (st.toggle)",
        value=True
    )
    if toggle:
        st.info("알림이 활성화되었습니다")

# 날짜/시간 입력
st.markdown("### 날짜 및 시간")
col8, col9 = st.columns(2)

with col8:
    date = st.date_input(
        "날짜 선택 (st.date_input)",
        value=datetime.now()
    )

with col9:
    time = st.time_input(
        "시간 선택 (st.time_input)",
        value=datetime.now().time()
    )

# 색상 선택
color = st.color_picker(
    "색상 선택 (st.color_picker)",
    value="#00f900"
)

st.markdown("---")

# ==================== 버튼 및 상호작용 ====================
st.markdown("## 3️⃣ 버튼 및 상호작용")

col10, col11, col12 = st.columns(3)

with col10:
    if st.button("일반 버튼 (st.button)", use_container_width=True):
        st.balloons()
        st.success("버튼이 클릭되었습니다!")

with col11:
    if st.button("다운로드 버튼 (st.download_button)", use_container_width=True):
        st.write("다운로드 기능 예시")

with col12:
    if st.button("위험 버튼 (st.button)", use_container_width=True):
        st.error("⚠️ 주의: 이것은 위험한 작업입니다!")

st.markdown("---")

# ==================== 데이터 표시 ====================
st.markdown("## 4️⃣ 데이터 표시 요소")

# 테이블 데이터 생성
df = pd.DataFrame({
    "이름": ["김철수", "이영희", "박민준", "최지은", "정수현"],
    "나이": [25, 30, 28, 26, 32],
    "직급": ["사원", "대리", "사원", "과장", "부장"],
    "급여": [30000, 45000, 35000, 55000, 70000]
})

# 테이블 표시
st.markdown("### 테이블 (st.dataframe)")
st.dataframe(df, use_container_width=True)

# 정적 테이블
st.markdown("### 정적 테이블 (st.table)")
st.table(df.head(3))

st.markdown("---")

# ==================== 차트 및 시각화 ====================
st.markdown("## 5️⃣ 차트 및 시각화")

# 샘플 데이터
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["라인A", "라인B", "라인C"]
)

col13, col14 = st.columns(2)

with col13:
    st.markdown("### 라인 차트 (st.line_chart)")
    st.line_chart(chart_data)

with col14:
    st.markdown("### 바 차트 (st.bar_chart)")
    st.bar_chart(chart_data)

# 산점도
scatter_data = pd.DataFrame(
    np.random.randn(100, 2),
    columns=["x축", "y축"]
)
st.markdown("### 산점도 (st.scatter_chart)")
st.scatter_chart(scatter_data)

st.markdown("---")

# ==================== 알림 및 상태 메시지 ====================
st.markdown("## 6️⃣ 알림 및 상태 메시지")

col15, col16, col17, col18 = st.columns(4)

with col15:
    st.success("✅ 성공 (st.success)")

with col16:
    st.info("ℹ️ 정보 (st.info)")

with col17:
    st.warning("⚠️ 경고 (st.warning)")

with col18:
    st.error("❌ 에러 (st.error)")

st.markdown("---")

# ==================== 입력 폼 ====================
st.markdown("## 7️⃣ 폼 (st.form)")

with st.form("회원가입_폼"):
    st.write("### 회원가입 폼")
    
    col19, col20 = st.columns(2)
    
    with col19:
        first_name = st.text_input("이름", placeholder="홍")
    
    with col20:
        last_name = st.text_input("성", placeholder="길동")
    
    email = st.text_input("이메일", placeholder="example@email.com")
    
    terms = st.checkbox("이용약관에 동의합니다")
    
    # form_submit_button: 폼이 모두 입력된 후에만 전송
    submitted = st.form_submit_button("가입하기 (st.form_submit_button)")
    
    if submitted and terms:
        st.success(f"환영합니다, {first_name}{last_name}님!")
    elif submitted and not terms:
        st.warning("이용약관에 동의해주세요")

st.markdown("---")

# ==================== 레이아웃 및 구조 ====================
st.markdown("## 8️⃣ 레이아웃 요소")

# 사이드바
with st.sidebar:
    st.title("⚙️ 설정")
    st.markdown("### 사이드바 (st.sidebar)")
    sidebar_option = st.radio(
        "메뉴 선택",
        ["홈", "설정", "정보", "도움말"]
    )
    st.write(f"선택된 항목: {sidebar_option}")

# 탭
tab1, tab2, tab3 = st.tabs(["탭1 (st.tabs)", "탭2", "탭3"])

with tab1:
    st.header("탭 1 내용")
    st.write("첫 번째 탭의 컨텐츠입니다")

with tab2:
    st.header("탭 2 내용")
    st.write("두 번째 탭의 컨텐츠입니다")

with tab3:
    st.header("탭 3 내용")
    st.write("세 번째 탭의 컨텐츠입니다")

# 확장 가능한 섹션
with st.expander("더 보기 (st.expander)"):
    st.write("""
    이것은 확장/축소 가능한 섹션입니다.
    - 클릭하면 펼쳐집니다
    - 다시 클릭하면 접혀집니다
    """)

# 컨테이너
with st.container(border=True):
    st.markdown("### 컨테이너 (st.container with border)")
    st.write("경계선이 있는 컨테이너입니다")

st.markdown("---")

# ==================== 특수 요소 ====================
st.markdown("## 9️⃣ 특수 요소")

# 진행률 표시
progress = st.progress(0)
st.write("진행률 (st.progress)")
for percent in range(101):
    progress.progress(percent)

# 스피너
with st.spinner("로딩 중... (st.spinner)"):
    import time
    time.sleep(2)
st.success("완료!")

# 메트릭 표시
col21, col22, col23 = st.columns(3)

with col21:
    st.metric(
        label="매출액 (st.metric)",
        value="₩1,234,567",
        delta="+12.5%"
    )

with col22:
    st.metric(
        label="사용자 수",
        value="10,234",
        delta="-5%"
    )

with col23:
    st.metric(
        label="만족도",
        value="4.8/5.0",
        delta="+0.2"
    )

st.markdown("---")

# ==================== 파일 처리 ====================
st.markdown("## 🔟 파일 처리")

uploaded_file = st.file_uploader(
    "파일 업로드 (st.file_uploader)",
    type=["csv", "txt", "pdf"]
)

if uploaded_file is not None:
    st.success(f"파일 '{uploaded_file.name}' 이 업로드되었습니다!")

st.markdown("---")

# ==================== 마지막 ====================
st.markdown("## 완료!")
st.balloons()
st.write("모든 Streamlit UI 요소를 확인했습니다! 🎉")
