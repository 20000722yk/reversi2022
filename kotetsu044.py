#貪欲AI
import random
class kotetsuAI(object):
  def name(self):
    return 'kotetsu044'

  def put_and_reverse(self, x, y, color, reverse=True):
    if not self.on(x, y) or self.b[y, x] != EMPTY:
      return 0
      reversibles = []
      for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
          rs = self.find_reversibles(x, y, dx, dy, color)
          reversibles.extend(rs)
      
      if reverse and len(reversibles) > 0:
        self.b[y, x] = color
        for xt, yt in reversibles:
          self.b[yt, xt] = color
      return len(reversibles)
  
  def play(self, board, color):
    #現在の局面と色を受け取り、色を置く場所(x,y)を返す
      while True:
        A=[]
        for i in range(0,board.N+1):
          for j in range(0,board.N+1):
            if board.put_and_reverse(i, j, color, reverse=False) > 0:
              # A.append([put_and_reverse(self,i,j,color),i,j]) を A.append([board.put_and_reverse(i,j,color),i,j]) に変更
              A.append([board.put_and_reverse(i,j,color),i,j])
              A.sort()
              return (A[0][1],A[0][2])
