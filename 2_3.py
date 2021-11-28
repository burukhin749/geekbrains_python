broken_sentence = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, v in enumerate(broken_sentence):
    if v.isdigit():
        broken_sentence[i] = f'"{int(v):02}"'
    elif v[1:].isdigit():
        broken_sentence[i] = f'"{v[0]}{int(v[1:]):02}"'

print(broken_sentence)
print(" ".join(broken_sentence))
