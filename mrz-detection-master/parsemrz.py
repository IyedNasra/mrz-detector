def parse(cleaned_list: list):
    if len(cleaned_list) != 2 or cleaned_list[0][0] != "P":
        return "Only input passport images/Image not clear";
    #tolerating OCR mistakes
    for i in range(len(cleaned_list)):
        while len(cleaned_list[i]) < 44:
            cleaned_list[i] = cleaned_list[i][:-2] + "<" + cleaned_list[i][-2:]
    # Extracting the first letter of the first element
    Passport_type = cleaned_list[0][0]  # Accessing the second character
    if cleaned_list[0][1] == '<':
        Passport_subtype = None
    else:
        # Extracting the second letter of the first element
        Passport_subtype = cleaned_list[0][1]  # Accessing the second character
    Issuing_country = cleaned_list[0][2:5]
    remains = cleaned_list[0][5:] #Comntains name and surname for further processing
    Surname = remains.split('<<', 1)[0].replace('<', ' ')
    Name = remains.split('<<', 1)[1].strip('<').replace('<', ' ')
    Passport_number = cleaned_list[1][0:9]
    Check_digit1 = cleaned_list[1][9]
    Nationality = cleaned_list[1][10:13]
    Birth_Date = cleaned_list[1][13:19]
    Check_digit2 = cleaned_list[1][19]
    if cleaned_list[1][20] == '<':
        Gender = 'unspecified'
    else:
        Gender = cleaned_list[1][20]
    Expiration_date = cleaned_list[1][21:27]
    Check_digit3 = cleaned_list[1][27]
    if len(cleaned_list[0]) == 44:
        Personal_number = cleaned_list[1][28:42].strip('<')
        Check_digit4 = cleaned_list[1][42]
        Check_digit5 = cleaned_list[1][43]
    elif len(cleaned_list[0]) == 36:
        Personal_number = cleaned_list[1][28:35].strip('<')
        Check_digit4 = cleaned_list[1][35]
    details = [Name, Surname, Passport_type, Passport_subtype, Issuing_country, Passport_number, Nationality, Birth_Date, Gender, Expiration_date, Personal_number, Check_digit1, Check_digit2, Check_digit3, Check_digit4, Check_digit5]
    new_details = []
    for element in details:
        if element == Passport_subtype:
            continue
        if element.endswith("<"):
            element = element.strip("<")
        new_details.append(element)
    details = new_details
    return details
