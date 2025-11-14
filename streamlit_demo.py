import streamlit as st
import os
#on terminal, streamlit run (path)
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.ticker as ticker
from matplotlib import rc

def apply_web_font(): #Streamlit 웹에 Pretendard family 웹 폰트 적용
    #Pretendard @font-face CSS 구문
    comp_css = """
    <style>
    @font-face {
        font-family: 'Pretendard';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/pretendard@1.0/Pretendard-Thin.woff2') format('woff2');
        font-weight: 100;
        font-display: swap;
    }
    @font-face {
        font-family: 'Pretendard';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/pretendard@1.0/Pretendard-ExtraLight.woff2') format('woff2');
        font-weight: 200;
        font-display: swap;
    }
    @font-face {
        font-family: 'Pretendard';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/pretendard@1.0/Pretendard-Light.woff2') format('woff2');
        font-weight: 300;
        font-display: swap;
    }
    @font-face {
        font-family: 'Pretendard';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/pretendard@1.0/Pretendard-Regular.woff2') format('woff2');
        font-weight: 400;
        font-display: swap;
    }
    @font-face {
        font-family: 'Pretendard';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/pretendard@1.0/Pretendard-Medium.woff2') format('woff2');
        font-weight: 500;
        font-display: swap;
    }
    @font-face {
        font-family: 'Pretendard';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/pretendard@1.0/Pretendard-SemiBold.woff2') format('woff2');
        font-weight: 600;
        font-display: swap;
    }
    @font-face {
        font-family: 'Pretendard';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/pretendard@1.0/Pretendard-Bold.woff2') format('woff2');
        font-weight: 700;
        font-display: swap;
    }
    @font-face {
        font-family: 'Pretendard';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/pretendard@1.0/Pretendard-ExtraBold.woff2') format('woff2');
        font-weight: 800;
        font-display: swap;
    }
    @font-face {
        font-family: 'Pretendard';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/pretendard@1.0/Pretendard-Black.woff2') format('woff2');
        font-weight: 900;
        font-display: swap;
    }
    
    /* --- 요소별 폰트 굵기 지정 --- */
        
        /* 기본 텍스트 (st.write, st.markdown 등) */
        body {
            font-family: 'Pretendard', sans-serif;
            font-weight: 400; /* Regular */
        }
        
        /* st.title (가운데 정렬 포함) */
        h1 {
            font-weight: 900 !important; /* Black */
            text-align: center;
        }
        
        /* st.subheader */
        h2 {
            font-weight: 600 !important; /* SemiBold */
        }
        
        /* st.header */
        h3 {
             font-weight: 500 !important; /* Medium */
        }

        h6 {
             font-weight:300 !important; /* Light */
             text-align: left;
        }

        /* 감소 라벨 */
        .decrease-label {
            display: inline-block;
            background-color: rgba(255, 0, 0, 0.1);
            color: #d32f2f;
            padding: 8px 16px;
            border-radius: 6px;
            font-size: 16px;
            font-weight: bold;
            margin-bottom: 10px;
            border: 1px solid rgba(255, 0, 0, 0.2);
        }

        /* 증가 라벨 */
        .increase-label {
                display: inline-block;
                background-color: rgba(0, 128, 0, 0.1);
                color: #2e7d32;
                padding: 8px 16px;
                border-radius: 6px;
                font-size: 16px;
                font-weight: bold;
                margin-bottom: 10px;
                border: 1px solid rgba(0, 128, 0, 0.2);
        }


    </style>
    """
    st.markdown(comp_css, unsafe_allow_html=True)

def setting_matplotlib_font(): #Matplotlib 차트 이미지에 로컬 Pretendard 폰트 적용
    # 현재 스크립트 파일(streamlit_demo.py)이 있는 폴더 경로
    base_dir = os.path.dirname(__file__)
    
    # 폰트 파일 이름
    font_filename = 'Pretendard-Bold.ttf' 
    
    # 폰트 파일의 전체 경로 (base_dir와 폰트 파일 이름을 합침)
    font_path = os.path.join(base_dir, font_filename)

    # (중요) 폰트가 실제로 존재하는지 확인
    if not os.path.exists(font_path):
        # 만약 파일을 못 찾으면, Streamlit Cloud 로그에 경로가 찍히도록 함
        print(f"현재 폴더 경로: {base_dir}")
        print(f"찾으려는 폰트 경로: {font_path}")
        raise FileNotFoundError(f"폰트 파일을 찾을 수 없습니다: {font_path}")
    
    plt.rcParams['font.family'] = 'Pretendard' # <-- 'Pretendard-Bold'가 아닐 수 있음
    plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지
    
    print("폰트 설정 완료.") # Streamlit Cloud 로그 확인용

    # 폰트 매니저에 폰트 추가
    fm.fontManager.addfont(font_path)

def graph_population() : #총인구수 그래프
    data = pd.read_csv("C:/Users/taehyeon/Desktop/2025-2/전공/데이터시각화/Project/장래인구추계.csv", encoding="cp949")

    years = data.columns[1:]
    population = data.iloc[0, 1:]
    
    years = pd.to_numeric(years, errors='coerce').values
    population = pd.to_numeric(population, errors='coerce').values

    #총인구 최대치 연도
    max_population_index = population.argmax()
    max_year = years[max_population_index]
    max_population_value = population[max_population_index]

    plt.figure(figsize=(14, 6))
    plt.plot(years, population, linewidth=2.5, color='#2563eb')
    plt.fill_between(years, population, alpha=0.3, color='#93c5fd')

    #최대치 연도 세로선
    plt.axvline(x = max_year, color = 'red', linestyle = ':', linewidth = 2, label = f'최대 인구 시점, {max_year}년')
    text_label = f"{max_population_value:,.0f}명"
    plt.text(x=max_year + 0.2,                 #x좌표 (선에서 0.2년 옆)
             y=max_population_value / 2,       #y좌표 (선의 중간쯤)
             s=text_label,                     #표시할 텍스트
             color='red',                      #텍스트 색상
             fontsize=22,
             rotation=270,                      #텍스트를 90도 회전
             ha='left',                        #수평 정렬 (텍스트의 왼쪽을 x좌표에 맞춤)
             va='center')                      #수직 정렬 (텍스트의 세로 중앙을 y좌표에 맞춤)          
    plt.legend()
    
    plt.xlabel("연도", fontsize = 12)
    plt.ylabel("인구수", fontsize = 12)
    #plt.title("연도별 인구 수 변화", fontsize = 16)
    plt.grid(True, alpha = 0.3)
    
    #축 범위 꽉 채우기
    plt.xlim(years.min(), years.max())
    plt.ylim(0, population.max() * 1.05)  #y축
    
    plt.xticks(range(1960, 2030, 5), rotation = 45)
    plt.yticks(range(10000000, 60000000, 10000000), labels=["10M", "20M", "30M", "40M", "50M"])
    
    plt.tight_layout()  #전체 레이아웃 최적화
    
    col1, col2 = st.columns([3,1])
    with col1 :
        st.pyplot(plt)
        st.caption("데이터 출처 : [국가데이터처](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1BPA001&conn_path=I2)「장래인구추계」, 2072, 2025.11.05, 성 및 연령별 추계인구(1세별, 5세별) / 전국")
    
    with col2 :
        #최고치와 현재값 계산
        peak_value = max_population_value
        current_value = population[len(population) - 1]
        decrease_value = peak_value - current_value
        decrease_rate = ((peak_value - current_value) / peak_value) * 100

        #증감률 레이블 표시
        st.subheader("연도별 인구 수 변화")
        st.markdown("<h6>1960 ~ 2025</h6>",unsafe_allow_html=True)
        st.markdown(f'<div class="decrease-label">{years[max_population_index]}년도 대비 약 {decrease_rate:.2f}% 감소 <br><h2>↓ {format(decrease_value, ",")}명</h2></div>', unsafe_allow_html=True)
        
        st.markdown("<h5>그래프 설명</h5>", unsafe_allow_html=True)
        st.markdown("1960년부터 2025년까지 **국내에 상주하고 있는 외국인을 포함한 인구의 총합이다.**\n2020년에 인구 수 최대치를 기록하고 현재 소폭 감소하였다.", unsafe_allow_html=True)
    with st.expander("원본 데이터 표 보기"):
        st.dataframe(data)
    plt.close()

def graph_population_sex() : #성별에 따른 바 그래프 
    data = pd.read_csv("C:/Users/taehyeon/Desktop/2025-2/전공/데이터시각화/Project/성비.csv", encoding="cp949")

    years = data.columns[1:]
    population = data.iloc[0:, 1:3]

    x = range(len(years))
    width = 0.35

    male = population.iloc[0].values
    female = population.iloc[1].values

    fig = plt.figure(figsize=(8, 6.32))

    plt.bar([i - width/2 for i in x], male, width, label='남성', color='skyblue')
    plt.bar([i + width/2 for i in x], female, width, label='여성', color='pink')

    plt.title('성별 인구 비율 (2020-2025)', fontsize=18, fontweight='bold', pad=20)
    plt.ylabel('인구수', fontsize=12)   
    plt.xticks(x, years)
    plt.legend()

    ax = plt.gca()
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, p: f'{int(y):,}'))

    plt.ylim(male.max() * 0.993, male.max() * 1.0029)
    plt.grid(axis='y', alpha=0.3)

    #증감률 및 성비 표기
    for i in x:
        #2025년에만 전년 대비 증감률 표기
        if i == 1:
            #남성 증감률
            male_change = ((male[i] - male[i-1]) / male[i-1]) * 100
            plt.text(i - width/2, male[i] + male.max() * 0.0002, 
                    f'{male_change:+.2f}%\n{abs(male[i] - male[i-1]):,.0f}명 감소', 
                    ha='center', va='bottom', fontsize=9, fontweight='bold', color='#2E86AB')
            
            #여성 증감률
            female_change = ((female[i] - female[i-1]) / female[i-1]) * 100
            plt.text(i + width/2, female[i] + female.max() * 0.0002, 
                    f'{female_change:+.2f}%\n{abs(female[i] - female[i-1]):,.0f}명 감소', 
                    ha='center', va='bottom', fontsize=9, fontweight='bold', color='#E91E63')
        
        #각 연도별 남녀 인구 차이 표기
        diff = male[i] - female[i]
        diff_percent = (diff / female[i]) * 100
        
        #두 바 사이 중앙에 표기
        mid_y = (male[i] + female[i]) * 0.5 + 40000
        
        if diff > 0:
            text = f'남성\n+{diff:,.0f}명\n(+{diff_percent:.2f}%)'
            color = '#2E86AB'
        else:
            text = f'여성\n+{abs(diff):,.0f}명\n(+{abs(diff_percent):.2f}%)'
            color = '#E91E63'
        
        plt.text(i, mid_y, text, 
                ha='center', va='center', fontsize=8, 
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=color, alpha=0.8),
                color=color, fontweight='bold')
    plt.tight_layout()
    
    return fig, data

def graph_population_age() : #연령에 따른 파이 그래프
    data = pd.read_csv("C:/Users/taehyeon/Desktop/2025-2/전공/데이터시각화/Project/연령.csv", encoding="cp949")

    # 연령대별 그룹화
    youth = data[data["연령별"].isin(["0 - 4세", "5 - 9세", "10 - 14세"])]["2025"].sum()
    adult = data[data["연령별"].str.contains("15|20|25|30|35|40|45|50|55|60 - 64세")]["2025"].sum()
    elderly = data[data["연령별"].str.contains("65|70|75|80|100")]["2025"].sum()

    # 새로운 데이터프레임 생성
    age_groups = pd.DataFrame({
        "연령층": ["유소년층\n(0~14세)", "청장년층\n(15~64세)", "노년층\n(65세 이상)"],
        "인구": [youth, adult, elderly]
    })

    # 색상 설정 (노년층을 빨간색으로 강조)
    colors = ['#A8D5BA', '#7EB6D5', '#FF6B6B']

    # explode 설정 (노년층만 돌출)
    explode = [0, 0, 0.15]

    # 파이 차트 생성
    fig, ax = plt.subplots(figsize=(7, 7))

    wedges, texts, autotexts = ax.pie(
        age_groups["인구"].values,
        labels=age_groups["연령층"].values,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        explode=explode,
        textprops={'fontsize': 14},
        pctdistance=0.85
    )

    # 노년층 강조
    for i, (wedge, text, autotext) in enumerate(zip(wedges, texts, autotexts)):
        if i == 2:  # 노년층
            wedge.set_edgecolor('#D32F2F')
            wedge.set_linewidth(4)
            text.set_fontsize(16)
            text.set_fontweight('bold')
            text.set_color('#D32F2F')
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(14)
        else:
            autotext.set_fontsize(12)
            autotext.set_fontweight('bold')

    # 제목
    plt.title('연령층별 인구 비율 (2025)', fontsize=18, fontweight='bold', pad=20)

    plt.tight_layout()
    
    return fig, data

def st_columns_SexAge() : #성별, 연령 통합 출력 
    # 그래프 생성
    fig_sex, data_sex = graph_population_sex()
    fig_age, data_age = graph_population_age()
    
    # 그래프 컨테이너
    graph_container = st.container()
    with graph_container:
        col1, col2 = st.columns([4, 2.95])
        
        with col1:
            st.pyplot(fig_sex)
            plt.close(fig_sex)
        
        with col2:
            st.pyplot(fig_age)
            plt.close(fig_age)
    
    # 설명 컨테이너
    description_container = st.container()
    with description_container:
        col1, col2 = st.columns([4, 2.95])
        
        with col1:
            st.markdown("<h5>그래프 설명</h5>", unsafe_allow_html=True)
            st.markdown("2020년과 2025년의 **남녀 인구이다.**<br>2020년에는 남성이 여성보다 15,155명 많았으나, 2025년에는 여성의 인구가 8,758명 더 많다.", unsafe_allow_html=True)
            st.caption("데이터 출처 : [국가데이터처](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1BPA001&conn_path=I2)「장래인구추계」, 2072, 2025.11.05, 성 및 연령별 추계인구(1세별, 5세별) / 전국")
            
            with st.expander("원본 데이터 표 보기"):
                st.dataframe(data_sex)
        
        with col2:
            st.markdown("<h5>그래프 설명</h5>", unsafe_allow_html=True)
            st.markdown("**2025년의 연령대별 인구 비율이다.**<br>현재 65세 이상의 노년층이 전체 인구의 20.4%로, 초고령 사회임을 확인 가능하다.", unsafe_allow_html=True)
            st.caption("데이터 출처 : [국가데이터처](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1BPA001&conn_path=I2)「장래인구추계」, 2072, 2025.11.05, 성 및 연령별 추계인구(1세별, 5세별) / 전국")
            
            with st.expander("원본 데이터 표 보기"):
                st.dataframe(data_age)

def graph_population_growrate() : #인구성장률
    data_df = pd.read_csv("C:/Users/taehyeon/Desktop/2025-2/전공/데이터시각화/Project/인구성장률.csv", 
                   header=None, encoding="cp949")
    
    data = data_df.transpose()
    data.columns = data.iloc[0]
    data = data.drop(data.index[0])
    data = data.reset_index(drop=True)

    # 연도를 정수형으로 변환
    data["연도"] = data["연도"].astype(float).astype(int)
    data["인구성장률"] = data["인구성장률"].astype(float)

    # 5년 단위로 필터링 (1960, 1965, 1970, ..., 2025)
    data_5year = data[data["연도"] % 5 == 0]

    # 2025년 데이터 찾기
    year_2025 = data[data["연도"] == 2025]
    value_2025 = year_2025["인구성장률"].values[0]

    # color 변수 설정
    color = '#E91E63'

    # 그래프 그리기
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # 선 그래프
    ax.plot(data_5year["연도"], data_5year["인구성장률"], 
            marker='o', linewidth=2.5, markersize=8, 
            color='#1976D2', markerfacecolor='#64B5F6', markeredgewidth=1.5)

    # 2025년 포인트 강조
    ax.plot(2025, value_2025, marker='o', markersize=15, 
            color=color, markeredgecolor='darkred', markeredgewidth=2, zorder=5)

    # 2025년 텍스트 - 위쪽 (테두리 없음)
    ax.text(2025, value_2025 + 0.50, '2025년',
            ha='center', va='center', fontsize=9,
            color=color, fontweight='bold')
    
    # 2025년 값 박스 - 아래쪽 (큰 폰트, bbox 있음)
    ax.text(2025, value_2025 + 0.30, f'{value_2025:.2f}%',
            ha='center', va='center', fontsize=14,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', 
                     edgecolor=color, linewidth=2.5, alpha=0.95),
            color=color, fontweight='bold')

    # 축 설정
    ax.set_xlabel('연도', fontsize=13, fontweight='bold')
    ax.set_ylabel('인구성장률 (%)', fontsize=13, fontweight='bold')
    ax.set_title('인구성장률 변화 (1960-2025)', fontsize=16, fontweight='bold', pad=20)
    
    # x축 5년 단위로 강제 설정
    years = list(range(1960, 2030, 5))
    ax.set_xticks(years)
    ax.set_xticklabels(years, rotation=45, ha='right')
    
    # 그리드 설정
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax.set_axisbelow(True)
    
    # 배경색 설정
    ax.set_facecolor('#F8F9FA')
    
    plt.tight_layout()

    col1, col2 = st.columns([1.3,3])
    with col1 :
        st.subheader("연도별 인구 수 변화")
        st.markdown("<h6>1960 ~ 2025</h6>",unsafe_allow_html=True)
        st.markdown("<h5>그래프 설명</h5>", unsafe_allow_html=True)
        st.markdown("**인구성장률은 전년 대비 추계인구의 증감률이다.**<br>2021년 인구성장률 -0.13을 기록하며 마이너스 성장대로 전환했다.", unsafe_allow_html=True)
        with st.expander("원본 데이터 표 보기"):
            st.dataframe(data_df)
    with col2 :
        st.pyplot(fig)
        st.caption("데이터 출처 : [국가데이터처](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1BPA002&conn_path=I2)「장래인구추계」, 2072, 2025.11.14, 주요 인구지표(성비,인구성장률,인구구조,부양비 등) / 전국")

    
    plt.close()

def graph_fertility_rate(): #합계출산율
    data_df = pd.read_csv("C:/Users/taehyeon/Desktop/2025-2/전공/데이터시각화/Project/합계출산율.csv", 
                   header=None, encoding="cp949")
    
    data = data_df.transpose()
    data.columns = data.iloc[0]
    data = data.drop(data.index[0])
    data = data.reset_index(drop=True)

    # 연도를 정수형으로 변환
    data["연도"] = data["연도"].astype(float).astype(int)
    data["합계출산율"] = data["합계출산율"].astype(float)

    # 5년 단위로 필터링 (1970, 1975, 1980, ..., 2025)
    data_5year = data[data["연도"] % 5 == 0]

    # 2025년 데이터 찾기
    year_2025 = data[data["연도"] == 2025]
    value_2025 = year_2025["합계출산율"].values[0]

    # color 변수 설정
    color = '#E91E63'

    # 그래프 그리기
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # 선 그래프
    ax.plot(data_5year["연도"], data_5year["합계출산율"], 
            marker='o', linewidth=2.5, markersize=8, 
            color='#1976D2', markerfacecolor='#64B5F6', markeredgewidth=1.5)

    # 2024년 수직선 추가 (잠정치 표시)
    ax.axvline(x=2024, color='orange', linestyle='--', linewidth=2, alpha=0.7, label='잠정치')
    
    # 잠정치 영역 음영 처리
    ax.axvspan(2024, 2026, alpha=0.1, color='orange')

    # 2025년 포인트 강조
    ax.plot(2025, value_2025, marker='o', markersize=15, 
            color=color, markeredgecolor='darkred', markeredgewidth=2, zorder=5)

    # 축 설정
    ax.set_xlabel('연도', fontsize=13, fontweight='bold')
    ax.set_ylabel('합계출산율 (명)', fontsize=13, fontweight='bold')
    ax.set_title('합계출산율 변화 (1970-2025)', fontsize=16, fontweight='bold', pad=20)
    
    # x축 5년 단위로 강제 설정
    years = list(range(1970, 2030, 5))
    ax.set_xticks(years)
    ax.set_xticklabels(years, rotation=45, ha='right')
    ax.set_xlim(1970, 2026)

    # 그리드 설정
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax.set_axisbelow(True)
    
    # 배경색 설정
    ax.set_facecolor('#F8F9FA')
    
    # 범례 추가
    ax.legend(loc='upper right', fontsize=10)
    
    plt.tight_layout()

    col1, col2 = st.columns([3, 1])
    with col2:
        st.subheader("연도별 합계출산율 변화")
        st.markdown(f'<div class="decrease-label";>OECD 합계출산율 평균 대비  <br><h2>↓ {1.51 - value_2025}명 낮음</h2></div>', unsafe_allow_html=True)
        st.markdown("<h6>1970 ~ 2025</h6>", unsafe_allow_html=True)
        st.markdown("<h5>그래프 설명</h5>", unsafe_allow_html=True)
        st.markdown(f"**여성 1명이 평생 낳을 것으로 예상되는 평균 출생아 수**를 나타낸다. <br>인구를 현재 수준으로 유지할 수 있는 합계출산율은 2.1명이며, **현재 이보다 {2.1 - value_2025:.2f}명 낮은 {value_2025}명을 기록하고 있다.**", unsafe_allow_html=True)
    with col1:
        st.pyplot(fig)
        st.caption("데이터 출처 : [국가데이터처](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1BPA101&conn_path=I2)「장래인구추계」, 2072, 2025.11.14, 장래 합계출산율 / 전국")
    with st.expander("원본 데이터 표 보기"):
        st.dataframe(data_df)

    plt.close()

def graph_ageing_index(): #고령화지수
    data_df = pd.read_csv("C:/Users/taehyeon/Desktop/2025-2/전공/데이터시각화/Project/노령화지수_노년부양비.csv", header=None, encoding="cp949")
    
    data = data_df.transpose()
    data.columns = data.iloc[0]
    data = data.drop(data.index[0])
    data = data.reset_index(drop=True)

    # 데이터 타입 변환
    data["연도"] = data["연도"].astype(float).astype(int)
    data["노령화지수"] = data["노령화지수"].astype(float)
    data["노년부양비"] = data["노년부양비"].astype(float)

    # 5년 단위로 필터링
    data_5year = data[data["연도"] % 5 == 0]

    # 2025년 데이터 찾기
    year_2025 = data[data["연도"] == 2025]
    value_ageing_2025 = year_2025["노령화지수"].values[0]
    value_dependency_2025 = year_2025["노년부양비"].values[0]

    # 노령화지수 그래프
    color1 = '#E91E63'
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    
    ax1.plot(data_5year["연도"], data_5year["노령화지수"], 
             marker='o', linewidth=2.5, markersize=8, 
             color='#1976D2', markerfacecolor='#64B5F6', markeredgewidth=1.5)

    # 2024년부터 잠정치 영역 표시
    ax1.axvspan(2024, 2072, alpha=0.1, color='orange')
    ax1.axvline(x=2024, color='orange', linestyle='--', linewidth=2, alpha=0.7, label='2024년 이후 잠정치')

    # 2025년 포인트 강조
    ax1.plot(2025, value_ageing_2025, marker='o', markersize=15, 
            color=color1, markeredgecolor='darkred', markeredgewidth=2, zorder=5)

    # 2025년 텍스트
    ax1.text(2025, value_ageing_2025 + 40, '2025년',
            ha='center', va='center', fontsize=9,
            color=color1, fontweight='bold')
    
    ax1.text(2030, value_ageing_2025 - 30, f'{value_ageing_2025:.1f}',
            ha='center', va='center', fontsize=14,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', 
                     edgecolor=color1, linewidth=2.5, alpha=0.95),
            color=color1, fontweight='bold')

    ax1.set_xlabel('연도', fontsize=13, fontweight='bold')
    ax1.set_ylabel('노령화지수', fontsize=13, fontweight='bold')
    ax1.set_title('노령화지수 변화 (1960-2072)', fontsize=14, fontweight='bold', pad=20)
    
    years = list(range(1960, 2075, 5))
    ax1.set_xticks(years)
    ax1.set_xticklabels(years, rotation=45, ha='right')
    
    ax1.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax1.set_axisbelow(True)
    ax1.set_facecolor('#F8F9FA')
    ax1.legend(loc='upper left', fontsize=10)
    
    plt.tight_layout()

    # 노년부양비 그래프
    color2 = '#E91E63'
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    
    ax2.plot(data_5year["연도"], data_5year["노년부양비"], 
             marker='o', linewidth=2.5, markersize=8, 
             color='#1976D2', markerfacecolor='#64B5F6', markeredgewidth=1.5)

    # 2024년부터 잠정치 영역 표시
    ax2.axvspan(2024, 2072, alpha=0.1, color='orange')
    ax2.axvline(x=2024, color='orange', linestyle='--', linewidth=2, alpha=0.7, label='2024년 이후 잠정치')

    # 2025년 포인트 강조
    ax2.plot(2025, value_dependency_2025, marker='o', markersize=15, 
            color=color2, markeredgecolor='darkred', markeredgewidth=2, zorder=5)

    # 2025년 텍스트
    ax2.text(2025, value_dependency_2025 + 5, '2025년',
            ha='center', va='center', fontsize=9,
            color=color2, fontweight='bold')
    
    ax2.text(2030, value_dependency_2025 - 5, f'{value_dependency_2025:.1f}',
            ha='center', va='center', fontsize=14,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', 
                     edgecolor=color2, linewidth=2.5, alpha=0.95),
            color=color2, fontweight='bold')

    ax2.set_xlabel('연도', fontsize=13, fontweight='bold')
    ax2.set_ylabel('노년부양비', fontsize=13, fontweight='bold')
    ax2.set_title('노년부양비 변화 (1960-2072)', fontsize=14, fontweight='bold', pad=20)
    
    ax2.set_xticks(years)
    ax2.set_xticklabels(years, rotation=45, ha='right')
    
    ax2.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax2.set_axisbelow(True)
    ax2.set_facecolor('#F8F9FA')
    ax2.legend(loc='upper left', fontsize=10)
    
    plt.tight_layout()

    # 그래프를 1:1 비율로 배치
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.pyplot(fig1)
        plt.close(fig1)
    with col2:
        st.pyplot(fig2)
        plt.close(fig2)
    st.caption("데이터 출처 : [국가데이터처](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1BPA002&conn_path=I2)「장래인구추계」, 2072, 2025.11.14, 주요 인구지표(성비,인구성장률,인구구조,부양비 등) / 전국")
    
    # 설명 섹션
    st.subheader("노령화지수 및 노년부양비")
    st.markdown("<h6>1960 ~ 2072</h6>", unsafe_allow_html=True)
    st.markdown("<h5>그래프 설명</h5>", unsafe_allow_html=True)
    st.markdown("**노령화지수**는 유소년인구(14세 이하) 100명에 대한 고령인구(65세 이상)의 비율이다.<br>**노년부양비**는 생산연령인구(15~64세) 100명에 대한 고령(65세 이상)인구의 비이다.<br>심화되는 초고령사회가 짊어질 부담의 정도를 대락적으로 확인할 수 있다.", unsafe_allow_html=True)
    
    with st.expander("원본 데이터 표 보기"):
        st.dataframe(data_df)

def graph_multicultural_furniture(): #다문화가정
    data_df = pd.read_csv("C:/Users/taehyeon/Desktop/2025-2/전공/데이터시각화/Project/다문화가구.csv", 
                          header=None, encoding="cp949")
    
    data = data_df.transpose()
    data.columns = data.iloc[0]
    data = data.drop(data.index[0])
    data = data.reset_index(drop=True)
    
    data.columns = ['연도', '다문화가구']  # 강제로 컬럼명 지정
    
    # 데이터 타입 변환
    data["연도"] = data["연도"].astype(float).astype(int)
    data["다문화가구"] = data["다문화가구"].astype(float)

    # 2024년 데이터 찾기
    year_2024 = data[data["연도"] == 2024]
    value_2024 = year_2024["다문화가구"].values[0]

    # color 설정
    colors = ['#64B5F6'] * len(data)
    colors[-1] = '#E91E63'  # 2024년을 강조색으로

    # 그래프 그리기
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # 바 그래프
    bars = ax.bar(data["연도"], data["다문화가구"], 
                  color=colors, edgecolor='#1976D2', linewidth=1.5, alpha=0.8)

    # 2024년 값 강조
    ax.text(2024, value_2024 + 20000, f'{value_2024:,.0f}',
            ha='center', va='center', fontsize=12,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', 
                     edgecolor='#E91E63', linewidth=2.5, alpha=0.95),
            color='#E91E63', fontweight='bold')

    # 축 설정
    ax.set_xlabel('연도', fontsize=13, fontweight='bold')
    ax.set_ylabel('다문화가구 수 (가구)', fontsize=13, fontweight='bold')
    ax.set_title('연도별 다문화가구 수 변화 (2015-2024)', fontsize=16, fontweight='bold', pad=20)
    
    # x축 설정
    ax.set_xticks(data["연도"])
    ax.set_xticklabels(data["연도"], rotation=45, ha='right')
    
    # y축 포맷 (천 단위 구분)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x):,}'))
    ax.set_ylim(200000, 500000)
    # 그리드 설정
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8, axis='y')
    ax.set_axisbelow(True)
    
    # 배경색 설정
    ax.set_facecolor('#F8F9FA')
    
    plt.tight_layout()

    col1, col2 = st.columns([2, 3])
    with col1:
        st.subheader("연도별 다문화가구 수")
        st.markdown("<h6>2015 ~ 2024</h6>", unsafe_allow_html=True)
        st.markdown("<h5>그래프 설명</h5>", unsafe_allow_html=True)
        st.markdown("""
        2015년부터 2024년까지 **대한민국의 다문화가구 수 변화**를 나타낸다.<br>
        다문화가구는 한국인과 외국인으로 이루어진 가구 또는 귀화자가 포함된 가구를 의미한다.<br>
        다문화가구는 지속적으로 증가하고 있었음을 보여주며, 이를 통해 인구의 유입과 저출산 해소의 힌트를 얻었다는 시각을 제시한다.
        """, unsafe_allow_html=True)
        with st.expander("원본 데이터 표 보기"):
            st.dataframe(data_df)
    with col2:
        st.pyplot(fig)
        st.caption("데이터 출처 : [국가데이터처](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1BZ0505&conn_path=I2)「장래가구추계」, 2052, 2025.11.14, 가구주의 연령/가구유형별 추계가구_시도")
    
    plt.close()

def graph_alone_household(): #1인가구
    data_df = pd.read_csv("C:/Users/taehyeon/Desktop/2025-2/전공/데이터시각화/Project/1인가구수.csv", 
                          header=None, encoding="cp949")
    
    data = data_df.transpose()
    data.columns = data.iloc[0]
    data = data.drop(data.index[0])
    data = data.reset_index(drop=True)

    # 컬럼명 강제 지정
    data.columns = ['연도', '1인가구수']
    
    # 데이터 타입 변환
    data["연도"] = data["연도"].astype(float).astype(int)
    data["1인가구수"] = data["1인가구수"].astype(float)

    # 2025년 데이터 찾기
    year_2025 = data[data["연도"] == 2025]
    value_2025 = year_2025["1인가구수"].values[0]

    # color 변수 설정
    color = '#E91E63'

    # 그래프 그리기
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # 선 그래프 (전체 데이터 사용)
    ax.plot(data["연도"], data["1인가구수"], 
            marker='o', linewidth=2.5, markersize=6, 
            color='#1976D2', markerfacecolor='#64B5F6', markeredgewidth=1.5)

    # 2025년 포인트 강조
    ax.plot(2025, value_2025, marker='o', markersize=15, 
            color=color, markeredgecolor='darkred', markeredgewidth=2, zorder=5)

    # 2025년 텍스트 - 위쪽 (테두리 없음)
    ax.text(2025, value_2025 - 300000, '2025년',
            ha='center', va='center', fontsize=9,
            color=color, fontweight='bold')
    
    # 2025년 값 박스 - 아래쪽 (큰 폰트, bbox 있음)
    ax.text(2025, value_2025 - 700000, f'{value_2025:,.0f}',
            ha='center', va='center', fontsize=12,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', 
                     edgecolor=color, linewidth=2.5, alpha=0.95),
            color=color, fontweight='bold')

    # 축 설정
    ax.set_xlabel('연도', fontsize=13, fontweight='bold')
    ax.set_ylabel('1인 가구 수 (가구)', fontsize=13, fontweight='bold')
    ax.set_title('연도별 1인 가구 수 변화 (2000-2025)', fontsize=16, fontweight='bold', pad=20)
    
    # x축 5년 단위로 강제 설정
    years = list(range(2000, 2030, 5))
    ax.set_xticks(years)
    ax.set_xticklabels(years, rotation=45, ha='right')
    
    # y축 포맷 (천 단위 구분)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x/1000000):.0f}M'))
    
    # 그리드 설정
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax.set_axisbelow(True)
    
    # 배경색 설정
    ax.set_facecolor('#F8F9FA')
    
    plt.tight_layout()
    
    return fig, data_df

def graph_alone_household_pie(): #1인가구 비율
    data_df = pd.read_csv("C:/Users/taehyeon/Desktop/2025-2/전공/데이터시각화/Project/1인가구비중.csv", 
                          header=None, encoding="cp949")
    
    data = data_df.transpose()
    data.columns = data.iloc[0]
    data = data.drop(data.index[0])
    data = data.reset_index(drop=True)

    # 컬럼명 강제 지정
    data.columns = ['연도', '전체가구수', '1인가구수']
    
    # 데이터 타입 변환
    data["연도"] = data["연도"].astype(float).astype(int)
    data["전체가구수"] = data["전체가구수"].astype(float)
    data["1인가구수"] = data["1인가구수"].astype(float)

    # 2025년 데이터 추출
    data_2025 = data[data["연도"] == 2025]
    total_household = data_2025["전체가구수"].values[0]
    alone_household = data_2025["1인가구수"].values[0]
    other_household = total_household - alone_household
    
    # 비율 계산
    alone_ratio = (alone_household / total_household) * 100
    other_ratio = (other_household / total_household) * 100

    # 파이 차트 데이터
    sizes = [alone_household, other_household]
    labels = ['1인 가구', '다인 가구']
    colors = ['#FF6B6B', '#A8D5BA']
    explode = [0.1, 0]  # 1인 가구 돌출

    # 파이 차트 생성
    fig, ax = plt.subplots(figsize=(10, 10))

    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        explode=explode,
        textprops={'fontsize': 20, 'fontweight': 'bold'},
        pctdistance=0.85
    )

    # 1인 가구 강조
    wedges[0].set_edgecolor('#D32F2F')
    wedges[0].set_linewidth(4)
    texts[0].set_fontsize(16)
    texts[0].set_color('#D32F2F')
    autotexts[0].set_color('white')
    autotexts[0].set_fontsize(16)

    # 다인 가구 스타일
    autotexts[1].set_fontsize(14)
    autotexts[1].set_fontweight('bold')

    # 제목
    plt.title('1인 가구 비중 (2025)', fontsize=25, fontweight='bold', pad=20)

    plt.tight_layout()
    
    return fig, data_df, total_household, alone_household, alone_ratio

def st_columns_household():
    # 데이터 로드
    fig_line, data_df_line = graph_alone_household()
    fig_pie, data_df_pie, total_household, alone_household, alone_ratio = graph_alone_household_pie()
    
    # 컨테이너 1: 그래프
    cont1 = st.container()
    with cont1:
        col1, col2 = st.columns([5, 2.445])
        with col1:
            st.pyplot(fig_line)
            plt.close(fig_line)
        with col2:
            st.pyplot(fig_pie)
            plt.close(fig_pie)
    
    # 컨테이너 2: 출처
    cont2 = st.container()
    with cont2:
        st.caption("데이터 출처 : [국가데이터처](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1BZ0505&conn_path=I2)「장래가구추계」, 2052, 2025.11.14, 가구주의 연령/가구유형별 추계가구_시도")
        st.caption("데이터 출처 : [국가데이터처](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1BZ0502&conn_path=I2)「장래가구추계」, 2052, 2025.11.14, 가구주의 연령/가구유형별 추계가구-전국")

        
    # 컨테이너 3: 설명
    cont3 = st.container()
    with cont3:
        col1, col2 = st.columns([5, 2.445])
        with col1:
            st.subheader("연도별 1인 가구 수")
            st.markdown("<h6>2000 ~ 2025</h6>", unsafe_allow_html=True)
            st.markdown("<h5>그래프 설명</h5>", unsafe_allow_html=True)
            st.markdown("""
            2000년부터 2025년까지 **1인 가구 수의 변화**를 나타낸다.<br>
            1인 가구는 1명이 독립적으로 취사, 취침 등 생계를 유지하는 가구를 의미한다.<br>
            2000년부터 지속적으로 증가하였으며, 2020년을 기점으로 1인 가구 증가세가 소폭 상승했음을 확인 가능하다.
            """, unsafe_allow_html=True)
            with st.expander("원본 데이터 표 보기"):
                st.dataframe(data_df_line)
        
        with col2:
            st.subheader("2025년 1인 가구 비중")
            st.markdown("<h6>전체 가구 대비 1인 가구</h6>", unsafe_allow_html=True)
            st.markdown("<h5>그래프 설명</h5>", unsafe_allow_html=True)
            st.markdown(f"""
            2025년 **전체 가구 중 1인 가구가 차지하는 비중**을 나타낸다.<br>
            전체 가구 중 **1인 가구가 {alone_ratio:.1f}%를 차지하고 있다.**<br>
            """, unsafe_allow_html=True)
            with st.expander("원본 데이터 표 보기"):
                st.dataframe(data_df_pie)

apply_web_font()
setting_matplotlib_font()
st.set_page_config(layout="wide")

st.title("대한민국 총인구 대시보드")
st.markdown("<h6>게시자 : 첨단IT학부 빅데이터전공 20223468 김태현</h6>", unsafe_allow_html=True)
st.divider()

def main() :
    cont1 = st.container()
    cont2 = st.container()
    cont3 = st.container()
    cont4 = st.container()
    
    with cont1 :
        st.markdown("<h3>Section 1 : 대한민국 인구 현황</h3>\n<h5>현재 대한민국의 인구가 '얼마나', '어떻게' 구성되어 있는지 확인할 수 있습니다.</h5>",unsafe_allow_html=True)
        graph_population()
        st_columns_SexAge()
        st.divider()
    with cont2 :
        st.markdown("<h3>Section 2 : 인구 감소 원인 확인</h3>\n<h5>대한민국의 인구성장률과 합계출산율을 통해 인구 감소의 원인을 확인할 수 있습니다.</h5>",unsafe_allow_html=True)
        graph_population_growrate()
        graph_fertility_rate()
        st.divider()
    with cont3 :
        st.markdown("<h3>Section 3 : 사회적 영향과 미래</h3>\n<h5>저출산이 고령화로 이어지는 과정과 결과, 이로 야기되는 사회적 부담을 확인할 수 있습니다.</h5>",unsafe_allow_html=True)
        graph_ageing_index()
        st.divider()
    with cont4 :
        st.markdown("<h3>Section 4 : 가구 구조의 변화</h3>\n<h5>사회를 구성하는 기본 단위인 '가구'의 형태 변화를 강조하며, 저출산 해결의 실마리인 다문화 가정을 제시합니다.</h5>",unsafe_allow_html=True)
        st_columns_household()
        graph_multicultural_furniture()


if __name__ == "__main__" :
    main()