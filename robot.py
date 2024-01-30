import streamlit as st 
import requests
import pandas as pd 

def check_url(url):
    robot_url = f"{url}/robots.txt"
    response = requests.get(robot_url)
    return '예' if response.status_code == 200 else '아니오'

def main():
    st.title("robot.txt 파일 검색 서비스")
    # url = st.text_input("검색할 사이트 URL을 입력하세요.")
    
    uploaded_file = st.file_uploader("사이트 URL 포함된 엑셀 업로드", type=['xlsx', 'csv', 'txt'])
    
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        df['robots.txt 존재 여부'] = df['URL'].apply(check_url)
        
        st.dataframe(df)
        
if __name__ == "__main__":
    
    main()
    
    