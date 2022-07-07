class myInput():
    def __init__(self, text):
      print(text)
      temp_value = input()
      for symbol in temp_value:
          if not symbol.isdigit():
              self.value = str(temp_value)
              break
      else:
          self.value = int(temp_value)

    def __str__(self):
      return str(self.value)
        
def mytype(var):
  return type(var.value)

#########

a = myInput("Ievadi datus!")
print(mytype(a))

