import csv
import datetime
from project import Project


def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Skip the header
        for row in reader:
            if row:
                name, start_date, priority, cost_estimate, completion = row
                project = Project(name, start_date, priority, cost_estimate, completion)
                projects.append(project)
    return projects


def save_projects(filename, projects):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['Name', 'Start Date', 'Priority', 'Cost Estimate', 'Completion'])
        for project in projects:
            writer.writerow([project.name, project.start_date.strftime('%d/%m/%Y'),
                             project.priority, f"${project.cost_estimate:.2f}", project.completion])


def display_projects(projects):
    incomplete = [p for p in projects if not p.is_completed()]
    completed = [p for p in projects if p.is_completed()]

    print("Incomplete projects:")
    for p in sorted(incomplete):
        print(p)

    print("\nCompleted projects:")
    for p in sorted(completed):
        print(p)


def filter_projects_by_date(projects, date):
    date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    filtered_projects = [p for p in projects if p.start_date > date]
    return filtered_projects


def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion = input("Percent complete: ")
    project = Project(name, start_date, priority, cost_estimate, completion)
    projects.append(project)


def update_project(projects):
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    index = int(input("Choose project number to update: "))
    project = projects[index]
    new_completion = input(f"New completion for {project.name} (leave blank to keep current): ")
    if new_completion:
        project.update_completion(int(new_completion))
    new_priority = input(f"New priority for {project.name} (leave blank to keep current): ")
    if new_priority:
        project.update_priority(int(new_priority))


def main():
    filename = 'projects.txt'
    projects = load_projects(filename)

    while True:
        choice = input("\nChoose an option:\n"
                       "(L)oad projects\n"
                       "(S)ave projects\n"
                       "(D)isplay projects\n"
                       "(F)ilter projects by date\n"
                       "(A)dd new project\n"
                       "(U)pdate project\n"
                       "(Q)uit\n"
                       ">>> ").upper()
        if choice == 'L':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            date_str = input("Enter date (dd/mm/yyyy): ")
            filtered_projects = filter_projects_by_date(projects, date_str)
            display_projects(filtered_projects)
        elif choice == 'A':
            add_project(projects)
        elif choice == 'U':
            update_project(projects)
        elif choice == 'Q':
            if input("Save changes before quitting? (y/n): ").lower() == 'y':
                filename = input("Enter filename to save: ")
                save_projects(filename, projects)


if __name__ == "__main__":
    main()
