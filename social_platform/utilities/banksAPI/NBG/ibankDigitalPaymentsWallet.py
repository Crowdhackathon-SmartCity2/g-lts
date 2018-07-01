#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.client
import uuid
import json

__version__     = '1'
__copyright__   = 'GNU General Public License v3.0'
__maintainer__  = 'Tas-sos'
__author__      = 'Tas-sos'
__email__       = 'tas-sos@g-lts.info'


class DigitalPaymentsWallet:

    def __init__(self):
        self.conn = http.client.HTTPSConnection("apis.nbg.gr")
        self.sandboxID = "2593025500905472"
        self.clientID = "3fc6ffe9-5dac-419d-8e6b-5b4012f009bf"

        self.sandbox = self.get_sandbox()

    def donation_user1(self, username, amount):
        """
        Μέθοδος κατάθεσης δωρεάς.

        :param username:        Το username του χρήστη που θα χρεωθεί η δωρεά.
        :param amount:          Το ποσό που δωρίζει.
        :return:
        """

        guid = str(uuid.uuid4())

        payload = """
            {
              "header": {
                "ID": "419FF7EC-1CEE-4CF2-A8E0-8286B1F528CD",
                "application": "419FF7EC-1CEE-4CF2-A8E0-8286B1F528CD",
                 "channel":"{{body.header.channel}}"
                },
              "payload": {
                "userId": "47eaf8de-f924-402e-b3a9-1219a6283b41",
                "actualUserId": """+ username +"""",
                "memberId": "21989497-a829-4029-b506-fd4c24a6d085",
                "deviceRegistrationId": "d7bd5203-96aa-400a-9db2-a15ebe45e285",
                "registrationId": "21989497-a829-4029-b506-fd4c24a6d085",
                "amount": """ + amount + """,
                "reason": "Δωρεά στο κοινονικό παντωπολείο.",
                "contact": {
                  "memberId": "21989497-a829-4029-b506-fd4c24a6d043",
                  "contactId": "21989497-A829-4029-B506-FD4C24A6D083",
                  "firstName": "Δήμος",
                  "surName": "Αμαρουσίου",
                  "nickName": "",
                  "title": "",
                  "registries": [
                    {
                      "name": "string",
                      "isPrimary": true,
                      "description": "string"
                    }
                  ],
                  "status": "Active",
                  "verificationCode": "12345",
                  "identities": [
                    {
                      "identityId": "230BDE44-0EE5-44BB-AEAC-A466F2C45023",
                      "network": "Mobile",
                      "networkId": "+306949504300",
                      "matched": true,
                      "nickName": "IBankPayUser2.nickname",
                      "preferredAccount": "6519D427-2B54-45F9-9591-81DFA64FD344",
                      "preferredAccountId": "82E0B7AE-5EE9-4A24-8A2D-C986B5107B75",
                      "verificationCode": "12345",
                      "status": "Active",
                      "accessToken": "12345"
                    }
                  ]
                },
                "tanNumber": "string",
                "isSmsOtp": true,
                "getInfo": true,
                "registry": {
                  "name": "string",
                  "isPrimary": true,
                  "description": "string"
                }
              }
            }
            """

        headers = {
            'x-ibm-client-id': self.clientID,
            'sandbox_id': self.sandboxID,
            'application_id': self.clientID,
            'user_id': username,
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
            print(json.dumps(json_response))
        except:  # Δεν επιστρέφει JSON, άρα..
            print("Η δωρεά σας στο κοινονικό παντωπολείο πραγματποιήθηκε επιτυχώς.")

    def get_sandbox(self):
        """
        Μέθοδος που κατεβάζει όλο το sandbox.

        :return: Επιστρέφει όλο sandbox ως JSON object.
        """

        headers = {
            'x-ibm-client-id':  self.clientID,
            'accept': "text/json"
        }

        self.conn.request("GET", "/public/sandbox/ibankpaysandbox/v1.1/sandbox/" + self.sandboxID, headers=headers)

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
    nbg = DigitalPaymentsWallet()
    # username , amount
    # nbg.donation_user1('1000815', "0.5")
