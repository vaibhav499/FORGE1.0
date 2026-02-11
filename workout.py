def get_workout_plan(goal):
    if goal == "Muscle Gain":
        return {
            "Day 1 – Chest + Triceps": [
                ("Bench Press", "4 × 8"),
                ("Incline DB Press", "3 × 10"),
                ("Tricep Pushdown", "3 × 12")
            ],
            "Day 2 – Back + Biceps": [
                ("Lat Pulldown", "4 × 10"),
                ("Barbell Curl", "3 × 10")
            ],
            "Day 3 – Legs": [
                ("Squats", "4 × 8"),
                ("Leg Press", "3 × 10")
            ]
        }

    if goal == "Fat Loss":
        return {
            "Day 1 – Full Body": [
                ("Push-ups", "3 × 15"),
                ("Squats", "4 × 12")
            ]
        }

    return {
        "Day 1 – Full Body": [
            ("Bench Press", "3 × 10"),
            ("Lat Pulldown", "3 × 10"),
            ("Squats", "3 × 10")
        ]
    }
