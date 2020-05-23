from flask import Flask, request
import requests
import json
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World... We're live!"

#Start of Yoruba ROUTE

@app.route('/yoruba', methods=['POST'])
def yoruba ():
    return "Yoruba"

#End of Yoruba ROUTE

@app.route('/sms', methods=['POST'])
def sms_reply ():
    incoming_msg = request.values.get('Body', '').upper()
    #print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    
    #GREETINGS FUNCTION

    egreet = ['Hi', 'Hey', 'Heya', 'Menu', 'Into', 'Hello']
    ygreet = ['Bawo', 'Bawoni', 'Booni', 'Ekaro', 'Ekaaro', 'Ekasan', 'Ekaasan', 'Ekale', 'Ekaale']

    if incoming_msg in egreet:
        #text = "Hello 🙋🏽‍♂, \nThis is a COVID-19-Nigeria-Bot developed by Jeremiah Jacob, to provide latest information updates \n\n Use below keys to select your prefered language. \n\n E to continue with English \n\n Y layi yan ede Yoruba \n\n H don zaɓar harshen hausa \n\n I iji họrọ asusu igbo"
        text = "Welcome to Naija Mental Health Bot by CONVAS.ng, to provide latest information updates \n\n Use below keys to select your prefered language. \n\n E to continue with English \n\n Y layi yan ede Yoruba \n\n H don zaɓar harshen hausa \n\n I iji họrọ asusu igbo"
        msg.body(text)
        responded = True

    if incoming_msg in ygreet:
        #text = 'Hello 🙋🏽‍♂, \nThis is a COVID-19-Nigeria-Bot developed by Jeremiah Jacob, to provide latest information updates i.e cases in different part the country and create awareness to help you and your family stay safe.\n For any emergency 👇 \n 📞 Helpline: 080097000010 | Toll-Free Number: 112 \n ✉ Email: info@ncdc.gov.ng \n\n Please enter one of the following option 👇 \n
        #  *A*. COVID-19 statistics in *Nigeria*. \n *B*. COVID-19 cases in *Affected States*. \n *C*. COVID-19 cases in *North Central*. \n *D*. COVID-19 cases in *North East*. \n *E*. COVID-19 cases in *North West*. \n *F*. COVID-19 cases in *South East*. \n *G*. COVID-19 cases in *South South*. \n *H*. COVID-19 cases in *South West*. \n *I*. How does it *Spread*? \n *J*. *Preventive measures* to be taken.'
        text = "Kaabo 🙋🏽‍♂, \n Eyi jẹ COVID-19-Nigeria-Bot nipasẹ Jeremiah Jacob, lati pese awọn imudojuiwọn alaye tuntun \n\n Lo awọn bọtini isalẹ lati yan ede ti o fẹ. \ n\n E lati tẹsiwaju pẹlu ede Gẹẹsi \ n\n Y lati yan ede Yoruba \n\n H lati yan ede Hausa \n\n I lati yan ede Igbo"
        msg.body(text)
        responded = True

    #END GREETING FUNCTIONS

    if incoming_msg == 'E':
            text = "You're still using english language \n *E1*. COVID-19 statistics in *Nigeria*. \n *E2*. COVID-19 cases in *Affected States*. \n *E3*. COVID-19 cases in *North Central*. \n *E4*. COVID-19 cases in *North East*. \n *E5*. COVID-19 cases in *North West*. \n *E6*. COVID-19 cases in *South East*. \n *E7*. COVID-19 cases in *South South*. \n *E8*. COVID-19 cases in *South West*. \n *E9*. How does it *Spread*? \n *E10*. *Preventive measures* to be taken. \n\n 0 to select another language"
            msg.body(text)
            responded = True

    if incoming_msg == 'Y':
        text = "Ekaabo si ede yoruba \n Y1 fun Gbogbo Orile Ede *Nigeria* \n Y2 fun Awọn iṣẹlẹ COVID-19 ni *Awọn ipinlẹ ti o ti ṣẹlẹ* \n Y3 fun *Ariwa Aarin* \n Y4 fun *Ariwa-oorun* \n Y5 fun *Ariwa iwọ-oorun* \n Y6 fun *Guusu ila oorun* \n Y6 fun *Guusu Guusu* \n Y8 fun *Iwọ oorun guusu* \n\n 0 lati yan ede miran"
        msg.body(text)
        responded = True

    if incoming_msg == 'H':
        text = " *H1*. Kididdigar COVID-19 a *Najeriya*. \n *H2*. COVID-19 lokuta a cikin *Jihohin da cutar ta shafa*. \n *H3*. COVID-19 lokuta a *Arewa ta Tsakiya*. \n *H4*. COVID-19 lokuta a *Arewa maso Gabas*. \n *H5*. COVID-19 lokuta a cikin *Arewa maso Yamma*. \n *H6*. COVID-19 lokuta a *Kudu maso Gabas*. \n *H7*. COVID-19 lokuta a cikin *Kudancin Kudu*. \n *H8*. COVID-19 lokuta a cikin *Kudu maso Yamma*. \n *H9*. Ta yaya *Rarrabawa*? \ n *H10*. *Matakan hanyoyin kariya* da za'ayi. \n\n 0 don zaɓar wani yare"
        msg.body(text)
        #msg.media("https://covid19project.org.ng/whatsapp/twilio/audio/welcome_hausa.ogg")
        responded = True

    if incoming_msg == 'I':
        #text = "Ekaabo si yoruba \n Y1 fun Gbogbo Orile Ede *Nigeria* \n Y2 fun Awọn iṣẹlẹ COVID-19 ni *Awọn ipinlẹ ti o ti ṣẹlẹ* \n Y3 fun *Ariwa Aarin* \n Y4 fun *Ariwa-oorun* \n\n Y5 fun *Ariwa iwọ-oorun* \n Y6 fun *Guusu ila oorun* \n Y6 fun *Guusu Guusu* \n\n Y8 fun *Iwọ oorun guusu*"
        msg.body(text)
        responded = True        

    #STARTING ENGLISH FUNCTION#

    if incoming_msg == 'E1':
        # return total cases
        r = requests.get('https://covid19project.org.ng/api/endpoints/stats?action=totalcases')
        if r.status_code == 200:
            data = r.json()
            text = f'_COVID-19 Nigeria Cases Statistics_ \n\nConfirmed Cases : *{data["confirmed"]}*\n\nDischarged : *{data["recovered"]}* \n\nActive Cases : *{data["active_cases"]}*\n\n Deaths : *{data["death"]}*'
            msg.body(text)
            responded = True
        else:
            text = 'I could not retrieve the results at this time, sorry.'
            msg.body(text)
            responded = True

    if  incoming_msg == 'E2':
        # return cases in Affected States
        r = requests.get('https://covid19project.org.ng/api/endpoints/affected_states')
        if r.status_code == 200:
            data = r.json()
            for each in data['Covid19NG']:
                text = ".\n\n"+each['name']+" : Cases ("+each['cases']+ ")"+" : Discharged ("+each['recovered']+")"+" : Deaths ("+each['death']+ ")"
                print(text)
                msg.body(text)
        else:
            text = 'I could not retrieve the results at this time, sorry.'
            print(text)
        #msg.body(text)
        responded = True

    if  incoming_msg == 'E3':
        # return cases in North Central
        r = requests.get('https://covid19project.org.ng/api/endpoints/gpzone_affected_states?geop_zone_id=1')
        if r.status_code == 200:
            data = r.json()
            for each in data['Covid19NG']:
                text = ".\n\n"+each['name']+" : Cases ("+each['cases']+ ")"+" : Discharged ("+each['recovered']+")"+" : Deaths ("+each['death']+ ")"
                print(text)
                msg.body(text)
        else:
            text = 'I could not retrieve the results at this time, sorry.'
            print(text)
        #msg.body(text)
        responded = True
    
    if  incoming_msg == 'E4':
        # return cases in North East
        r = requests.get('https://covid19project.org.ng/api/endpoints/gpzone_affected_states?geop_zone_id=2')
        if r.status_code == 200:
            data = r.json()
            for each in data['Covid19NG']:
                text = ".\n\n"+each['name']+" : Cases ("+each['cases']+ ")"+" : Discharged ("+each['recovered']+")"+" : Deaths ("+each['death']+ ")"
                print(text)
                msg.body(text)
        else:
            text = 'I could not retrieve the results at this time, sorry.'
            print(text)
        #msg.body(text)
        responded = True
    
    if  incoming_msg == 'E5':
        # return cases in North West
        r = requests.get('https://covid19project.org.ng/api/endpoints/gpzone_affected_states?geop_zone_id=3')
        if r.status_code == 200:
            data = r.json()
            for each in data['Covid19NG']:
                text = ".\n\n"+each['name']+" : Cases ("+each['cases']+ ")"+" : Discharged ("+each['recovered']+")"+" : Deaths ("+each['death']+ ")"
                print(text)
                msg.body(text)
        else:
            text = 'I could not retrieve the results at this time, sorry.'
            print(text)
        #msg.body(text)
        responded = True

    if  incoming_msg == 'E6':
        # return cases in  South East
        r = requests.get('https://covid19project.org.ng/api/endpoints/gpzone_affected_states?geop_zone_id=4')
        if r.status_code == 200:
            data = r.json()
            for each in data['Covid19NG']:
                text = ".\n\n"+each['name']+" : Cases ("+each['cases']+ ")"+" : Discharged ("+each['recovered']+")"+" : Deaths ("+each['death']+ ")"
                print(text)
                msg.body(text)
        else:
            text = 'I could not retrieve the results at this time, sorry.'
            print(text)
        #msg.body(text)
        responded = True

    if  incoming_msg == 'E7':
        # return cases in  South South
        r = requests.get('https://covid19project.org.ng/api/endpoints/gpzone_affected_states?geop_zone_id=5')
        if r.status_code == 200:
            data = r.json()
            for each in data['Covid19NG']:
                text = ".\n\n"+each['name']+" : Cases ("+each['cases']+ ")"+" : Discharged ("+each['recovered']+")"+" : Deaths ("+each['death']+ ")"
                print(text)
                msg.body(text)
        else:
            text = 'I could not retrieve the results at this time, sorry.'
            print(text)
        #msg.body(text)
        responded = True

    if incoming_msg == 'E8':
        # return cases in  South West
        r = requests.get('https://covid19project.org.ng/api/endpoints/gpzone_affected_states?geop_zone_id=6')
        if r.status_code == 200:
            data = r.json()
            for each in data['Covid19NG']:
                text = ".\n\n"+each['name']+" : Cases ("+each['cases']+ ")"+" : Discharged ("+each['recovered']+")"+" : Deaths ("+each['death']+ ")"
                print(text)
                msg.body(text)
        else:
            text = 'I could not retrieve the results at this time, sorry.'
            print(text)
        #msg.body(text)
        responded = True

    if incoming_msg == 'E9':
        text = f'_Coronavirus spreads from an infected person through_ 👇 \n\n ♦ Small droplets from the nose or mouth which are spread when a person coughs or sneezes \n\n ♦ Touching an object or surface with these droplets on it and then touching your mouth, nose, or eyes before washing your hands \n \n ♦ Close personal contact, such as touching or shaking hands  \n\n 👉 Type J to check the *Preventive Measures* \n 👉 Type *A, B, C, D, E* to see other options \n 👉 Type *Menu* to view the Main Menu'
        msg.body(text)
        msg.media('https://res.cloudinary.com/Jeremiah Jacob/image/upload/v1586852638/htocf1afalf8v8lrrz6a.jpg')
        responded = True
    
    if incoming_msg == 'E10':
        text = f'_Coronavirus infection can be prevented through the following means_ 👇 \n ✔️ Clean hand with soap and water or alcohol-based hand rub  \n\n ✔️ Cover nose and mouth when coughing & sneezing with a tissue or flexed elbow  \n\n ✔️ Avoid close contact & maintain 1-meter distance with anyone who is coughing or sneezin  \n\n ✔️ Isolation of persons traveling from affected countries or places for at least 14 day  \n\n ✔️ Quarantine if advise  \n\n 👉 Type *A, B, C, D, E, F* to see other option \n 👉 Type *Menu* to view the Main Menu'
        msg.body(text)
        msg.media('https://res.cloudinary.com/Jeremiah Jacob/image/upload/v1586852639/uhpuibqxmvfnmen9we3v.jpg')
        responded = True

#ENDING ENGLISH FUNCTION#


#STARTING YORUBA FUNCTION#

    if incoming_msg == "Y1":
        r = requests.get('https://covid19project.org.ng/api/endpoints/stats?action=totalcases')
        if r.status_code == 200:
            data = r.json()
            text = f'_Awọn iṣiro COVID-19 ni Nigeria_ \n\nAwọn Igba ikẹru : *{data["confirmed"]}*\n\nAwọn igbapada : *{data["recovered"]}* \n\nAwọn Igba lọwọ : *{data["active_cases"]}*\n\n Awọn iku : *{data["death"]}*'
            msg.body(text)
            responded = True
        else:
            text = 'Emi ko le gba awọn abajade pada ni akoko yii, mabinu.'
            msg.body(text)
            responded = True
            
    if  incoming_msg == 'Y2':
        # return cases in Affected States
        r = requests.get('https://covid19project.org.ng/api/endpoints/affected_states')
        if r.status_code == 200:
            data = r.json()
            for each in data['Covid19NG']:
                text = ".\n\n"+each['name']+" : Mimo ("+each['cases']+ ")"+" : nAwọn igbapada ("+each['recovered']+")"+" : Awọn iku ("+each['death']+ ")"
                msg.body(text)
                responded = True
        else:
            text = 'Emi ko le gba awọn abajade pada ni akoko yii, mabinu.'
            responded = True

    if  incoming_msg == 'Y3':
        # return cases in North Central
        r = requests.get('https://covid19project.org.ng/api/endpoints/gpzone_affected_states?geop_zone_id=1')
        if r.status_code == 200:
            data = r.json()
            for each in data['Covid19NG']:
                text = ".\n\n"+each['name']+" : Mimo ("+each['cases']+ ")"+" : nAwọn igbapada ("+each['recovered']+")"+" : Awọn iku ("+each['death']+ ")"
                msg.body(text)
                responded = True
        else:
            text = 'Emi ko le gba awọn abajade pada ni akoko yii, mabinu.'
            responded = True
    
    if  incoming_msg == 'Y4':
        # return cases in North East
        r = requests.get('https://covid19project.org.ng/api/endpoints/gpzone_affected_states?geop_zone_id=2')
        if r.status_code == 200:
            data = r.json()
            for each in data['Covid19NG']:
                text = ".\n\n"+each['name']+" : Mimo ("+each['cases']+ ")"+" : nAwọn igbapada ("+each['recovered']+")"+" : Awọn iku ("+each['death']+ ")"
                msg.body(text)
                responded = True
        else:
            text = 'Emi ko le gba awọn abajade pada ni akoko yii, mabinu.'
            responded = True
    
    if  incoming_msg == 'Y5':
        # return cases in North West
        r = requests.get('https://covid19project.org.ng/api/endpoints/gpzone_affected_states?geop_zone_id=3')
        if r.status_code == 200:
            data = r.json()
            for each in data['Covid19NG']:
                text = ".\n\n"+each['name']+" : Mimo ("+each['cases']+ ")"+" : nAwọn igbapada ("+each['recovered']+")"+" : Awọn iku ("+each['death']+ ")"
                msg.body(text)
                responded = True
        else:
            text = 'Emi ko le gba awọn abajade pada ni akoko yii, mabinu.'
            responded = True

    if  incoming_msg == 'Y6':
        # return cases in  South East
        r = requests.get('https://covid19project.org.ng/api/endpoints/gpzone_affected_states?geop_zone_id=4')
        if r.status_code == 200:
            data = r.json()
            for each in data['Covid19NG']:
                text = ".\n\n"+each['name']+" : Mimo ("+each['cases']+ ")"+" : nAwọn igbapada ("+each['recovered']+")"+" : Awọn iku ("+each['death']+ ")"
                msg.body(text)
                responded = True
        else:
            text = 'Emi ko le gba awọn abajade pada ni akoko yii, mabinu.'
            responded = True

    if  incoming_msg == 'Y7':
        # return cases in  South South
        r = requests.get('https://covid19project.org.ng/api/endpoints/gpzone_affected_states?geop_zone_id=5')
        if r.status_code == 200:
            data = r.json()
            for each in data['Covid19NG']:
                text = ".\n\n"+each['name']+" : Mimo ("+each['cases']+ ")"+" : nAwọn igbapada ("+each['recovered']+")"+" : Awọn iku ("+each['death']+ ")"
                msg.body(text)
                responded = True
        else:
            text = 'Emi ko le gba awọn abajade pada ni akoko yii, mabinu.'
            responded = True

    if incoming_msg == 'Y8':
        # return cases in  South West
        r = requests.get('https://covid19project.org.ng/api/endpoints/gpzone_affected_states?geop_zone_id=6')
        if r.status_code == 200:
            data = r.json()
            for each in data['Covid19NG']:
                text = ".\n\n"+each['name']+" : Mimo ("+each['cases']+ ")"+" : nAwọn igbapada ("+each['recovered']+")"+" : Awọn iku ("+each['death']+ ")"
                msg.body(text)
                responded = True
        else:
            text = 'Emi ko le gba awọn abajade pada ni akoko yii, mabinu.'
            responded = True

    #ENDING YORUBA FUNTION#
            
    if responded == False:
        #msg.body('I only know about COVID-19 in Nigeria, sorry!\n\n Hello 🙋🏽‍♂, \nThis is a COVID-19-Nigeria-Bot developed by Jeremiah Jacob, to provide latest information updates i.e cases in different part the country and create awareness to help you and your family stay safe.\n For any emergency 👇 \n 📞 Helpline: 080097000010 | Toll-Free Number: 112 \n ✉ Email: info@ncdc.gov.ng \n\n Please enter one of the following option 👇 \n *A*. COVID-19 statistics in *Nigeria*. \n *B*. COVID-19 cases in *Affected States*. \n *C*. COVID-19 cases in *North Central*. \n *D*. COVID-19 cases in *North East*. \n *E*. COVID-19 cases in *North West*. \n *F*. COVID-19 cases in *South East*. \n *G*. COVID-19 cases in *South South*. \n *H*. COVID-19 cases in *South West*. \n *I*. How does it *Spread*? \n *J*. *Preventive measures* to be taken.')
        msg.body("Hello 🙋🏽‍♂, \nThis is a COVID-19-Nigeria-Bot developed by Jeremiah Jacob, to provide latest information updates \n\n Use below keys to select your prefered language. \n\n E to continue with English \n\n Y lati yan ede Yoruba \n\n H don zaɓar harshen hausa \n\n I iji họrọ asusu igbo")

    return str(resp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
