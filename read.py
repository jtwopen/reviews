data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)

sum_len = 0
for d in data:
	sum_len += len(d)
print(sum_len / len(data))


wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 10000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('請輸入想查找的字: ')
	if word == 'q':
		print('感謝使用本程式')
		break
	elif word in wc:
		print(word, '出現過的次數是', wc[word], '次')
	else:
		print('此字不在字典裡,請重新輸入')