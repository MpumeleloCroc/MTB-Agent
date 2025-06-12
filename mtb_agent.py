import random

TRAILS = [
    {"name": "Modderfontein Reserve", "level": "beginner", "distance_km": [10, 17, 40]},
    {"name": "Northern Farm", "level": "all", "distance_km": [22, 34, 62]},
    {"name": "Alberts Farm Conservancy", "level": "intermediate", "distance_km": [5, 10]},
    {"name": "Braamfontein Spruit", "level": "all", "distance_km": [8, 17]},
    {"name": "Thaba Trails", "level": "advanced", "distance_km": [10, 25]}
]

class MTBAgent:
    def __init__(self, user_level="beginner"):
        self.user_level = user_level
        self.rides = []

    def recommend_trails(self):
        return [trail for trail in TRAILS if self.user_level in trail["level"] or trail["level"] == "all"]

    def suggest_training_plan(self, rides_per_week=3):
        plan = []
        trails = self.recommend_trails()
        for _ in range(rides_per_week):
            trail = random.choice(trails)
            distance = random.choice(trail["distance_km"])
            plan.append(f"Ride {distance}km at {trail['name']}")
        return plan

    def track_ride(self, trail_name, distance, time_minutes):
        self.rides.append({"trail": trail_name, "distance": distance, "time": time_minutes})

    def summarize_progress(self):
        total_km = sum(ride["distance"] for ride in self.rides)
        return f"You've ridden {total_km}km in total!"

# Example usage:
if __name__ == "__main__":
    agent = MTBAgent(user_level="beginner")
    print("Recommended trails:", agent.recommend_trails())
    print("Training plan:", agent.suggest_training_plan())
    agent.track_ride("Modderfontein Reserve", 10, 45)
    print(agent.summarize_progress())