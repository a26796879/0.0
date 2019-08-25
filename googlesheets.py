import pygsheets as pyg
import numpy as np

gc = pyg.authorize(service_file='D:/Python Codes/My Project 87532-60e5410c48f8.json')

sh = gc.open('TEST')

wks = sh.sheet1
#wks.append_table(values=[123,645,978])
wks.update_value('A1', "Hey yank this numpy array")

for i in range(2,10):
    wks.update_value('A'+str(i),i-1)

print ('OK')
