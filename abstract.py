class Observer:
    def handle_event(self, lottery_number: int):
        pass


class Observed:
    def add_observer(self, player):
        pass

    def remove_observer(self, player):
        pass

    def notify_observers(self, lottery_number: int):
        pass
