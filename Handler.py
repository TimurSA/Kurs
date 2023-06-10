class EventHandler:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def process_events(self):
        print(f"{self.name} is processing events:")
        for event in self.events:
            print(f"{self.name} is processing event: {event}")
        print()

    def clear_events(self):
        self.events = []


class EventController:
    def __init__(self):
        self.handler1 = EventHandler("Handler 1")
        self.handler2 = EventHandler("Handler 2")
        self.all_events = []

    def add_event(self, event):
        self.all_events.append(event)

    def process_events(self):
        for event in self.all_events:
            if event in self.handler1.events:
                self.handler1.process_events()
            elif event in self.handler2.events:
                self.handler2.process_events()

    def clear_events(self):
        self.handler1.clear_events()
        self.handler2.clear_events()
        self.all_events = []


# Пример использования
events = ["Event 1", "Event 2", "Event 3", "Event 4", "Event 5", "Event 6"]

controller = EventController()
for event in events:
    controller.add_event(event)

controller.process_events()

controller.clear_events()

new_events = ["Event 3", "Event 4", "Event 7", "Event 8", "Event 9"]

for event in new_events:
    controller.add_event(event)

controller.process_events()
