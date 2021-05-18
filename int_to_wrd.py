import pyttsx3 
import speech_recognition as sr 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def int_to_en(m):
	d = { 0 : 'Zero', 1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five',
          6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9 : 'Nine', 10 : 'Ten',
          11 : 'Eleven', 12 : 'Twelve', 13 : 'Thirteen', 14 : 'Fourteen',
          15 : 'Fifteen', 16 : 'Sixteen', 17 : 'Seventeen', 18 : 'Eighteen',
          19 : 'Nineteen', 20 : 'Twenty',
          30 : 'Thirty', 40 : 'Forty', 50 : 'Fifty', 60 : 'Sixty',
          70 : 'Seventy', 80 : 'Eighty', 90 : 'Ninety'
        }
	if(m=='q'):
		exit()
	n=int(m)
	if n<20:
		return d[n]
	elif n<100:
		return(d[(int((n/10))*10)]+"-"+d[(n%10)])
	elif n<1000:
		return(d[(int(n/100))]+" hundread and "+int_to_en(n%100))
	elif n<10000:
		return(d[(int(n/1000))]+" thousand "+int_to_en(n%1000))
	elif n<100000:
		return(int_to_en(int(n/1000))+" thousand "+int_to_en(n%1000))
	elif n<1000000:
		return(d[(int(n/100000))]+" lakh "+int_to_en(n%100000))
	elif n<10000000:
		return(int_to_en(int(n/100000))+" lakh "+int_to_en(n%100000))	
	elif n<100000000:
		return(d[(int(n/10000000))]+" crore "+int_to_en(n%10000000))
	else:
		t="no"
		return t
		#If want to read from a file
'''		
with open("text.txt","r")as f:
	num=int(f.read())
print(str(num)+" = "+int_to_en(num))
'''
print("\n")
print("_____________WELCOME TO NUMBER TO WORD CONVERSION WINDOW_____________\n")
while(True):
	num=input("\n Enter the Number or Press q to Quit: ")
	print("\n")
	numwrd=int_to_en(num)
	if(numwrd=='no'):
		print("Very large number is entered, kindly enter a smaller number")
		speak("Very large number is entered, kindly enter a smaller number")	
	else:
		print(num+" = "+numwrd+"\n")
		speak("The Number in words is, "+numwrd)

	
