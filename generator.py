class _calendar:
    def __init__(self, AgeInMonths):
      self.Mon = {
      # Num Month NumOfDays
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
      #Current data
      self.month = int(strftime('%m'))
      self.day = int(strftime('%d'))
      #How many months
      self.dead = AgeInMonths

    def generate(self):
        # Check day
        def __checkday():
            # Choose month
            _id = self.Mon[self.month]
            # Always safer than sorry
            if self.day > _id[1]-1:
                data = self.day - _id[1]
                if data == 0:
                    # Add one extra since we took one for calucation
                    data = 2
            
            else: data = self.day
            return data

        def __checkMonth():
            # Math time
            return (self.month+self.dead)

        def __checkYear():
            # Our year
            year = int(strftime("%Y"))
            while self.dead > 12 or self.dead == 12:
                year += +1
                self.dead -= 12
            return str(year)

        year = __checkYear()
        month = str(__checkMonth())
        return month+'/'+str(__checkday())+'/'+year

# Example...
# print(_calander(monthsToExpire).generate())
