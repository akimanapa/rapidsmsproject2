"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from rapidsms.tests.harness import RapidTest
from conversation1.models import Questions, History

#For two next tests, is the case when the phone number is not known in our system and the incoming message is 'JO'

class SendSMSTest0(RapidTest):
    def test_when_JO_is_send_but_no_question(self):#If there is no question(s) available, the registration must not be possible
        """Outbox should contain message 'SORY, TRY AGAIN LATER!' """
        self.receive('JO', self.lookup_connections('1')[0])
        self.assertEqual(self.outbound[0].text, 'SORY, TRY AGAIN LATER!')


class SendSMSTest1(RapidTest):
    def test_when_JO_is_send_the_first_time(self):#If there is question(s) and the message 'JO' comes from the no registered user, he/she must get the message 'WELCOME TO RAPIDSMS!'
												  # and the question(s) to ask him/her are recorded in the table History
        """Outbox should contain message 'WELCOME TO RAPIDSMS' """
        Questions.objects.create(question="q")
        self.receive('JO', self.lookup_connections('1')[0])
        self.assertEqual(History.objects.all()[0].question,'q')
        self.assertEqual(self.outbound[0].text, 'WELCOME TO RAPIDSMS!')
        

#For all tests above, is the case when the phone number is not known in our system and the incoming message is 'JO'



#The next test, is the case when the phone number is not known in our system and the incoming message is not 'JO'
class SendSMSTest2(RapidTest):
    def test_when_JO_is_send_the_first_time(self):
        """Outbox should contain message 'SORY YOU ARE NOT REGISTERED! TO REGISTER YOURSELF SEND JO !' """
        Questions.objects.create(question="q")
        self.receive('message', self.lookup_connections('1')[0])
        self.assertEqual(self.outbound[0].text, 'SORY YOU ARE NOT REGISTERED! TO REGISTER YOURSELF SEND JO !')
        

     
#For the next test, the phone number is known in the system and the incoming message is 'JO'   
class SendSMSTest3(RapidTest):       
	def test_when_JO_is_send_as_an_answer(self):#If the answer of a question is 'JO' the system ask to the user the next question, the status of the previous and the next question changes,and the response of the previous question is recorded
		"""Outbox should contain the next question """
		History.objects.create(question="q1",tel_num=2,status=1)
		History.objects.create(question="q2",tel_num=2,status=0)
		self.receive('JO', self.lookup_connections('2')[0])
		self.assertEqual(History.objects.all()[0].status,2)
		self.assertEqual(History.objects.all()[1].status,1)
		#self.assertEqual(History.objects.all()[0].response,'JO')
		self.assertEqual(self.outbound[0].text,u' q2 ')


class SendSMSTest4(RapidTest):       
	def test_question(self):#If the user responds to all questions he/she must get a message that informs him/her that he/she is registered:
		"""Outbox should contain 'CONGRATULATION! YOU ARE REGISTERED IN OUR SYSTEM !' """
		History.objects.create(question="q1",tel_num=2,status=1)
		self.receive('message', self.lookup_connections('2')[0])
		self.assertEqual(History.objects.all()[0].status,2)
		self.assertEqual(self.outbound[0].text,'CONGRATULATION! YOU ARE REGISTERED IN OUR SYSTEM !')
		

