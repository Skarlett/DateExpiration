from time import strftime

class _calendar:
    def __init__(self):
      self.Mon = {
        1:  ('January', 31),
        2:  ('February', 28),
        3:  ('March', 31),
        4:  ('April', 30),
        5:  ('May', 31),
        6:  ('June', 30),
        7:  ('July', 31),
        8:  ('August', 31),
        9:  ('September', 30),
        10: ('October', 31),
        11: ('November', 31),
        12: ('December', 31),
        }

      self.month = int(strftime('%m'))

    def generate(self, AgeInMonths, day=None):
          if day == None:
              self.day = int(strftime('%d'))
          else:
              self.day = int(day)

          self.dead = AgeInMonths
          # Check day
          def __checkday(monthId):
              # Choose month
              _id = self.Mon[monthId]
              # Always safer than sorry
              if self.day > _id[1] - 1:
                  data = self.day - _id[1]
                  if data == 0:
                      # Add one extra since we took one for calucation
                      data = 2

              else:
                  data = self.day
              if validate_Month_and_legal_Date(monthId, data)[2] == True:
                return data
              else: print('Fatal Error')

          def __checkMonth():
              # Math time
              return (self.month + self.dead)

          def __checkYear(mon):
              # Our year
              year = int(strftime("%Y"))
              while mon >= 12 or mon == 12:
                  year += +1
                  mon -= 12
              if mon == 0:
                  mon = 1
              return str(year), str(mon)


          year = __checkYear(__checkMonth())
          return year[1] + '/' + str(__checkday(int(year[1]))) + '/' + year[0]

def validate_Month_and_legal_Date(mon, day):
    oneSec = _calendar()
    if not mon > len(oneSec.Mon) and not 0 >= mon:
        for x in oneSec.Mon:
            if x == mon:
                data = oneSec.Mon[x][1]
                if not int(day) > data and not data <= 0:
                    trueorFalse = True
                else:
                    trueorFalse = False
    else:
        print('Bad month Error')
        trueorFalse = False

    return mon, day, trueorFalse

def checkSpan(age):
    FalseData = []
    cal = _calendar()
    amountOfChecks = 0
    for month in range(1, 13):
         for day in range(1, cal.Mon[month][1]+1):
            amountOfChecks += 1
            data = cal.generate(int(age), day=day).split('/')
            newdata = validate_Month_and_legal_Date(int(data[0]), int(data[1]))
            if newdata[2] == False:
                FalseData.append(newdata)

    if not len(FalseData) == 0:
        for x in FalseData:
            print(x)

    print('days: '+str(amountOfChecks))

def ageTest(yearCheck):
    for x in range(1, 12*int(yearCheck)):
        checkSpan(x)

ageTest(12)
