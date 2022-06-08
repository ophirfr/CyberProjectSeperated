
class UI_State():
    STATE_NO_TOKEN = 0
    STATE_VALID_TOKEN = 1
    STATE_EXIT_APP = 2

    def __init__(self):
        self.State = self.STATE_NO_TOKEN

    def GetState(self):
        return self.State

    def SetState(self,s):
        t = self.State
        self.State =s
        return t;
