# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 10:32:50 2021

@author: NAVYA .P
"""

x = 'Grow Gratitude'
x[0] #G
len(x) #14
x.count('G') #2

y ='Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else. '
len(y)
# 119

z = "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"
z[0] #I
z[0:3] # Ide
z[-3:] #lth

I = "stay positive and optimistic"
i_split = I.split(' ')
i_split
# ['stay', 'positive', 'and', 'optimistic']

count =0
for i in i_split:
    if i[0] == 'H':
        print(i)
    count += 1
# no word starts with H

  
count =0
for i in i_split:
    if i[-1] == 'd':
        print(i)
    count += 1
#and

count =0
for i in i_split:
    if i[-1] == 'c':
        print(i)
    count += 1
# optimistic


f = '🪐'*108
print(f)


c = 'Grow Gratitude'
c = c.split(' ')
c[0] = 'Growth'
print(c)
string = ''
string = string.join(c)
print(string)


story = '''.elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh 
,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT
 .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .
 ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .
 eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,
 peels s’noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A'''

new_story = story[::-1]
print(new_story)








