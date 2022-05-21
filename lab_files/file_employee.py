class Employees():

    
    def __init__(self, file_name=None):
        self.default_db_file = 'employees.txt'
        self.file_name = file_name
    
    def save(self, name):
        file_name = self.file_name if self.file_name else self.default_db_file
        my_file = open(file_name, 'a')
        my_file.write(f"{name}\n")
        my_file.close()

    def get_all(self):
        file_name = self.file_name if self.file_name else self.default_db_file
        my_file = open(file_name, 'r')
        data = my_file.read()
        return data
    
    def get_at_line(self, number_line):
        data = self.get_all()
        employees = [emp for emp in data.split("\n")]
        return employees[number_line-1]
        