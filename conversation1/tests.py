"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from rapidsms.tests.harness import RapidTest
from conversation1.models import Questions, History

class SendSMSTest(RapidTest):


    def test_when_JO_is_send_the_first_time(self):
        """Outbox should contain message 'WELCOME TO RAPIDSMS' """
        self.receive('JO', self.lookup_connections('1')[0])
        self.assertEqual(self.outbound[0].text, 'WELCOME TO RAPIDSMS')
	def test_when_JO_is_send_as_an_answer(self):
		"""Outbox should contain the next question """
		History.objects.create(question="q1",tel_num=tel,status=1)
		History.objects.create(question="q2",tel_num=tel,status=0)
		self.receive('JO', self.lookup_connections('1')[0])
		
		self.assertEqual(self.outbound[0].text,"q2")
