# 피아노 매크로 사용방법

## 설치 방법
기본적으로 이걸 쓰려면 프로그램을 몇개 설치해야함.
1. 파이썬 3 설치하기

[파이썬 3 다운로드 링크](https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe)를 눌러서 다운로드하고 설치하면 됨.

2. 실행에 필요한 각종 라이브러리 설치하기

파이썬 3를 설치한 다음, 실행(Win+R)을 켜서 cmd를 쳐서 들어간다음,

```
pip install mido pyautogui
```
로 설치하면 됨.

## 사용 방법

사용방법은 음원 소스의 종류에 따라 달라짐.
음원 소스는
- MIDI 파일
- PDF 악보
- 피아노 음원

이렇게 있는데, 각 방법에 대해서 설명하겠음

### MIDI 파일

제일 간단한 방법임. 프로그램에 넣고 돌리면 끝임.
```
python3 macro.py --file "MIDI파일 경로"
```

이 명령어를 입력하고 5초 후 자동으로 피아노가 연주됨.

### PDF 악보

악보를 MIDI파일로 변환해야함. 여기에는 일반적으로 Audiveris라는 프로그램이 사용됨.

[Audiveris 다운로드 링크](https://github.com/Audiveris/audiveris/releases/download/5.3.1/Audiveris_Setup-5.3.1-windows-x86_64.exe)

이걸로 악보를 MIDI파일로 바꾼다음, 프로그램에 넣고 돌리면 됨.

### 피아노 음원

이 경우, 인공지능을 이용해서 음원을 MIDI로 변환해야함.

[변환기 링크](https://colab.research.google.com/drive/1eL7XaiPQ4crfKMv2QLd-MLcedqjAywN3)

위 링크에 들어가서 첫번째 블럭을 실행한다음, 두번째 블럭에 유튜브 음원 URL을 넣고 돌리면 자동으로 변환된 MIDI가 다운로드됨

이걸 프로그램에 넣고 돌리면 됨.