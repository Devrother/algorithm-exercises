def get_issuer(number):
    strnum = str(number)
    if (strnum[0:2] == '34') or (strnum[0:2] == '37') and len(strnum) == 15:
        return "AMEX"
    elif (strnum[0:4] == '6011') and len(strnum) == 16:
        return "Discover"
    elif (strnum[0:2] == '51') or (strnum[0:2] == '52') or (strnum[0:2] == '53') or (strnum[0:2] == '54') or (strnum[0:2] == '55') and len(strnum) == 16:
        return "Mastercard"
    elif (strnum[0:1] == '4') and ((len(strnum) == 13) or (len(strnum) == 16)):
        return "VISA"
    else:
        return "Unknown"
