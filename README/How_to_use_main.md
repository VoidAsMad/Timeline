# 연표 작성 프로그램 (Version 1.0.0)
연표를 쉽게 작성 할 수 있도록 도와주는 프로그램입니다!<br>
**[다운로드](https://github.com/VoidAsMad/Timeline/archive/refs/heads/main.zip)**

## 사용법
1. Python을 설치해주세요! ([설치하기](https://www.python.org/downloads/))
2. timeline 폴더 안에 있는 `setup.py`를 실행시켜주세요!<br>(**설치가 완료되었습니다! 창을 종료후 main 파일을 실행시켜주세요!** 라는 창이 뜰때까지 창을 닫지 마세요!)
3. timeline 폴더 안에 있는 `main.py`를 실행시켜주세요!
4. 날짜를 적어주세요! `ex) 1919, 1919년, 1919년 3월 1일` 등등
5. 내용을 작성해주세요! `ex) 3.1 운동이 일어남`
6. 계속 작성하실려면 `n`를 입력한 결과를 볼려면 `y`를 입력해주세요!

## 출력값
```json
{
    "1919" : "3.1 운동이 일어남",
    "1945" : ["안네의 일기의 저자 안네 프랑크가 사망하였다.", "8월 15일, 대한제국이 독립해서 8.15 광복을 맞이했다."] 
}
```

## 특징
1. 자동으로 **결과값이 복사**됩니다.
2. 연도가 같은 데이터는 리스트의 형태로 지원합니다.
