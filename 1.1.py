num=0 #맵 크기를 그때마다 바꾸려는 노력의 흔적
playmap= [[0,0,0,0,0,0,0,0,0,0] #맵
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]]
flag = 0 #턴


def print_board(): #맵 출력 명령어
    print("   " + " ".join(f"{i}" for i in range(10)))
    for i, row in enumerate(playmap):
        print(f"{i} " + " ".join(str(cell) if cell != 0 else "." for cell in row))
    print()

def victory(): #규칙 명령어
    for i in range(10):
        for j in range(10 - 4):
            if playmap[i][j] == playmap[i][j + 1] == playmap[i][j + 2] == playmap[i][j + 3] == playmap[i][j + 4] != 0:
                return True
            if playmap[j][i] == playmap[j + 1][i] == playmap[j + 2][i] == playmap[j + 3][i] == playmap[j + 4][i] != 0:
                return True

    for i in range(10 - 4):
        for j in range(10 - 4):
            if playmap[i][j] == playmap[i + 1][j + 1] == playmap[i + 2][j + 2] == playmap[i + 3][j + 3] == playmap[i + 4][j + 4] != 0:
                return True
            if playmap[i][j + 4] == playmap[i + 1][j + 3] == playmap[i + 2][j + 2] == playmap[i + 3][j + 1] == playmap[i + 4][j] != 0:
                return True
    return False

#턴 주고받기
while True:
    print_board()
    x, y = map(int, input("0과 9 사이의 숫자 2개를 입력해주세요 (예: 3 5): ").split())
    
    if x < 0 or x >= 10 or y < 0 or y >= 10: 
        print("범위 외 값입니다. 다시 입력해주세요.")
        continue
    
    if playmap[x][y] != 0:
        print("다른이가 이미 둔 자리입니다. 다시 입력해주세요.")
        continue

    if flag == 0:
        playmap[x][y] = "A"
        flag = 1
    else:
        playmap[x][y] = "B"
        flag = 0

#게임 종료
    if victory():
        print_board()
        print(f"플레이어 {'A' if flag == 1 else 'B'}가 승리했습니다!")
        break
