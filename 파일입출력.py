# score_file = open("score.txt", 'w', encoding='utf-8')
# print("수학: 45", file=score_file)
# print("영어: 55", file=score_file)
# score_file.write("과학: 80\n")
# score_file.write("코딩: 100\n")
# score_file.close()
#
# score_file = open("score.txt", 'r', encoding='utf-8')
# print(score_file.read())
# score_file.close()

score_file = open('score.txt', 'r', encoding='utf-8')
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end='')
score_file.close()

score_file = open('score.txt', 'r', encoding='utf-8')
line = score_file.readline()
for line in score_file:
    print(line, end='')
score_file.close()