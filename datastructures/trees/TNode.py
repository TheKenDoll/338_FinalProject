


class TNode:
    def __init__(self, data, balance, P, L, R) -> None:
        self.data = data
        self.balance = balance
        self.P = P
        self.L = L
        self.R = R

    def setData(self, data):
        self.data = data

    def setBalance(self, balance):
        self.balance = balance

    def setP(self, P):
        self.P = P

    def setL(self, L):
        self.L = L

    def setR(self, R):
        self.R = R

    def getData(self):
        return self.data
        
    def getBalance(self):
        return self.balance
    
    def getP(self):
        return self.P
    
    def getL(self):
        return self.L
    
    def getR(self):
        return self.R

    def print(self):
        return f"P: {self.P}, L: {self.L}, R: {self.R}"
    
    def toString(self):
        return str(self.data)