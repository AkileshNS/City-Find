import pandas as pd

df = pd.read_csv("Final Final/Kannada.csv")

northset = {'Belgaum / Belagavi','Uttara Kannada / Karwar','Vijayapura / Bijapur','Raichur','Koppal','Gadag','Bidar','Gulbarga / Kalaburagi', 'Yadgir','Hubli','Dharwad', 'Haveri', 'Bagalkot', 'Bellary / Ballari' }

southset = {'Kolar',
    'Chikballapur',
    'Bangalore City',
    'Bangalore Rural',
    'Tumkur',
    'Shimoga',
    'Davanagere',
    'Chitradurga',
    'Mandya',
    'Ramanagara',
    'Chamarajnagar',
    'Hassan'
}

southwset = {'Mysore',
    'Dakshina Kannada',
    'Chikmagalur',
    'Kodagu / Coorg'
}

coastal = {
    'Udupi',
    'Mangalore'
}

#n repts no. of dialects
n = 4
l1 = []
countl = [0]*n

for i in range(0,df.shape[0]):

    if df['City'][i] in northset:
        countl[0]+=1
        
    elif df['City'][i] in southset:
        countl[1]+=1

    elif df['City'][i] in southwset:
        countl[2]+=1

    elif df['City'][i] in coastal:
        countl[3]+=1



for i in range(0,df.shape[0]):
    
    if df['City'][i] in northset:
        l1.append('Northern Kannada - Sample Size'+'('+str(countl[0])+')')

    elif df['City'][i] in southset:
        l1.append('Southern Kannada - Sample Size'+'('+str(countl[1])+')')

    elif df['City'][i] in southwset:
        l1.append('South Western Kannada - Sample Size'+'('+str(countl[2])+')')

    elif df['City'][i] in coastal:
        l1.append('Coastal Kannada - Sample Size'+'('+str(countl[3])+')')


df['dialectlabel'] = l1

df.to_csv('Final Final/KannadaDialectt.csv',index=False)

