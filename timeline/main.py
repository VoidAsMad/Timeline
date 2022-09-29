from client import Timeline
import os


time = Timeline()
while True:

    year: str = input(
        f"\033[37m---------------\n\033[32m연도를 입력해주세요! ex) 1976\n\033[37m---------------\n> "
    )
    text: str = input(
        "\033[37m---------------\n\033[32m데이터를 입력해주세요!\n\033[37m---------------\n> "
    )
    time.append(year, text)

    while True:
        if_close = input(
            "\033[37m---------------\n\033[31m종료하기 : y\n\033[92m계속 추가하기 : n\n\033[37m---------------\n> "
        )
        if_close = if_close.lower()
        if if_close == "" or not if_close in ["y", "n"]:
            print("'y' 또는 'n'만 입력해주세요!")
        else:
            os.system("cls")
            break

    if if_close == "y":
        break
    else:
        pass

print(time._return())
os.system("pause")
