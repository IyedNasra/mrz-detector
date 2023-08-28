def parse(mrz: list):
    if len(mrz) != 2 or mrz[0][0] != "P":
        return "Only input passport images/Image not clear";
    #tolerating OCR mistakes
    for i in range(len(mrz)):
        while len(mrz[i]) < 44:
            mrz[i] = mrz[i][:-2] + "<" + mrz[i][-2:]
    # Extracting the first letter of the first element
    Passport_type = mrz[0][0]  # Accessing the second character
    if mrz[0][1] == '<':
        Passport_subtype = None
    else:
        # Extracting the second letter of the first element
        Passport_subtype = mrz[0][1]  # Accessing the second character
    Issuing_country = mrz[0][2:5]
    remains = mrz[0][5:] #Comntains name and surname for further processing
    Surname = remains.split('<<', 1)[0].replace('<', ' ')
    Name = remains.split('<<', 1)[1].strip('<').replace('<', ' ')
    Passport_number = mrz[1][0:9]
    Check_digit1 = mrz[1][9]
    Nationality = mrz[1][10:13]
    Birth_Date = mrz[1][13:19]
    Check_digit2 = mrz[1][19]
    if mrz[1][20] == '<':
        Gender = 'unspecified'
    else:
        Gender = mrz[1][20]
    Expiration_date = mrz[1][21:27]
    Check_digit3 = mrz[1][27]
    if len(mrz[0]) == 44:
        Personal_number = mrz[1][28:42].strip('<')
        Check_digit4 = mrz[1][42]
        Check_digit5 = mrz[1][43]
    elif len(mrz[0]) == 36:
        Personal_number = mrz[1][28:35].strip('<')
        Check_digit4 = mrz[1][35]
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
