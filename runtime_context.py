class RuntimeContext:
    def __init__(self, data_filename):
        self.memory = {}
        self.initialized = set()
        self.data = []
        self.data_index = 0
        
        with open(data_filename, "r") as f:
            for line in f:
                line = line.strip()
                if line != "":
                    self.data.append(int(line))
    
    def set_value(self, name, value):
        self.memory[name] = value
        self.initialized.add(name)

    def get_value(self, name):
        if name not in self.initialized:
            raise Exception(f"Variable {name} has not been initialized")
        return self.memory[name]
    
    def read_next(self):
        if self.data_index >= len(self.data):
            raise Exception("No more input data available")
        value = self.data[self.data_index]
        self.data_index += 1
        return value