



class Token:

   def __init__(self, token_type='UNKNOWN', value=None, string='', line=-1, col=-1):
      self.category = token_type
      self.position = line, col
      self.symbol = string
      self.value = value

   def __str__(self):
      return f'{self.symbol:^20} {self.category:<22} {self.value:^20} {self.position[0]:8d}'

'''class Number(Token):

   def __init__(self, value=0, line=-1, col=-1):
      Token.__init__(self, 'NUMBER', '', line, col)
      self.value = value

   def __str__(self):
      return '({}, {}, line={}, column={})'.format(self.category, self.value, self.position[0], self.position[1])

class Real(Token):

   def __init__(self, value=0.0, line=-1, col=-1):
      Token.__init__(self, 'REAL', '', line, col)
      self.value = value

   def __str__(self):
      return '({}, {}, line={}, column={})'.format(self.category, self.value, self.position[0], self.position[1])
   

class Boolean(Token):

   def __init__(self, value=False, line=-1, col=-1):
      Token.__init__(self, 'BOOL', '', line, col)
      self.value = value

   def __str__(self):
      return '({}, {}, line={}, column={})'.format(self.category, self.value, self.position[0], self.position[1])'''