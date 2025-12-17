import matplotlib.pyplot as plt 
import csv 
  
x = [] 
y = [] 
  
with open('PPC-python\MACHINE LEARNING\cardata.csv','r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
      
    for row in plots: 
        x.append(row[0]) 
        y.append((row[3])) 
  
plt.bar(x, y, color = 'g', width = 0.75, label = "Weight") 
plt.xlabel('Car') 
plt.ylabel('Weight') 
plt.title('Weight of car') 
plt.legend() 
plt.show() 