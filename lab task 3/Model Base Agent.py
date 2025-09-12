class Model_Based_Agent:
    def __init__(self, temp, filename="temp history.txt"):
        self.fixed_temp = temp
        self.filename = filename
        open(self.filename, "a").close()
        
    def senser(self, temp, room_name=""):
        self.current_temp = temp
        self.current_room = room_name
        with open(self.filename, "a") as f:
            f.write(f"{room_name}: {temp}\n")
        
    def performance(self):
        with open(self.filename, "r") as f:
            lines = f.read().strip().split("\n")
        
        for line in lines:
            if str(self.current_temp) in line:   # agar temp match mil gaya
                if self.current_temp > self.fixed_temp:
                    return "(History) Turn ON the AC"
                else:
                    return "(History) Turn OFF the AC"
        
        if self.current_temp > self.fixed_temp:
            return "Turn ON the AC"
        else:
            return "Turn OFF the AC"
    
    def actuator(self, room_name=""):
        action = self.performance()
        print(f"{room_name} {self.current_temp} => Action: {action}")

        print("History so far:")
        with open(self.filename, "r") as f:
            history = f.read().strip().split("\n")
            print(history)
        print("-" * 40)


rooms = {
    "Living room": 11,
    "Drawing room": 24,
    "Bed Room": 22
}

agent = Model_Based_Agent(16)

for room, temp in rooms.items():
    agent.senser(temp, room)
    agent.actuator(room)

agent.senser(22, "Guest Room")
agent.actuator("Guest Room")
