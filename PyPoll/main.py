import os
import csv


votes = []
candidates = []


csv_path = os.path.join('Resources','Election_Data.csv')
path_out = os.path.join('Analysis','Election_Analysis.txt')


with open(csv_path) as csv_file:
   csv_reader = csv.reader(csv_file, delimiter = ',')
   csv_header = next(csv_reader)
   
  
   for column in csv_reader:
      votes.append(column[0])
      candidates.append(column[2])

    
   Total_Votes = (len(votes))
   

   Khan = int(candidates.count('Khan'))
   Correy = int(candidates.count('Correy'))
   Li = int(candidates.count('Li'))
   O_Tooley = int(candidates.count("O'Tooley"))
  

   Khan_percentage = format((Khan/Total_Votes) * 100 ,'.3f')
   Correy_percentage = format((Correy/Total_Votes) * 100,'.3f')
   Li_percentage = format((Li/Total_Votes) * 100,'.3f')
   O_Tooley_percentage = format((O_Tooley/Total_Votes) * 100,'.3f')
 
  
   if Khan > Correy > Li > O_Tooley:
      Winner = 'Khan'
    
   elif Correy > Khan > Li > O_Tooley:
      Winner = 'Correy'
    
   elif Li > Khan > Correy > O_Tooley:
      Winner = 'Li'
    
   elif O_Tooley > Khan > Correy > Li:
      Winner = "O'Tooley"
   
   
print('----------------------------')
print('Election Results')
print('----------------------------')    
print(f'Total Votes: {Total_Votes}')
print('----------------------------') 
print(f'Khan: {Khan_percentage}% ({Khan})')
print(f'Correy: {Correy_percentage}% ({Correy})')
print(f'Li: {Li_percentage}% ({Li})')
print(f"O'Tooley: {O_Tooley_percentage}% ({O_Tooley})")
print('----------------------------')
print(f'Winner: {Winner}')
print('----------------------------')

with open(path_out, 'w') as output:

    output.write('----------------------------\n')
    output.write('Election Results\n')
    output.write('----------------------------\n')    
    output.write(f'Total Votes: {Total_Votes}\n')
    output.write('----------------------------\n') 
    output.write(f'Khan: {Khan_percentage}% ({Khan})\n')
    output.write(f'Correy: {Correy_percentage}% ({Correy})\n')
    output.write(f'Li: {Li_percentage}% ({Li})\n')
    output.write(f"O'Tooley: {O_Tooley_percentage}% ({O_Tooley})\n")
    output.write('----------------------------\n')
    output.write(f'Winner: {Winner}\n')
    output.write('----------------------------\n')