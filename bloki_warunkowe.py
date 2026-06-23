pensja=12000
wczasy = "morze"
if pensja<5000 and wczasy=="mazury":
    komunikat="nie za wiele na wczasy"
elif (pensja<8000 and
# \ podział wiersza na kilka linii
    (wczasy=="mazury" 
    or wczasy=="morze")):
    komunikat="może tak być"
elif pensja<13000 and pensja>=8000:
    komunikat="super"
else:
    komunikat="moze być"
 
 
 
 #komunikaty



print(komunikat)