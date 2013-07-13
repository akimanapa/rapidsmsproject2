"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from rapidsms.tests.harness import RapidTest

class SendSMSTest(RapidTest):


    def test_Accueil(self):
        """Outbox should contain message explaining WELCOME TO RAPIDSMS"""
        self.receive('JO', self.lookup_connections('1')[0])
        self.assertEqual(self.outbound[0].text, 'WELCOME TO RAPIDSMS')
		
