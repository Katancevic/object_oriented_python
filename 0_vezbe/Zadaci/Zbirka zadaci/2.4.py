
import datetime 

today = datetime.date.today()

#Od danasnjeg datuma oduzimamo jedan dan kako bismo dobili jucerasnji datum
yesterday = today - datetime.timedelta(days = 1)

#Na danasnji datum dodajemo jedan dan kako bismo dobili sutrasni datum
tomorrow = today + datetime.timedelta(days = 1) 

print('Juce : ',yesterday)
print('Danas : ',today)
print('Sutra : ',tomorrow)
