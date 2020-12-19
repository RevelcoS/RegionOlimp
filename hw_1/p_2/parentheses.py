class Parantheses:

    def __init__(self, n):
        self.n = n
        self.res = []
        self.recur_parantheses()

    def recur_parantheses(self, opening=0, closing=0, temp=''):
        for bracket in "()":
            if bracket == "(":
                if opening < self.n:
                    self.recur_parantheses(opening=opening+1, closing=closing, temp=temp+'(')
            elif bracket == ")":
                if closing < opening:
                    self.recur_parantheses(opening=opening, closing=closing+1, temp=temp+')')
                elif opening == self.n:
                    self.res.append(temp)
    
    def __iter__(self):
        return iter(self.res)

def parantheses(n):
    return list(Parantheses(n))