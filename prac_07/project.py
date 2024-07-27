import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate.strip('$'))
        self.completion = int(completion)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def is_completed(self):
        return self.completion == 100

    def update_completion(self, new_completion):
        self.completion = new_completion

    def update_priority(self, new_priority):
        self.priority = new_priority
