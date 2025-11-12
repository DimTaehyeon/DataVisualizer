import streamlit as st
#on terminal, streamlit run (path)
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.ticker as ticker
from matplotlib import rc

def apply_web_font(): #Streamlit 웹에 Pretendard 웹 폰트 적용
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
    font_path = 'C:/Users/taehyeon/Desktop/2025-2/전공/데이터시각화/Project/Pretendard-Bold.ttf' # (Pretendard-Bold.ttf도 가능)
    
    fm.fontManager.addfont(font_path)
    
    font_prop = fm.FontProperties(fname=font_path)
    
    plt.rcParams['font.family'] = font_prop.get_name()
    plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

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
        st.markdown(f'<div class="decrease-label">{years[max_population_index]}년도 대비 약 {decrease_rate:.2f}% 감소 <br>↓ {format(decrease_value, ",")}명</div>', unsafe_allow_html=True)
        
        st.markdown("<h5>그래프 설명</h5>", unsafe_allow_html=True)
        st.markdown("1960년부터 2025년까지 **국내에 상주하고 있는 외국인을 포함한 인구의 총합이다.** <br>argmax()함수를 이용하여 인구 수의 최대치인 시점을 찾고, axvline을 통해 해당 지점을 시각화하였다.", unsafe_allow_html=True)
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

    # figsize를 (가로, 세로) = (10, 10)으로 동일하게 설정
    plt.figure(figsize=(10, 8))

    plt.bar([i - width/2 for i in x], male, width, label='남성', color='skyblue')
    plt.bar([i + width/2 for i in x], female, width, label='여성', color='pink')

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
                    f'{male_change:+.2f}%\n{abs(male[i] - male[i-1])}명 감소', 
                    ha='center', va='bottom', fontsize=9, fontweight='bold', color='#2E86AB')
            
            #여성 증감률
            female_change = ((female[i] - female[i-1]) / female[i-1]) * 100
            plt.text(i + width/2, female[i] + female.max() * 0.0002, 
                    f'{female_change:+.2f}%\n{abs(female[i] - female[i-1])}명 감소', 
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

    cont1 = st.container()
    cont2 = st.container()

    with cont1 : 
        st.pyplot(plt)
    with cont2 :
        st.markdown("<h5>그래프 설명</h5>", unsafe_allow_html=True)
        st.markdown("**2020년과 2025년의 남녀 인구이다.** <br>", unsafe_allow_html=True)
        st.caption("데이터 출처 : [국가데이터처](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1BPA001&conn_path=I2)「장래인구추계」, 2072, 2025.11.05, 성 및 연령별 추계인구(1세별, 5세별) / 전국")
        
        with st.expander("원본 데이터 표 보기"):
            st.dataframe(data)
    plt.close()

def graph_population_age() : #연령에 따른 파이 그래프
    data = pd.read_csv("C:/Users/taehyeon/Desktop/2025-2/전공/데이터시각화/Project/연령.csv", encoding = "cp949")

    max_age = data["2025"].argmax()
    min_age = data["2025"].argmin()

    colors = plt.cm.Set3(range(len(data)))

    # explode 설정 (돌출 효과)
    explode = [0] * len(data)
    explode[max_age] = 0.1  # 최대값 돌출
    explode[min_age] = 0.1  # 최소값 돌출

    # 파이 차트 생성 - figsize를 (10, 10)으로 동일하게 설정
    fig, ax = plt.subplots(figsize=(10, 10))

    wedges, texts, autotexts = ax.pie(
        data["2025"].values, 
        labels=data["연령별"].values,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        explode=explode,
        textprops={'fontsize': 10},  # 레이블 폰트 크기
        pctdistance=0.85
    )

    # 가장 많은/적은 연령대 하이라이트
    for i, (wedge, text, autotext) in enumerate(zip(wedges, texts, autotexts)):
        if i == max_age:
            wedge.set_edgecolor('red')
            wedge.set_linewidth(3)
            text.set_fontsize(13)
            text.set_fontweight('bold')
            text.set_color('red')
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(11)
        elif i == min_age:
            wedge.set_edgecolor('blue')
            wedge.set_linewidth(3)
            text.set_fontsize(13)
            text.set_fontweight('bold')
            text.set_color('blue')
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(11)
        else:
            autotext.set_fontsize(9)

    # 제목
    plt.title('2025년 연령대별 인구 비율', fontsize=16, fontweight='bold', pad=20)

    # 범례 추가
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', 
                markersize=10, markeredgecolor='red', markeredgewidth=2,
                label=f'최다: {data["연령별"].iloc[max_age]} ({data["2025"].iloc[max_age]:,}명)'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', 
                markersize=10, markeredgecolor='blue', markeredgewidth=2,
                label=f'최소: {data["연령별"].iloc[min_age]} ({data["2025"].iloc[min_age]:,}명)')
    ]
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

    plt.tight_layout()

    cont1 = st.container()
    cont2 = st.container()
    
    with cont1 :
        st.pyplot(fig)
    with cont2 :
        st.markdown("<h5>그래프 설명</h5>", unsafe_allow_html=True)
        st.markdown("**2025년의 연령대별 인구 비율이다.** <br>", unsafe_allow_html=True)
        st.caption("데이터 출처 : [국가데이터처](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1BPA001&conn_path=I2)「장래인구추계」, 2072, 2025.11.05, 성 및 연령별 추계인구(1세별, 5세별) / 전국")
        
        with st.expander("원본 데이터 표 보기"):
            st.dataframe(data)
    plt.close()

def st_columns_SexAge() :
    col1, col2 = st.columns([1, 1])

    with col1 :
        graph_population_sex()
    with col2 :
        graph_population_age()
apply_web_font()
setting_matplotlib_font()
st.set_page_config(layout="wide")

st.title("대한민국 총인구 대시보드")
st.markdown("<h6>게시자 : 첨단IT학부 빅데이터전공 20223468 김태현</h6>", unsafe_allow_html=True)

graph_population()
st.divider()
st_columns_SexAge()