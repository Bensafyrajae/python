family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
def  payer_age(a):
    if a < 3:
        return 0
    elif  3< a <12 :
        return 10
    else:
        return 12
cout= 0
for key , value in family.items():
    cout += payer_age(value)

print(f' le coût total des films pour la famille {cout}')
