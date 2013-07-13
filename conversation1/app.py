from rapidsms.apps.base import AppBase
from conversation1.models import Questions, History

class App(AppBase):
	
	#The function bolow is used when the incoming message comes from the phone whose number is not yet registered in our system
	#A phone number is registered in our system when the user send for the first time the message "JO"
	def guest(tel_num,msg):
		if msg=='JO':
			for q in Questions.objects.all():
				h=History(question=q.question,tel_num=tel,status=0)
				h.save()
			return True
		else:
			return False
		
		
	#The function bolow is used when the incoming message comes from the phone whose number is already registered in our system
	#A phone number is registered in our system when the user send for the first time the message "JO"
	def notguest(tel_num,msg):
		pass
		
		
			
	def handle(self, message):
		tel=message.peer
		msg=message.text.split(" ")[0]
		
		
		if History.objects.filter(tel_num=tel): #If this phone number is already regestered
			notguest(tel,msg)
			
		else:                                   #If this phone number is not regestered
			if guest(tel,msg):
				message.respond("WELCOME TO RAPIDSMS")
			else:
				message.respond("SORY YOU ARE NOT REGISTERED! TO REGISTER YOURSELF SEND JO !")
			
			
			
		#if msg[0]=='JO':
			#for q in Questions.objects.all():
				#h=History(question=q.question,tel_num=tel,status=0)
				#h.save()
			#message.respond("WELCOME TO RAPIDSMS")
			#return True
		#elif History.objects.filter(tel_num=tel):
			#for q in (History.objects.filter(tel_num=tel)):
				#if(q.status==1):
					#q.reponse=message.text
					#q.status=2
					#q.save()
				#if(q.status==0):
					#q.status=1
					#q.save()
					#quest=q.question
					#message.respond(" %s " %(quest))
					#return True
			#message.respond("CONGRATULATION! YOU ARE REGISTERED IN OUR SYSTEM !")
			#return True
		#else:
			#message.respond("SORY YOU ARE NOT REGISTERED! TO REGISTER YOURSELF SEND JO !")
			#return True
			
