from datetime import datetime

class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority

    def is_overdue(self):
        return self.due_date < datetime.now()


class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_sorted_tasks(self):
        return sorted(self.tasks, key=lambda t: t.due_date)

    def get_overdue_tasks(self):
        return [t for t in self.tasks if t.is_overdue()]

    def display_tasks(self):
        print("\n--- Task List ---")
        for task in self.get_sorted_tasks():
            status = "Overdue" if task.is_overdue() else "Pending"
            print(task.name, "-", task.due_date.date(), "-", task.priority, "-", status)


def main():
    scheduler = TaskScheduler()

    scheduler.add_task(Task("Finish Project", "2026-05-20", "High"))
    scheduler.add_task(Task("Study SQL", "2026-06-05", "Medium"))
    scheduler.add_task(Task("Practice Python", "2026-05-10", "High"))

    scheduler.display_tasks()

    print("\nOverdue Tasks:")
    for task in scheduler.get_overdue_tasks():
        print(task.name)


main()