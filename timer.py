import time

class Timer:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.elapsed_time = 0
    
    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        return self.elapsed_time
    
    def reset(self):
        self.start_time = 0
        self.end_time = 0
        self.elapsed_time = 0

    def __str__(self) -> str:
        return("\nTotal Elapsed Time: " + str(self.elapsed_time) + " seconds\n")

