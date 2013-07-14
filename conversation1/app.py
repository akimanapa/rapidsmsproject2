from rapidsms.apps.base import AppBase
from conversation1.models import Questions, History

class App(AppBase):
	def handle(self, message):
		tel=message.peer
		msg=message.text.split(" ")
		
		if History.objects.filter(tel_num=tel):
			for q in (History.objects.filter(tel_num=tel)):
				if(q.status==1):
					q.reponse=message.text
					q.status=2
					q.save()
				if(q.status==0):
					q.status=1
					q.save()
					quest=q.question
					message.respond(" %s " %(quest))
					return True
			message.respond("CONGRATULATION! YOU ARE REGISTERED IN OUR SYSTEM !")
			return True
		elif msg[0]=='JO':
			for q in Questions.objects.all():
				h=History(question=q.question,tel_num=tel,status=0)
				h.save()
			if History.objects.filter(tel_num=tel):
				message.respond("WELCOME TO RAPIDSMS!")
			else:
				message.respond("SORY, TRY AGAIN LATER!")
			return True
		else:
			message.respond("SORY YOU ARE NOT REGISTERED! TO REGISTER YOURSELF SEND JO !")
			return True
			
