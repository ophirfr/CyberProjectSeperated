import json
import sys
from werkzeug.security import generate_password_hash


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#input - הסיסמא של המנהל
#output - מחזירה סיסמא מוצפנת וכותבת את הסיסמא המוצפנת לקובץ הגדרות
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def UpdatePass(password):
    # Opening JSON file
    try:
        with open('../setting_server/Setting.json', 'r') as openfile:
            json_object = json.load(openfile)
    except FileNotFoundError:
        print('can not find the file')
        return
    json_object["password"] = generate_password_hash(password, method='sha256')
    try:
        with open('../setting_server/Setting.json', 'w') as openfile:
            json.dump(json_object, openfile)
    except FileNotFoundError:
        print('can not find the file')




def main():
# לוקח את הארגומנטים מה Cmd כאשר הארגומנט הראשון הוא שם הקובץ והארגומנט השני הוא הסיסמא
    if( len(sys.argv)<2):
        print("You must enter a password")
        return
    UpdatePass(sys.argv[1])

if __name__ == '__main__':
    main()