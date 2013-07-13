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
		h=History(question="q1",tel_num=tel,status=1)
		h.save()
		h1=History(question="q2",tel_num=tel,status=0)
		h1.save()			
		self.receive('JO', self.lookup_connections('1')[0])
		self.assertEqual(self.outbound[0].text, h1.question)
