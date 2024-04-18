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
        #if we wanted to delete a fieldname, we would having deleted the corresponding fieldname from our 'fieldnames' list:
        #del line['description']
        #del line['industry']
        #del line['level']
        #del line['size']
        #del line['line_code']
        #del line['value']
        #del line['status']
        #del line['Unit']
        #del line['Footnotes']
        
        #if we wanted to add a fieldname, we would:
        line['description'] = line['description'] + " " + line['industry'] + " " + line['level'] + " " + line['size'] + " " + line['line_code'] + " " + line['value'] + " " + line['status'] + " " + line['Unit'] + " " + line['Footnotes']
        
        print(line['description'])
        print(line['industry'])
            
        
    # for line in csv_reader:
    #     print(line[2])
    
