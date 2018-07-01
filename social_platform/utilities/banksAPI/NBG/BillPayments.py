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


class BillPayments:

    def __init__(self):
        self.conn = http.client.HTTPSConnection("apis.nbg.gr")
        self.sandboxID = "5100773314658304"
        self.clientID = "3fc6ffe9-5dac-419d-8e6b-5b4012f009bf"

        self.sandbox = self.get_sandbox()



    def pay_dei(self, username, debtorFullName, amount):
        """
        Μέθοδος πληρωμής της ΔΕΗ.

        :param username:        Το username του χρήστη που θα χρεωθεί.
        :param debtorFullName:  Το πλήρες ονοματεπώνυπο ή περιγραφή για αυτόν που θα χρεωθεί.
        :param amount:          Το ποσό που πληρώνει.
        :return:
        """

        # UserID, AccountID, IBAN
        user_id, account_id, iban = self.get_user_details(username)

        guid = str(uuid.uuid4())
        # guid = "ea504c5c-86a4-4800-9bcf-a3552745eb05"

        payload = """
        {\n
              \"header\": {\n
                \"ID\": \"""" + guid + """\",\n 
                \"application\": \"""" + self.clientID + """\",\n 
                \"bank\": \"NBG\",\n
                \"hostSession\": null,\n 
                \"channel\": \"tpp\",\n 
                \"customer\": 0,\n
                \"logitude\": 0,\n 
                \"latitude\": 0,\n 
                \"go4moreMember\": true,\n 
                \"TAN\": null\n
              },\n
              \"payload\": {\n 
                \"userId\": \"""" + user_id + """\",\n
                \"paymentIdentification\": {\n
                  \"instrId\": \"""" + guid + """\",\n 
                  \"endtoendId\": null,\n
                  \"txId\": \"""" + guid + """\",\n 
                  \"clrSysRef\": null\n
                },\n
                \"paymentOrgIdentification\": {\n 
                  \"id\": \"69d6ffc8-cc65-4130-a172-d2fa16b6cbe8\",\n 
                  \"barcode\": null,\n
                  \"fields\": {\n
                  \t\"PAYMENT_CODE\" : \"1234567890\"\n 
                  },\n
                  \"extraData\": {}\n 
                },\n
                \"chargesInfo\": null,\n 
                \"settlementInfo\": {\n 
                  \"ccy\": \"EUR\",\n
                  \"amount\": """ + amount + """,\n 
                  \"method\": \"ACCT\"\n
                },\n
                \"debtor\": {\n 
                  \"name\": \"""" + debtorFullName + """\",\n 
                  \"debtorAccount\": {\n
                    \"iban\": \"""" + iban + """\",\n 
                    \"pan\": null\n
                  },\n
                  \"telephone\": \"2101234567\"\n 
                },\n
                \"ultimateDebtor\":  null,\n 
                \"remittanceInfo\": null,\n
                \"requestMachineId\": null,\n 
                \"acceptDuplicate\": true,\n
                \"machineId\": null\n
              }\n
            }
            """

        headers = {
            'x-ibm-client-id': self.clientID,
            'sandbox_id': self.sandboxID,
            'application_id': self.clientID,
            'user_id': user_id,
            'username': username,
            'provider_id': "NBG.gr",
            'provider': "NBG",
            'content-type': "text/json",
            'accept': "text/json"
        }

        self.conn.request("POST", "/public/sandbox/billpayments/v2/BillPayments/pay", payload.encode('utf-8'), headers)

        res = self.conn.getresponse()
        data = res.read()

        try:
            json_response = json.loads( data.decode("utf-8") )
            print(json_response['exception']['desc'])
        except:  # Δεν επιστρέφει JSON, άρα..
            print("Η πληρωμή σας στην Δ.Ε.Η. πραγματποιήθηκε επιτυχώς")
        # Right
        # print(data.decode("utf-8"))



    def pay_eydap(self, username, debtorFullName, amount):
        """
        Μέθοδος πληρωμής της Ε.Υ.Δ.Α.Π.

        :param username:        Το username του χρήστη που θα χρεωθεί.
        :param debtorFullName:  Το πλήρες ονοματεπώνυπο ή περιγραφή για αυτόν που θα χρεωθεί.
        :param amount:          Το ποσό που πληρώνει.
        :return:
        """

        # UserID, AccountID, IBAN
        user_id, account_id, iban = self.get_user_details(username)
        guid = str(uuid.uuid4())

        payload = """
             {\n
            \"header\": {\n
              \"ID\": \"""" + guid + """"\",\n
              \"application\": \"""" + self.clientID + """\",\n
              \"bank\": \"NBG\",\n
              \"hostSession\": null,\n
              \"channel\": \"tpp\",\n
              \"customer\": 0,\n
              \"logitude\": 0,\n
              \"latitude\": 0,\n
              \"go4moreMember\": true,\n
              \"TAN\": null\n
            },\n
            \"payload\": {\n
              \"userId\": \" """ + user_id + """ \",\n
              \"paymentIdentification\": {\n
                \"instrId\": \"""" + guid + """\",\n
                \"endtoendId\": null,\n
                \"txId\": \" """ + guid + """\",\n
                \"clrSysRef\": null\n
              },\n
              \"paymentOrgIdentification\": {\n
                \"id\": \"58f02321-441c-4c95-87a2-295092851534\",\n 
                \"barcode\": null,\n
                \"fields\": {\n
                \t\"PAYMENT_CODE\" : \"1234567890\",\n
                \t\"CUSTOMER_NAME\" : \"""" + debtorFullName + """\",\n
                \t\"EXPIRATION_DATE\" : \"2018-01-20\"\n
                },\n
                \"extraData\": {}\n
              },\n
              \"chargesInfo\": null,\n
              \"settlementInfo\": {\n
                \"ccy\": \"EUR\",\n
                \"amount\": """ + amount + """,\n
                \"method\": \"ACCT\"\n
              },\n
              \"debtor\": {\n
                \"name\": \"""" + debtorFullName + """\",\n
                \"debtorAccount\": {\n
                  \"iban\": \"""" + iban + """\",\n
                  \"pan\": null\n
                },\n
                \"telephone\": \"2101234567\"\n
              },\n
              \"ultimateDebtor\":  null,\n
              \"remittanceInfo\": null,\n
              \"requestMachineId\": \"DemoSpotMachine1\",\n   // Αλλάζει και αυτό επίσης σε σχέση με την ΔΕΗ.
              \"acceptDuplicate\": true,\n
              \"machineId\": null\n
            }\n
            "}"
             """

        headers = {
            'x-ibm-client-id': self.clientID,
            'sandbox_id': self.sandboxID,
            'application_id': self.clientID,
            'user_id': user_id,
            'username': username,
            'provider_id': "NBG.gr",
            'provider': "NBG",
            'content-type': "text/json",
            'accept': "text/json"
        }

        self.conn.request("POST", "/public/sandbox/billpayments/v2/BillPayments/pay", payload.encode('utf-8'), headers)

        res = self.conn.getresponse()
        data = res.read()

        try:
            json_response = json.loads(data.decode("utf-8"))
            print(json_response['exception']['desc'])
        except:  # Δεν επιστρέφει JSON, άρα..
            print("Η πληρωμή σας στην Ε.Υ.Δ.Α.Π. πραγματποιήθηκε επιτυχώς")


    def get_sandbox(self):
        """
        Μέθοδος που κατεβάζει όλο το sandbox.

        :return: Επιστρέφει όλο sandbox ως JSON object.
        """

        headers = {
            'x-ibm-client-id':  self.clientID,
            'accept': "text/json"
        }

        self.conn.request("GET", "/public/sandbox/billpayments/v2/sandbox/" + self.sandboxID, headers=headers)

        res = self.conn.getresponse()
        data = res.read()

        return json.loads( data.decode("utf-8") )

    def get_user_details(self, username):
        """
        Μέθοδος η οποία βρίσκει όλα τα στοιχεία ενώς χρήστη με βάση το όνομα του.

        :param username: Το username του χρήστη για τον οποίο θα βρεί τα ακόλουθα στοιχεία :
            * UserID
            * AccountID
            * IBAN
        :return:
        """

        for user in self.sandbox['payload']['users']:
            if user['userName'] == username:
                # UserID, AccountID, IBAN
                return str(user['userId']), str(user['userAccounts'][0]['accountId']), str(user['userAccounts'][0]['accountTypeValue'])


if __name__ == "__main__":
    nbg = BillPayments()
    # nbg.pay_dei("User3", "Πληρώνει ΔΕΗ", "80")
    # nbg.pay_eydap("User4", "Πληρώνει Ε.Υ.Δ.Α.Π.", "80")
