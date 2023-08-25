class Process:
    def __init__(self, pid, process_name, start_time, priority):
        self.pid = pid
        self.process_name = process_name
        self.start_time = start_time
        self.priority = priority

class FlightTable:
    def __init__(self):
        self.processes = []
    
    def add_process(self, process):
        self.processes.append(process)
    
    def sort_by_pid(self):
        n = len(self.processes)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.processes[j].pid > self.processes[j + 1].pid:
                    self.processes[j], self.processes[j + 1] = self.processes[j + 1], self.processes[j]
    
    def sort_by_start_time(self):
        n = len(self.processes)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.processes[j].start_time > self.processes[j + 1].start_time:
                    self.processes[j], self.processes[j + 1] = self.processes[j + 1], self.processes[j]
    
    def sort_by_priority(self):
        priority_order = {"Low": 0, "MID": 1, "High": 2}
        n = len(self.processes)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if priority_order[self.processes[j].priority] > priority_order[self.processes[j + 1].priority]:
                    self.processes[j], self.processes[j + 1] = self.processes[j + 1], self.processes[j]
    
    def display_table(self):
        print("P_ID\tProcess\tStart Time\tPriority")
        for process in self.processes:
            print(f"{process.pid}\t{process.process_name}\t{process.start_time}\t{process.priority}")

if __name__ == "__main__":
    flight_table = FlightTable()
    
    flight_table.add_process(Process("P1", "VSCode", 100, "MID"))
    flight_table.add_process(Process("P23", "Eclipse", 234, "MID"))
    flight_table.add_process(Process("P93", "Chrome", 189, "High"))
    flight_table.add_process(Process("P42", "JDK", 9, "High"))
    flight_table.add_process(Process("P9", "CMD", 7, "High"))
    flight_table.add_process(Process("P87", "NotePad", 23, "Low"))
    
    print("Select a sorting parameter:")
    print("1. Sort by P_ID\n2. Sort by Start Time\n3. Sort by Priority")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        flight_table.sort_by_pid()
    elif choice == 2:
        flight_table.sort_by_start_time()
    elif choice == 3:
        flight_table.sort_by_priority()
    else:
        print("Invalid choice.")
        exit(1)
    
    flight_table.display_table()
