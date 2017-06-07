class GamePhase:
    phase = 1

    @classmethod
    def get_phase(self):
        return self.phase

    @classmethod
    def set_phase(self, phase):
        self.phase = phase