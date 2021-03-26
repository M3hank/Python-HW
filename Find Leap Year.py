year = int(input("ENTER THE YEAR: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} IS A LEAP YEAR".format(year))
       else:
           print("{0} IS NOT A LEAP YEAR".format(year))
   else:
       print("{0} IS A LEAP YEAR".format(year))
else:
   print("{0} IS NOT A LEAP YEAR".format(year))
