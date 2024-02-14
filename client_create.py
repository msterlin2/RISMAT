class Client:
    def __init__(self) -> None:
        
        self.p1Name = 'Bob'
        self.p1Sex = 'M'
        self.p1Age = 67
        self.p2Name = 'Sue'
        self.p2Sex = 'F'
        self.p2Age = 65
        self.Year = 2015
        self.nScenarios = 100000
        self.budget = 1000000
        self.figureSize = [700, 700] #MS changed from original Matlab Code of [1500 900]
        
def client_create():
    return Client()


