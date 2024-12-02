import streamlit as st
import google.generativeai as genai
import PyPDF2
import io

def main():
    st.title("PDF Readerbot")
    
    # API 키 입력
    api_key = st.text_input("당신의 Gemini API 키를 입력하세요", type="password")
    
    # PDF 파일 업로더
    uploaded_file = st.file_uploader("PDF 파일을 업로드하세요", type=['pdf'])
    
    if uploaded_file and api_key:
        # Gemini API 설정
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-pro-002')
        
        # PDF 텍스트 추출
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text_content = ""
        for page in pdf_reader.pages:
            text_content += page.extract_text()
            
        # 사용자 질문 입력
        user_question = st.text_input("PDF에 대해 질문하세요")
        
        if user_question:
            # Gemini API로 질문 처리
            prompt = f"다음 PDF 내용에 대해 답변해주세요: {user_question}\n\nPDF 내용: {text_content}"
            response = model.generate_content(prompt)
            
            # 응답 표시
            st.write("답변:")
            st.write(response.text)

if __name__ == "__main__":
    main()
