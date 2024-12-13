proj=float(input("enter project score:"))
intern=float(input("enter internal score:"))
ext=float(input("enter external score:"))
if proj>=50 and intern>=50 and ext>=50:
   total=(70/100)*proj+(10/100)*intern+(20/100)*ext
   if total>=90:
       print("A grade")
   elif total>80:
       print("B grade")
   elif total>70:
       print("C grade")
   else:
       print("D grade")
else:
   if proj<50:
       print("failed in project and score is:",proj)
   if ext<50:
       print("failed in external and score is:",ext)
   if intern<50:
       print("failed in internal and score is:",intern)