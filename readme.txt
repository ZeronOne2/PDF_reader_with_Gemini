# PDF 리더 with Gemini AI

이 프로젝트는 Streamlit과 Gemini AI를 사용하여 PDF 파일의 내용을 읽고, 사용자의 질문에 대해 답변을 생성하는 웹 애플리케이션입니다.

## 기능

- 사용자가 PDF 파일을 업로드할 수 있습니다.
- 사용자가 Gemini API 키를 입력할 수 있습니다.
- PDF 내용에 대해 질문을 입력하면, Gemini AI가 답변을 생성합니다.

## 설치

이 프로젝트를 실행하기 위해서는 Python과 필요한 라이브러리들이 설치되어 있어야 합니다.

1. Python 3.7 이상이 설치되어 있는지 확인하세요.
2. 다음 명령어를 사용하여 필요한 라이브러리들을 설치하세요:

   ```bash
   pip install streamlit google-generativeai PyPDF2
   ```

3. 가상 환경을 사용하는 것이 좋습니다. 가상 환경을 설정하려면:

   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # Windows
   # 또는
   source myenv/bin/activate  # macOS/Linux
   ```

## 사용법

1. 이 저장소를 클론하거나 다운로드합니다.
2. 터미널에서 프로젝트 디렉토리로 이동합니다.
3. 다음 명령어를 사용하여 웹 애플리케이션을 실행합니다:

   ```bash
   streamlit run gemini_pdf_reader.py
   ```

4. 웹 브라우저에서 로컬 서버 주소로 이동하여 애플리케이션을 사용합니다.
5. Gemini API 키를 입력하고, PDF 파일을 업로드한 후 질문을 입력하여 답변을 확인합니다.

## 주의사항

- 이 애플리케이션을 사용하려면 유효한 Gemini API 키가 필요합니다.
- PDF 파일의 내용이 많을 경우, 처리 시간이 길어질 수 있습니다.

## 기여

기여를 원하신다면, 이 저장소를 포크하고 변경 사항을 푸시한 후 풀 리퀘스트를 보내주세요.

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 LICENSE 파일을 참조하세요.