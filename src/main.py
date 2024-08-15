import csv
import constants
def read():
    file=open(f"{constants.filesPath}/input_data.csv")
    csvReader =csv.reader(file)
    data = list(csvReader)
    file.close()
    return data

def write(data):
    file = open(f"{constants.filesPath}/output_data.csv","w")
    csvWriter = csv.writer(file)
    csvWriter.writerows(data)
    file.close()

def transformData(personsData):
    ageIndex =-1
    for index in range(len(personsData[0])):
        if personsData[0][index].strip() == "Age":
            ageIndex = index

    if ageIndex ==-1:
        raise Exception("Age is not present in data")
    
    personsData[0].append("Person Type")
    for index in range(1,len(personsData)):
        person = personsData[index]
        age = int(person[ageIndex])
        personType=""
        
        if age<18:
            personType = "Child"
        elif age>=18 and age<60:
            personType = "Young"
        else:
            personType = "Senior Citizen"
        
        person.append(personType)

def main():
    data =read()
    transformData(data)
    write(data)
   

main()