import csv

#reading a csv file using 1:regular reader; 2: DictReader, check encoding; default encoding is UTF-8
# with open("newname.csv", "r", encoding='latin1') as file:
#     csv_reader = csv.reader(file, delimiter='\t')
#     for line in csv_reader:
#         print(line)

with open("bns.csv", "r", encoding='latin1') as file:
    csv_reader = csv.DictReader(file)
    #next(csv_reader) #generator
    
    #writing to a csv file
    with open("newname.csv", "w") as newfile:
        fieldnames = ['description','industry','level','size','line_code','value','status','Unit','Footnotes']
        csv_writer = csv.DictWriter(newfile, fieldnames=fieldnames, delimiter='\t')
        
        #wwrite headers(optional)
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)
    
    for line in csv_reader:
        print(line['industry'])
            
        
    # for line in csv_reader:
    #     print(line[2])
    
