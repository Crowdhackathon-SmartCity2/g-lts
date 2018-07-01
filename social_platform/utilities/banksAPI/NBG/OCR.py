#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.client
import uuid         # https://docs.python.org/3/library/uuid.html
import json

__version__     = '1'
__copyright__   = 'GNU General Public License v3.0'
__maintainer__  = 'Tas-sos'
__author__      = 'Tas-sos'
__email__       = 'tas-sos@g-lts.info'


class OCR:

    def __init__(self):
        self.conn = http.client.HTTPSConnection("apis.nbg.gr")
        self.sandboxID = "2101750861398016"
        self.clientID = "3fc6ffe9-5dac-419d-8e6b-5b4012f009bf"
        self.sandbox = self.get_sandbox()



    def upload(self, type):
        """
         Μέθοδος αποστολής εγγράφου.

        Στην μέθοδο αυτή αποστέλετε ένα εικονικό έγγραφο στο open API της εθνικής τράπεζας ώστε να γίνει εκμεταύλεση
        της αναγώρισης και εξαγωγής δεδομένων από το έγγραφο.
        Το έγγραφο είναι "εικονικό" λόγο της προσωρινής υλοποίησης του "Optical Character Recognition (1.0.0)", σε
        παραγωγικό περιβάλλον το έγγραφο θα ανεβαίνει κανονικά.

        :param type: Ορίζεται ο τύπος του εγγράφου. Υπάρχουν οι ακόλουθεί τύποι :
            > Passport
            extractedDocumentType : 1cc5088d-2e92-41e6-b012-62dd0200bf16

            > DrivingLicensePage
            extractedDocumentType : 027affc9-99a9-49ce-a873-1192946e9983

            > BackIDPage
            extractedDocumentType : 1782d81f-5ac0-4a71-ae44-97cf1b6f348d

            > TaxForm
            extractedDocumentType : e0236ce1-9ea1-459b-82cd-cce5f5ff36b0

            > DehPage
            extractedDocumentType : 0eea3272-e69c-42ff-a2dd-7e1896fee894

            > EydapPage
            extractedDocumentType : 583973d4-ee99-4bab-9c8e-02dd85851e08

        :return: Ανεβάζει στο sandbox ένα έγγραφο.
        """
        guid = str(uuid.uuid4())

        doc_type = ""

        if type == "Passport":
            doc_type = "1cc5088d-2e92-41e6-b012-62dd0200bf16"
        if type == "DrivingLicensePage":
            doc_type = "027affc9-99a9-49ce-a873-1192946e9983"
        if type == "BackIDPage":
            doc_type = "1782d81f-5ac0-4a71-ae44-97cf1b6f348d"
        if type == "TaxForm":
            doc_type = "e0236ce1-9ea1-459b-82cd-cce5f5ff36b0"
        if type == "DehPage":
            doc_type = "0eea3272-e69c-42ff-a2dd-7e1896fee894"
        if type == "EydapPage":
            doc_type = "583973d4-ee99-4bab-9c8e-02dd85851e08"

        payload = """
        {\"header\":
            {
                \"ID\":\"""" + guid + """\",
                \"application\":\"""" + guid + """\",
                \"bank\":\"NBG\",
                \"hostSession\": null,
                \"channel\":\"web\",
                \"customer\":0,
                \"logitude\":0,
                \"latitude\":0,
                \"go4moreMember\":\"true\",
                \"TAN\": null
            },
            \"payload\":
            {
                \"declaredDocumentType\":\"""" + doc_type + """\",
                \"initialDocumentFormat\":\"string\",
                \"initialDocumentName\":\"string\",
                \"isMultiPage\":\"true\"
            }
        }"""

        headers = {
            'x-ibm-client-id': self.clientID,
            'sandbox_id': self.sandboxID,
            'application_id': self.clientID,
            'user_id': '645AF800-8C97-4F47-B489-6B9D7B05B86D',
            'username': 'User1',
            'provider_id': "NBG.gr",
            'provider': "NBG",
            'content-type': "text/json",
            'accept': "text/json"
        }

        # payload.encode('utf-8')
        self.conn.request("POST", "/public/sandbox/ocr.sandbox/v1/OcrDocument/uploadDocument", payload, headers)

        res = self.conn.getresponse()
        data = res.read()

        try:
            json_response = json.loads(data.decode("utf-8"))
            # print( json.dumps(json_response) )
            if type == "BackIDPage":
                self.view_upload_BackIDPage_details(json_response)
            if type == "Passport":
                self.view_upload_Passport_details(json_response)
            if type == "DrivingLicensePage":
                self.view_upload_DrivingLicensePage_details(json_response)
            if type == "TaxForm":
                self.view_upload_TaxForm_details(json_response)
            if type == "DehPage":
                self.view_upload_DehPage_details(json_response)
            if type == "EydapPage":
                self.view_upload_EydapPage_details(json_response)


        except Exception as e:  # Δεν επιστρέφει JSON, άρα..
            print(e)
            print("Η αποστολή του εγγράφου απέτυχε")



        # print(data.decode("utf-8"))

        # print( json.dumps(data.decode("utf-8"), indent=4 ) )
        # Right
        # print(data.decode("utf-8"))

    def view_upload_Passport_details(self, response):
        print("Το διαβατήριο σας ανέβηκε επιτυχώς και αναγνωρίστηκαν τα παρακάτω : ")
        print("\tΕθνικότητα : ", response['payload']['items'][1]['propertyValue'])
        print("\tΑριθμός διαβατηρίου : ", response['payload']['items'][2]['propertyValue'])
        print("\tΕπώνυμα : ", response['payload']['items'][3]['propertyValue'])
        print("\tΗμερωμηνία έκδοσης : ", response['payload']['items'][8]['propertyValue'])

    def view_upload_DrivingLicensePage_details(self, response):
        print("Ανέβηκε επιτυχώς η άδεια οδήγισης και αναγνωρίστηκαν τα παρακάτω : ")
        print("\tΕπώνυμο : ", response['payload']['items'][1]['propertyValue'])
        print("\tΌνομα : ", response['payload']['items'][3]['propertyValue'])
        print("\tΗμερωμηνία γέννησης οδηγού : ", response['payload']['items'][4]['propertyValue'])
        print("\tΤόπος γέννησης οδηγού : ", response['payload']['items'][5]['propertyValue'])
        print("\tΗμερωμηνία έκδοσης : ", response['payload']['items'][6]['propertyValue'])
        print("\tΕκδόθηκε από : ", response['payload']['items'][7]['propertyValue'])
        print("\tΗμερωμηνία λήξης : ", response['payload']['items'][8]['propertyValue'])
        print("\tΑ.Φ.Μ. οδηγού : ", response['payload']['items'][9]['propertyValue'])
        print("\tΚατηγόρια διπλώματος : ", response['payload']['items'][11]['propertyValue'])

    def view_upload_BackIDPage_details(self, response):
        print("Η αστυνομική σας ταυτότητα ανέβηκε επιτυχώς και αναγνωρίστηκαν τα παρακάτω : ")
        print("\tΕπώνυμο : ", response['payload']['items'][1]['propertyValue'])
        print("\tΌνομα : ", response['payload']['items'][3]['propertyValue'])
        print("\tΌνομα πατρός : ", response['payload']['items'][5]['propertyValue'])
        print("\tΌνομα μητρός : ", response['payload']['items'][3]['propertyValue'])
        print("\tΗμερωμηνία γέννησης : ", response['payload']['items'][9]['propertyValue'])
        print("\tΤόπος γέννησης : ", response['payload']['items'][10]['propertyValue'])

    def view_upload_TaxForm_details(self, response):
        print("Η φορολογική σας δήλωση ανέβηκε απιτυχώς και αναγνωρίστηκαν τα παρακάτω : ")
        print("\tΑριθμός παιδιών : ",           response['payload']['items'][11]['propertyValue'])
        print("\tΠλήρες ονοματεπώνυμο : ",      response['payload']['items'][12]['propertyValue'])
        print("\tΌνομα πατρώς : ",              response['payload']['items'][13]['propertyValue'])
        print("\tΑ.Φ.Μ. : ",                    response['payload']['items'][14]['propertyValue'])
        print("\tΔιεύθυνση : ",                 response['payload']['items'][15]['propertyValue'])
        print("\tΔ.Ο.Υ : ",                     response['payload']['items'][16]['propertyValue'])
        print("\tΗμερωμηνία έκδοσης : ",        response['payload']['items'][18]['propertyValue'])
        print("\tΣυνολικό δηλωθέν εισόδημα : ", response['payload']['items'][26]['propertyValue'])
        print("\tΦορολογικό έτος : ",           response['payload']['items'][27]['propertyValue'])

    def view_upload_DehPage_details(self, response):
        print("Ανέβηκε επιτυχώς ο λογαριασμός της Δ.Ε.Η. και αναγνωρίστηκαν τα παρακάτω : ")
        print("\tΠλήρες ονοματεπώνυμο : ", response['payload']['items'][0]['propertyValue'])
        print("\tΔιεύθυνση κατοικίας : ", response['payload']['items'][1]['propertyValue'])
        print("\tΑ.Φ.Μ. : ", response['payload']['items'][3]['propertyValue'])

    def view_upload_EydapPage_details(self, response):
        print("Ανέβηκε επιτυχώς ο λογαριασμός της Ε.Υ.Δ.Α.Π. και αναγνωρίστηκαν τα παρακάτω : ")
        print("\tΙδιοκτήτης λογαριασμού : ", response['payload']['items'][0]['propertyValue'])
        print("\tΔιεύθυνση κατοικίας : ", response['payload']['items'][2]['propertyValue'])
        print("\tΑ.Φ.Μ. : ", response['payload']['items'][3]['propertyValue'])
        print("\tΑριθμός μετρητή : ", response['payload']['items'][4]['propertyValue'])


    def get_sandbox(self):
        """
        Μέθοδος που κατεβάζει όλο το sandbox.

        :return: Επιστρέφει όλο sandbox ως JSON object.
        """

        headers = {
            'x-ibm-client-id':  self.clientID,
            'accept': "text/json"
        }

        self.conn.request("GET", "/public/sandbox/ocr.sandbox/v1/sandbox/" + self.sandboxID, headers=headers)

        res = self.conn.getresponse()
        data = res.read()

        # print( data.decode("utf-8") )
        return json.loads( data.decode("utf-8") )

    def get_passport_document(self, surname):
        """
        Μέθοδος η οποία αναζητάει για το διαβατήριο ενώς ατόμου και επιστρέφει (αν το βρει) τα στοιχεία του.

        Υποτίθετε πως έχει ανεβεί ήδη το διαβατήριο και το ψάχνει με βάση το επώνυμο του χρήστη.
        :param surname: Το surname του χρήστη για τον οποίο θα ψάξει να βρει το διαβατήριο του και θα του επιστρέψει τα
        ακόλουθα ( αν το βρει ) :
            * Nationality
            * Passport_Number
            * Issue_Date
        :return: Τα στοιχεία του διαβατηρίου του ( αν το βρει )
        """

        nationality = ""
        passport_number = ""
        issue_date = ""

        for user in self.sandbox['payload']['Documents']:
            if user['DocumentType'] == 'Passport':
                for item in user['Items']:
                    if item['PropertyName'] == 'Sur_Name' and item['PropertyValue'] == surname:
                        for p in user['Items']:
                            if p['PropertyName'] == 'Nationality':
                                nationality = p['PropertyValue']
                            if p['PropertyName'] == 'Passport_No':
                                passport_number = p['PropertyValue']
                            if p['PropertyName'] == 'Issue_Date':
                                issue_date = p['PropertyValue']

        print("Ιθαγένεια : ", nationality)
        print("Αριθμός διαβατηρίου : ", passport_number)
        print("Ημερομηνία έκδοσης : ", issue_date)

        return nationality, passport_number, issue_date


if __name__ == "__main__":
    ocr = OCR()
    # ocr.get_passport_document("PAPADOPOULOS")

    # Choose one type from : "Passport", "DrivingLicensePage", "BackIDPage", "TaxForm", "DehPage", "EydapPage"
    # ocr.upload("Passport")


