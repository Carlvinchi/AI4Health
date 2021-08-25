import predictor

mdel_name = 'Naive Bayes'
sym1 = 'Fever'
sym2 = 'Headache'
sym3 = 'Vomiting'
sym4 = ''
sym5 = ''
sym6 = ''
result =predictor.tester(mdel_name,sym1,sym2,sym3,sym4,sym5,sym6)
print(result)