import pandas as pd
import pdfplumber
import pikepdf
import os

'''Global Variables'''

HOUSE_NAME_VARIABLE = ('House', 'house')
NAME_VARIABLE = ('Name', 'Name:', 'name', 'name:')
AGE_VARIABLE = ('age:', 'Age:', 'gAe:', '||Age:', '||Age', '||gAe', '||gAe:')
NUMBER_VARIABLE = ('number', 'number:', 'Number', 'Number:','Number!')
GUARDIAN_VARIABLE = ("Father's", "Mother's", "Husband's", "Fathers", "Mothers", "Husbands", "Other's", 'Others')
GENDER_VARIABLE = ('Gender:', 'Gender')
WASTE_WORDS = ('Photo',':'," ","",'is','i',"Available")

def cleanLine(line):
    line = [x for x in line if x != ':']
    return line


def refactorBefore(epic):
    epic = epic.replace('-', '')
    epic = epic.replace('.', '')
    epic = epic.replace('XQ7', 'XOZ')
    epic = epic.replace('X07', 'XOZ')
    epic = epic.replace('X0Z', 'XOZ')
    epic = epic.replace('XO7', 'XOZ')
    
    epic = epic.replace("8ON" ,"SQN")
    epic = epic.replace('50N', 'SQN')
    epic = epic.replace('3QN', 'SQN')
    epic = epic.replace('30N', 'SQN')

    epic = epic.replace('111', 'ITI')
    epic = epic.replace('1T1', 'ITI')
    epic = epic.replace('110', 'ITI')
    epic = epic.replace('IT1', 'ITI')
    epic = epic.replace('[11', 'ITI')
    return epic

def refactorEpic(epic):
    epic = epic.replace('1RD', 'TRD')
    epic = epic.replace('D1G', 'DTC')
    epic = epic.replace('D1C', 'DTC')
    epic = epic.replace('XV7', 'HVZ')
    epic = epic.replace('K7S', 'KZS')
    epic = epic.replace('K75', 'KZS')
    epic = epic.replace('KZ5', 'KZS')
    epic = epic.replace('K7S', 'KZS')
    epic = epic.replace('TN7', 'TNZ')
    epic = epic.replace('1NZ', 'TNZ')
    epic = epic.replace('1N7', 'TNZ')
    epic = epic.replace('GP7', 'GPZ')
    epic = epic.replace('1IV', 'TIV')
    epic = epic.replace('WR1', 'WRT')





    epic = epic.replace('T3T', 'TST')
    epic = epic.replace('1S1', 'TST')
    epic = epic.replace('T5T', 'TST')
    epic = epic.replace('T51', 'TST')
    epic = epic.replace('TS1', 'TST')
    epic = epic.replace('1ST', 'TST')
    epic = epic.replace('HP7', 'HPZ')
    epic = epic.replace('TN7', 'TNZ')
    epic = epic.replace('GP7', 'GPZ')
    epic = epic.replace('15T', 'TST')
    epic = epic.replace('MD5', 'MDS')
    epic = epic.replace('MD3', 'MDS')



    epic = epic.replace('XQ7', 'XOZ')
    epic = epic.replace('X07', 'XOZ')
    epic = epic.replace('X0Z', 'XOZ')
    epic = epic.replace('XO7', 'XOZ')
    # print("before = ",epic)
    epic = epic.replace('1GD', 'ICD')
    epic = epic.replace('1CD', 'ICD')
    epic = epic.replace('XQ7', 'XOZ')
    epic = epic.replace('B5D', 'BSD')
    epic = epic.replace('Y5E', 'YSE')
    epic = epic.replace('F1B', 'FTB')
    epic = epic.replace('Y5E', 'YSE')
    epic = epic.replace('Y3E', 'YSE')

    epic = epic.replace('J1R', 'JTR')
    epic = epic.replace('F1B', 'FTB')

    epic = epic.replace('K8X', 'KSX')
    epic = epic.replace('K5X', 'KSX')
    epic = epic.replace('5QN', 'SQN')
    epic = epic.replace('DP5', 'DRS')
    epic = epic.replace('DP3', 'DRS')
    
    epic = epic.replace('B5B', 'BSB')
    epic = epic.replace('JR5', 'JRS')
    epic = epic.replace('DR5', 'DRS')
    epic = epic.replace('DR8', 'DRS')
    epic = epic.replace('1OK', 'TQK')
    epic = epic.replace('TOK', 'TQK')
    epic = epic.replace('T0K', 'TQK')
    epic = epic.replace('10K', 'TQK')
    epic = epic.replace('K5X', 'KSX')
    
    epic = epic.replace('-', '')
    epic = epic.replace('X5U', 'XSU')
    epic = epic.replace('X3U', 'XSU')
    epic = epic.replace('R7N', 'RZN')
    epic = epic.replace('L/P', 'LZP')
    epic = epic.replace('1T1', 'ITI')
    epic = epic.replace('[11', 'ITI')
    epic = epic.replace('F11', 'ITI')
    epic = epic.replace('G1D', 'GTD')
    epic = epic.replace('GT0', 'GTD')
    epic = epic.replace('-', '')
    #######################################################
    # #print(epic)
    temp = epic[3:].replace('g', '9')

    #######################################################
    # temp = temp.replace('T','7')
    temp = temp.replace('€','6')
    temp = temp.replace('G','9')
    temp = temp.replace('D','0')
    temp = temp.replace('i','1')
    temp = temp.replace('l','1')


    #######################################################
    epic = epic[:3] + ''.join(temp)
    temp = epic[3:].replace('O', '0')
    epic = epic[:3] + ''.join(temp)
    # if not epic[:3].isalpha():
    #     return ''
    temp = epic[:3].replace('0', 'Q')
    epic = ''.join(temp)+epic[3:] 

    temp = epic[:3].replace('5', 'S')
    epic = ''.join(temp)+epic[3:] 
    # #print(epic)
    if len(epic) != 10:
        epic = ''
    # print("after = ",epic)
    return epic



def getEpicNumbers(epic_numbers_list, count_of_name):
    group_of_numbers = []
    for n in epic_numbers_list:
        if (n.isalnum() == True and n.isalpha() == False and n.isnumeric() == False and len(n) >= 9) or (
                len(n) >= 9 and n[-1] == '.') or (len(n) >= 10 and n[-1] == ','):
            group_of_numbers.append(n)
    # #print(group_of_numbers)

    if count_of_name == len(group_of_numbers):
        group_of_numbers = [refactorEpic(x) for x in group_of_numbers]
        # #print(group_of_numbers)
        return group_of_numbers
    else:
        try:
            # #print('entered')
            temp = []
            i = 0
            cnt = 0
            while i < epic_numbers_list.__len__():
                # #print(temp)
                epic_numbers_list[i] = refactorBefore(epic_numbers_list[i])
                if cnt >= count_of_name:
                    break
                if epic_numbers_list[i][0].isalpha() or (
                        len(epic_numbers_list[i]) > 1 and epic_numbers_list[i][1].isalpha()):

                    current = ''.join(epic_numbers_list[i])
                    # #print('starting current = ',current)
                    i += 1
                    while current.__len__() <= 9:
                        # #print("updated current = ",current)
                        current = current + "".join(epic_numbers_list[i])
                        i += 1
                        # #print("updated current = ",current)
                    temp.append(refactorEpic(current))
                    cnt += 1
                else:
                    i += 1
            # #print('temp=',temp)
            if temp.__len__() == count_of_name:
                return temp
            else:
                return [''] * count_of_name

        except Exception as p:
            return [''] * count_of_name


def getGuardianData(guardian_list, count_of_name):
    extracted_list = []
    i = 0
    while i < len(guardian_list):
        if guardian_list[i] in GUARDIAN_VARIABLE:
            # #print('lalal')
            # traverse till you get Name
            while i < len(guardian_list) and guardian_list[i] not in NAME_VARIABLE:
                i += 1
            Name = guardian_list[i + 1]
            # Remove below part if you get errors
            if i + 2 < len(guardian_list) and guardian_list[i + 2] not in GUARDIAN_VARIABLE:
                Name += ' ' + guardian_list[i + 2]
            extracted_list.append(Name)
        else:
            i += 1
    # #print(extracted_list)
    if len(extracted_list) == count_of_name:
        return extracted_list
    return [''] * count_of_name

def filterHouseNo(number):
    # print(number)
    # try:
    #     number = number[:number.find("/")]
    #     print(number)
    # except:
    #     return number
    return number

def getHouseNumber(house_number_list, count_of_name):
    # #print('In getHouseNumber')
    extracted_list = []
    i = 0
    while i < len(house_number_list):
        if house_number_list[i] in HOUSE_NAME_VARIABLE:
            # #print('lalal')
            # traverse till you get age
            while i < len(house_number_list) and house_number_list[i] not in NUMBER_VARIABLE:
                i += 1
            extracted_list.append(house_number_list[i + 1])
        else:
            i += 1
    # #print(extracted_list)
    if len(extracted_list) == count_of_name:
        return extracted_list
    return [''] * count_of_name


def isGuardian(string):
    if string.isupper():
        return True
    return False

def clean(input):
    cleaned = []
    for word in input:
        if word not in WASTE_WORDS:
            cleaned.append(word)

    return cleaned

def getSingleHouseNumber(house_number_list):

    house_number = ""
    print("recieved",house_number_list)
    flag = False
    i = 0
    while i<len(house_number_list)-1:
        if house_number_list[i] in HOUSE_NAME_VARIABLE:
            flag = True
        if flag and house_number_list[i] in NUMBER_VARIABLE:
            house_number = house_number_list[i+1]
            break
        i+=1
    print(house_number)
    return house_number

def getHouseNumber_ERROR(house_number_list, count_of_name):
    # print('In getHouseNumber')
    error_position = -1
    extracted_list = []
    i = 0
    while i < len(house_number_list):
        if isGuardian(house_number_list[i]):
            # print('Guardian FOund')
            error_position = len(extracted_list)
            extracted_list.append('')
            i += 1
        elif house_number_list[i] in HOUSE_NAME_VARIABLE:
            # #print('lalal')
            # traverse till you get age
            # print("KHBBN")
            while house_number_list[i] not in NUMBER_VARIABLE:
                i += 1
            extracted_list.append(house_number_list[i + 1])
        else:
            i += 1
    # print(extracted_list)
    return extracted_list, error_position


def getGender(age_gender_list, count_of_name):
    extracted_list = []
    i = 0
    while i < len(age_gender_list):
        if age_gender_list[i] in GENDER_VARIABLE:
            extracted_list.append(age_gender_list[i + 1])

        i += 1
    # #print(extracted_list)
    if len(extracted_list) == count_of_name:
        return extracted_list
    return [''] * count_of_name


def getAge(age_gender_list, count_of_name):
    extracted_list = []
    i = 0
    while i < len(age_gender_list):
        if age_gender_list[i] in AGE_VARIABLE:
            extracted_list.append(age_gender_list[i + 1])
        i += 1
    # print("extracted -->",extracted_list)
    if len(extracted_list) == count_of_name:
        return extracted_list
    return [''] * count_of_name


def getAgeCount(age_list):
    count = 0
    for i in age_list:
        if i in AGE_VARIABLE:
            count += 1
    return count

def getFirstPage(page1):
    VARIABLE_NO = ('No.', 'No', 'no.', 'no')
    FIRST_TWO_LINES_DICT = {'No. Name and Reservation Status of Assembly Constituency':'',
                            'Part number':'',
                            'No. Name and Reservation Status of Parliamentary Constituency(ies) in which the Assembly Constituency is located':''}
    
    page = page1
    try:
        all_data = page.extract_text()
        list_data = all_data.split('\n')
        a = [i.split() for i in list_data]
        INDEX_OF_NO = []
        STARTING_TWO_LINES = []

        for i in range(len(a)):
            #print(a[i])
            if a[i][0] in VARIABLE_NO:
                if len(INDEX_OF_NO) == 0:
                    INDEX_OF_NO.append(i)
                    STARTING_TWO_LINES.append(a[i:i + 3])
                elif len(INDEX_OF_NO) == 1:
                    INDEX_OF_NO.append(i)
                    STARTING_TWO_LINES.append(a[i:i + 2])
        firstLine = STARTING_TWO_LINES[0]
        secondLine = STARTING_TWO_LINES[1]
        res = ''
        if 'Constituency:' in firstLine[0]:
            idx = firstLine[0].index('Constituency:')
            part_idx = firstLine[0].index('Part')
            res = ' '.join(firstLine[0][idx+1:part_idx]) + ' '+ ' '.join(firstLine[2][:])
        elif ':' in firstLine[0]:
            idx = firstLine[0].index(':')
            part_idx = firstLine[0].index('Part')
            res = ' '.join(firstLine[0][idx + 1:part_idx]) +' ' +' '.join(firstLine[2][:])
        elif 'Constituency' in firstLine[0]:
            idx = firstLine[0].index('Constituency')
            part_idx = firstLine[0].index('Part')
            res = ' '.join(firstLine[0][idx + 1:part_idx]) +' ' +' '.join(firstLine[2][:])
        #print('--->',firstLine[2])
        #print(res)
        part2 = ' '.join(firstLine[2][:-1])
        #print('--->',part2)
        res = res.replace(':','')

        FIRST_TWO_LINES_DICT['No. Name and Reservation Status of Assembly Constituency'] = res
        FIRST_TWO_LINES_DICT['Part number'] = firstLine[1][0].replace('g','9')
        res = ''
        if 'located:' in secondLine[-1]:
            idx = secondLine[-1].index('located:')
            res = ' '.join(secondLine[-1][idx+1:])
        elif ':' in secondLine[-1]:
            idx = secondLine[-1].index(':')
            res = ' '.join(secondLine[-1][idx + 1:])
        elif 'located' in secondLine[-1]:
            idx = secondLine[-1].index('located')
            res = ' '.join(secondLine[-1][idx + 1:])
        res = res.replace(':','')
        FIRST_TWO_LINES_DICT['No. Name and Reservation Status of Parliamentary Constituency(ies) in which the Assembly Constituency is located'] = res
    except:
        print("First two lines error")
    # print(res)
    # print(STARTING_TWO_LINES)
    # print(FIRST_TWO_LINES_DICT)
    return FIRST_TWO_LINES_DICT


def getRestDetails(page1):
    def isPresent(line_list,variable):
        #print("line = ",line_list)
        #print("vari = ",variable)
        for word in line_list:
            for w in variable:
                if word == w:
                    return True
        return False
        
    def getData(row_data,start):
        try:
            answer_string = " ".join(row_data)
            answer_string = answer_string[answer_string.find(start)+len(start):]
            answer_string = answer_string.replace(":","")
            answer_string = answer_string.strip()
            return answer_string
        except:
            return ""
    village_string = ''
    post_string = ''
    block_string = ''
    panchayat_string = ''
    police_string = ''
    sub_string = ''
    district_string = ''
    pin_string = ''
    VILLAGE = ('Main','main','Village:','village:','Village')
    POST = ('Post','post')
    PANCHAYAT = ('Panchayat',"Panchayat:")
    BLOCK = ('Block',"Block:")
    POLICE = ("Police",)
    SUB = ("Sub",)
    DISTRICT = ("District","District:")
    PIN = ("Pin",)

    REST_DETAILS_DICT = {'Main':['Main Town or Village',None],
                         'Post':['Post Office',None],
                         'Panchayat':['Panchayat',None],
                         'Block':['Block',None],
                         'Police':['Police Station',None],
                         'Sub':['Sub Division',None],
                         'District':['District',None],
                         'Pin':['Pin Code',None]}
    try:
        page = page1
        all_data = page.extract_text()
        list_data = all_data.split('\n')
        # #print(len(list_data))
        # #print(list_data)
        a = [i.split() for i in list_data]
        # #print(a)
        #print(a)
        for i in range(len(a)):
            if len(a[i]) == 0:
                continue
            if isPresent(a[i],VILLAGE):
                start = "llage"
                #print("dd ",a[i])
                village_string = getData(a[i],start)
                #print("village --> ",village_string)
            elif isPresent(a[i],BLOCK):
                start = "ock"
                # print("dd ",a[i])
                block_string = getData(a[i],start)
                #print("post --> ",block_string)
            elif isPresent(a[i],POST):
                start = "ffice"
                #print("dd ",a[i])
                post_string = getData(a[i],start)
                #print("post --> ",post_string)
                
            elif isPresent(a[i],PANCHAYAT):
                start = "chayat"
                #print("dd ",a[i])
                panchayat_string = getData(a[i],start)
                #print("panchayat --> ",panchayat_string)
                
            elif isPresent(a[i],POLICE):
                start = "tation"
                print("dd ",a[i])
                police_string = getData(a[i],start)
                #print("police --> ",police_string)
                
            elif isPresent(a[i],SUB):
                start = "vision"
                #print("dd ",a[i])
                sub_string = getData(a[i],start)
                #print("Sub --> ",sub_string)
                
            elif isPresent(a[i],DISTRICT) :
                start = "strict"
                #print("dd ",a[i])
                district_string = getData(a[i],start)
                #print("District --> ",district_string)
                
            elif isPresent(a[i],PIN):
                start = "ode"
                #print("dd ",a[i])
                pin_string = getData(a[i],start)
                #print("Pin --> ",pin_string)
                
        REST_DETAILS_DICT['Main'][1] = village_string
        REST_DETAILS_DICT['Post'][1] = post_string
        REST_DETAILS_DICT['Block'][1] = block_string
        REST_DETAILS_DICT['Panchayat'][1] = panchayat_string
        REST_DETAILS_DICT['Police'][1] = police_string
        REST_DETAILS_DICT['Sub'][1] = sub_string
        REST_DETAILS_DICT['District'][1] = district_string
        REST_DETAILS_DICT['Pin'][1] = pin_string
    except Exception as p:
        #print(p)
        print("rest details error")
    
    return REST_DETAILS_DICT

def main(pdf_file,destination):

    stored_data = {
        "Epic Numbers": [],
        "Name": [],
        "Guardian": [],
        "House No": [],
        "Age": [],
        "Gender": [],
        "section_data": [],
        "assembly_data": [],
        "part_number":[]
    }

    FIRST_TWO_LINES_DICT = {}
    REST_DETAILS_DICT = {}
    is_section_data = False
    is_addition_data = False

    with pdfplumber.open(pdf_file) as pdf:
    
        p = len(pdf.pages)
        # print(pdf.pages)
        try:
            for i in range(0, 1):
                REST_DETAILS_DICT = getRestDetails(pdf.pages[i])
                FIRST_TWO_LINES_DICT = getFirstPage(pdf.pages[i])
            #print("first page",FIRST_TWO_LINES_DICT)
            #print("rest det",REST_DETAILS_DICT)
            # exit()
        except Exception as p:
            print(p)
            print("First Page Error")
            # exit()
        assembly_data = ""
        prev_number = ""
        for i in range(2, p):

            page = pdf.pages[i]
            # print(page)
            all_data = page.extract_text()
            # print(all_data)
            list_data = all_data.split('\n')
            
            a = [i.split() for i in list_data]

            list_data = []
            for c in a:
                if c:
                    list_data.append(c)
            j = 0
            # print(list_data)

            while j < len(list_data):

                # if j<=2:
                #print(list_data[j])
                '''Assembly'''
                
                try:
                    if list_data[j].count('Assembly') >= 1:
                        assembly_raw_data = list_data[j]
                        assembly_data = cleanLine(assembly_raw_data)
                        assembly_data = " ".join(assembly_raw_data)
                        start = 'Name'
                        end = 'Part'
                        assembly_data = assembly_data[assembly_data.find(start)+len(start):assembly_data.rfind(end)]
                        assembly_data = assembly_data.replace(":","")
                        assembly_data = assembly_data.replace(" ","")
                        assembly_data = assembly_data.replace(".","")
                        
                        # print(assembly_data)
                        

                    '''Section Number'''
                    if list_data[j].count('Section') >= 1:
                        section_raw_data = cleanLine(list_data[j])
                        section_raw_data = " ".join(section_raw_data)
                        #print(section_raw_data)
                        start = "Name"
                        section_raw_data = section_raw_data[section_raw_data.find(start)+len(start):]
                        section_raw_data = section_raw_data.replace(":","")
                        section_raw_data = section_raw_data.replace(" ","")
                        section_raw_data = section_raw_data.replace(".","")
                        section_data = section_raw_data
                        #print(section_data)
                        
                        try:
                            number = int(section_data[:section_data.find('-')])
                            #print("a",number)
                            prev_assembly = stored_data['section_data'][-1]
                            
                            
                            #print("b")
                            if number != prev_number and number!= prev_number+1 and number>9:
                                if int(str(number)[1]) == prev_number:
                                    number = prev_number
                                elif int(str(number)[1]) == prev_number+1:
                                    number = prev_number+1
                            prev_number = number
                            section_data = str(number)+section_data[section_data.find('-'):]

                        except Exception as p:
                            number = int(section_data[:section_data.find('-')])
                            prev_number = number
                            #print(p)
                            #print("assembly possible error ")
                        is_section_data = True

                    '''List of additions'''
                    if list_data[j].count('Additions') >= 1 or list_data[j].count('additions') >= 1 or list_data[j].count(
                            'Addition') >= 1:
                        addition_raw_data = cleanLine(list_data[j])
                        addition_data = ' '.join(addition_raw_data)
                        is_addition_data = True
                        # #print(addition_data)
                except:
                    print("Possible Error b- (can be ignored)")

                '''Completed Headers'''
                not_possible = False
                x = list_data[j]
                # print(x)
                if x:

                    if x[0] == 'Name' or x[0] == 'Name:':
                        try:
                            # print('-------------------------------------------------')
                            '''Name extraction'''
                            Name_list = []
                            count_of_name = 0
                            for k in range(len(x)):
                                if x[k] == 'Name:':
                                    s = x[k + 1]
                                    if k + 2 < len(x) and (x[k + 2] != 'Name' and x[k + 2] != 'Name:'):
                                        s += ' ' + x[k + 2]
                                    Name_list.append(s)

                                    count_of_name += 1
                                elif x[k] == 'Name':
                                    s = x[k + 2]
                                    if k + 3 < len(x) and (x[k + 3] != 'Name' and x[k + 3] != 'Name:'):
                                        s += ' ' + x[k + 3]
                                    Name_list.append(s)
                                    count_of_name += 1
                            name_extracted_list = Name_list
                            count_of_name = len(name_extracted_list)

                            #print("---->", x)
                            #print(Name_list)
                            # print('count : ',count_of_name )
                            '''IPEC numbers extraction'''
                            epic_numbers = list_data[j - 1]
                            #print("epic ",epic_numbers)
                            try:
                                epic_number_extracted_list = getEpicNumbers(epic_numbers, count_of_name)
                                if epic_number_extracted_list.__len__() != count_of_name:
                                    epic_number_extracted_list = [''] * count_of_name
                            except:
                                epic_number_extracted_list = [''] * count_of_name
                            #print("epic after ",epic_number_extracted_list)
                            ####
                            '''Guardian Name extraction'''
                            # print(list_data[j+1])
                            try:
                                guardian_list = list_data[j + 1]
                                guardian_list = cleanLine(guardian_list)
                                guardian_list.remove
                                guardian_extracted_list = getGuardianData(guardian_list, count_of_name)
                            except:
                                guardian_extracted_list = [''] * count_of_name
                            
                            '''House Number extraction'''
                            third_line = clean(list_data[j+2])
                            fourth_line = clean(list_data[j+3])
                            fifth_line = clean(list_data[j+4])
                            print(third_line)
                            print(fourth_line)
                            print(fifth_line)
                            firstHouse  = ""
                            secondHouse = ""
                            thirdHouse = ""
                            if len(third_line)>=3:
                                firstHouse = getSingleHouseNumber(third_line[:3])
                            if firstHouse =="" and len(fourth_line)>=3:
                                firstHouse = getSingleHouseNumber(fourth_line[:3])
                            if firstHouse =="" and len(fifth_line)>=3:
                                firstHouse = getSingleHouseNumber(fifth_line[:3])

                            if count_of_name >=2:
                                if len(third_line)>=5:
                                    secondHouse = getSingleHouseNumber(third_line[1:len(third_line)-1])
                                if secondHouse =="" and len(fourth_line)>=6:
                                    secondHouse = getSingleHouseNumber(fourth_line[1:len(fourth_line)-1])
                                if secondHouse =="" and len(fifth_line)>=6:
                                    secondHouse = getSingleHouseNumber(fifth_line[1:len(fifth_line)-1])

                            if count_of_name ==3:
                                if len(third_line)>=5:
                                    thirdHouse = getSingleHouseNumber(third_line[len(third_line)-3:])
                                if thirdHouse =="" and len(fourth_line)>=5:
                                    thirdHouse = getSingleHouseNumber(fourth_line[len(fourth_line)-3:])
                                if thirdHouse =="" and len(fifth_line)>=5:
                                    thirdHouse = getSingleHouseNumber(fifth_line[len(fifth_line)-3:])
                            print(firstHouse,secondHouse,thirdHouse)
                            if count_of_name == 1:
                                house_number_extracted_list = [firstHouse]
                            elif count_of_name == 2:
                                house_number_extracted_list = [firstHouse,secondHouse]
                            elif count_of_name == 3:
                                house_number_extracted_list = [firstHouse,secondHouse,thirdHouse]
                            # print('count : H',count_of_name )
                            # print(list_data[j+2])
                            # try:
                            #     house_number_list = list_data[j + 2]
                            #     house_number_list = cleanLine(house_number_list)

                            #     is_guardian_normal = True
                            #     if house_number_list.count('House') < count_of_name:
                            #         is_guardian_normal = False
                            #         house_number_extracted_list, error_position = getHouseNumber_ERROR(house_number_list,
                            #                                                                         count_of_name)
                            #     # Normal name
                            #     else:
                            #         house_number_extracted_list = getHouseNumber(house_number_list, count_of_name)
                            #     # print("H answer",house_number_list,house_number_extracted_list)
                            #     if len(house_number_extracted_list) != count_of_name:
                            #         house_number_extracted_list = [''] * count_of_name
                            # except:
                            #     house_number_extracted_list = [''] * count_of_name
                            #     # print(house_number_list,house_number_extracted_list)
                            '''Age, Gender extraction'''
                            try:
                                # print(list_data[j+3])
                                age_gender_list = list_data[j + 3]
                                age_gender_list = cleanLine(age_gender_list)
                                # Gender Extraction
                                if age_gender_list.count('Gender:') == count_of_name:
                                    gender_extracted_list = getGender(age_gender_list, count_of_name)
                                else:
                                    gender_extracted_list = [''] * count_of_name
                            except:
                                gender_extracted_list = [''] * count_of_name
                            # Age Extraction
                            try:
                                if getAgeCount(age_gender_list) == count_of_name:
                                    # print("**********************")
                                    age_extracted_list = getAge(age_gender_list, count_of_name)
                                else:
                                    age_extracted_list = [''] * count_of_name
                            except:
                                age_extracted_list = [''] * count_of_name
                            # print(list_data[j+4])
                            j += 2

                            '''Combining stage'''

                            section_data_list = [''] * count_of_name
                            try:
                                if is_section_data:
                                    section_data_list = [section_data]
                                    section_data_list.extend([''] * (count_of_name - 1))
                                    print(section_data_list)
                            except:
                                section_data_list = [''] * count_of_name

                            addition_data_list = [''] * count_of_name
                            try:
                                if is_addition_data:
                                    addition_data_list = [addition_data]
                                    addition_data_list.extend([''] * (count_of_name - 1))
                            except:
                                addition_data_list = [''] * count_of_name

                            if is_addition_data:
                                is_addition_data = False
                                stored_data['section_data'].extend(addition_data_list)
                            else:
                                is_section_data = False
                                stored_data['section_data'].extend(section_data_list)
                                
                            '''Assembly Data'''
                            assembly_data_list = [''] * count_of_name
                            try:
                                if assembly_data.__len__()>1:
                                    assembly_data_list = [assembly_data]
                                    assembly_data_list.extend([''] * (count_of_name - 1))
                                    # print(assembly_data_list)
                            except:
                                assembly_data_list = [''] * count_of_name
                            # print(len(name_extracted_list),len(house_number_extracted_list))
                            '''DELETED ENTRY CODE'''
                            # if count_of_name == 0:
                            #     epic_number_extracted_list = ['deleted_row_entry']*3
                            #     name_extracted_list = ['deleted_row_entry']*3
                            #     house_number_extracted_list = ['deleted_row_entry']*3
                            #     guardian_extracted_list= ['deleted_row_entry']*3
                            #     age_extracted_list = ['deleted_row_entry']*3
                            #     gender_extracted_list = ['deleted_row_entry']*3
                            #     stored_data['section_data'].extend(gender_extracted_list)

                            stored_data['Epic Numbers'].extend(epic_number_extracted_list)
                            stored_data['Name'].extend(name_extracted_list)
                            stored_data['House No'].extend(house_number_extracted_list)
                            stored_data["Guardian"].extend(guardian_extracted_list)
                            stored_data['Age'].extend(age_extracted_list)
                            stored_data['Gender'].extend(gender_extracted_list)
                            stored_data['assembly_data'].extend(assembly_data_list)
                        # break
                        except:
                            stored_data['Epic Numbers'].append('')
                            stored_data['Name'].append('')
                            stored_data['House No'].append('')
                            stored_data["Guardian"].append('')
                            stored_data['Age'].append('')
                            stored_data['Gender'].append('')
                            stored_data['section_data'].append('')
                            stored_data['assembly_data'].append('')
                j += 1

   
    # #print("***************************************")
    # #print(stored_data["Epic Numbers"])
    # print(stored_data["Name"])
    # #print(stored_data["Age"])
    # #print(stored_data["Guardian"])
    # #print(stored_data["Gender"])
    # #print(stored_data["House No"])
    # #print("Epic = ",stored_data["Epic Numbers"].__len__())
    # #print("House = ",stored_data["House No"].__len__())
    try:
        x = stored_data["Epic Numbers"]
        # #print(x)

        for i in range(len(x)):
            y = x[i]
            if '.' in y:
                y = y.replace('.', '')
                x[i] = y
            elif ',' in y:
                y = y.replace(',', '')
                x[i] = y
        # #print(x)

        for i in range(len(x)):
            y = x[i]
            if '2' in y[:3] and ('Z' in y[:3] or 'z' in y[:3]):
                y2 = y[3:]
                y1 = y[:3].replace('2', '')
                x[i] = y1 + y2
            elif '2' in y[:3] and 'Z' not in y[:3] and 'z' not in y[:3]:
                y2 = y[3:]
                y1 = y[:3].replace('2', 'Z')
                x[i] = y1 + y2

        for i in range(len(x)):
            y = x[i]
            if 'QO' in y and len(y) > 10:
                y = y.replace('QO', 'Q')
                x[i] = y
            elif 'BO' in y and len(y) > 10:
                y = y.replace('BO', 'B')
                x[i] = y
        wrong_index = []
        for i in range(len(x)):
            if len(x[i]) != 10 and len(x[i]) != 0:
                wrong_index.append(i)

        len_x = [len(i) for i in x]
        # #print(len_x)
        stored_data["Epic Numbers"] = x
    except:
        print('Possible Error c (can ignore) ')
    # #print(wrong_index)
    # #print(len(wrong_index))
    print("Epic = ", stored_data["Epic Numbers"].__len__())
    print("House = ", stored_data["House No"].__len__())
    print("Age = ", stored_data["Age"].__len__())
    print("Guardian = ", stored_data["Guardian"].__len__())
    print("Gender = ", stored_data["Gender"].__len__())
    print("Name = ", stored_data["Name"].__len__())
    print("Section Data = ", stored_data['section_data'].__len__())
    print("Assembly Data = ", stored_data['assembly_data'].__len__())

    i = 1
    while i<stored_data['section_data'].__len__():
        if stored_data['section_data'][i] =='':
            stored_data['section_data'][i] = stored_data['section_data'][i-1]
        i+=1

    i = 1
    while i<stored_data['assembly_data'].__len__():
        if stored_data['assembly_data'][i] =='':
            stored_data['assembly_data'][i] = stored_data['assembly_data'][i-1]
        i+=1
    # save_data()
    # stored_data['Epic Numbers'].append(stored_data['Epic Numbers'].count(''))
    # stored_data['Name'].append(stored_data['Name'].count(''))
    # stored_data['House No'].append(stored_data['House No'].count(''))
    # stored_data["Guardian"].append(stored_data["Guardian"].count(''))
    # stored_data['Gender'].append(stored_data['Gender'].count(''))
    # stored_data['Age'].append(stored_data['Age'].count(''))
    # stored_data['section_data'].append(stored_data['section_data'].count(''))
    SIZE = stored_data['Epic Numbers'].__len__()
    FIRST_TWO_LINES_DICT['Part number'] = FIRST_TWO_LINES_DICT['Part number'].replace("g","9")
    FIRST_TWO_LINES_DICT['Part number'] = FIRST_TWO_LINES_DICT['Part number'].replace("I","1")
    temp_data = {
        "Epic_Number": stored_data['Epic Numbers'],
        "Name": stored_data['Name'],
        "House_Number": stored_data['House No'],
        "Guardian": stored_data["Guardian"],
        "Gender": stored_data['Gender'],
        "Age": stored_data['Age'],
        "Assembly Constituency No and Name":stored_data['assembly_data'],
        "Section No. and Name": stored_data['section_data'],
        "No. Name and Reservation Status of Assembly Constituency":SIZE*[FIRST_TWO_LINES_DICT["No. Name and Reservation Status of Assembly Constituency"]],
        "Part number":SIZE*[FIRST_TWO_LINES_DICT['Part number']],
        "No. Name and Reservation Status of Parliamentary Constituency(ies) in which the Assembly Constituency is located":SIZE*[FIRST_TWO_LINES_DICT["No. Name and Reservation Status of Parliamentary Constituency(ies) in which the Assembly Constituency is located"]],
        'Main Town or Village ':SIZE*[REST_DETAILS_DICT['Main'][1]],
        "Post Office":SIZE*[REST_DETAILS_DICT['Post'][1]],
        "Panchayat":SIZE*[REST_DETAILS_DICT['Panchayat'][1]],
        "Block":SIZE*[REST_DETAILS_DICT['Block'][1]],
        "Police Station":SIZE*[REST_DETAILS_DICT['Police'][1]],
        "Sub Division":SIZE*[REST_DETAILS_DICT['Sub'][1]],
        "District":SIZE*[REST_DETAILS_DICT['District'][1]],
        "Pincode":SIZE*[REST_DETAILS_DICT['Pin'][1]],
    }

 
    # convert pdf name to csv name
    
    # dictionary of lists
    df = pd.DataFrame(temp_data)

    # saving the dataframe
    df.to_csv(destination[:destination.find('.pdf')] + '.csv')


'''CALL MAIN FUNCTION AND CHANGE pdf_file as required'''
if __name__ == '__main__':
    # pdf_file = 'folder/A0090001.pdf'
    
    base = "test/"
    for file in os.listdir(base):
        pdf_file = base+file
        pdf_name = pdf_file[pdf_file.rfind('/')+1:]
        pdf = pikepdf.open(pdf_file)
        new_file = pdf_file[:pdf_file.rfind('/')+1]+"con-"+pdf_name
        pdf.save(new_file)
        main(new_file,pdf_file)
