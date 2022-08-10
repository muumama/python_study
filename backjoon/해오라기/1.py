chess_dong = list(map(int,input().split()))
chess_setting = [1, 1, 2, 2, 2, 8]

final_setting = []

for i in range(len(chess_dong)):

  setting = (chess_setting[i] - chess_dong[i])
  final_setting.append(setting)

print(*final_setting)
