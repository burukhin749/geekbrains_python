tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б']

result = ((tutors[n], klasses[n]) if len(klasses) > n else (tutors[n], None) for n in range(len(tutors)))

print(type(result), *result, sep='\n')
print(next(result))
