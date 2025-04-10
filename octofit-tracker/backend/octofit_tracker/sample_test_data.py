# Test data for populating the octofit_db database

test_data = {
    "users": [
        {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
        {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
        {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
        {"username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
        {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"}
    ],
    "teams": [
        {"name": "Team Alpha", "members": ["thundergod", "metalgeek"]},
        {"name": "Team Beta", "members": ["zerocool", "crashoverride"]},
        {"name": "Team Gamma", "members": ["sleeptoken"]}
    ],
    "activities": [
        {"user": "thundergod", "activity": "Running", "duration": 30},
        {"user": "metalgeek", "activity": "Cycling", "duration": 45},
        {"user": "zerocool", "activity": "Swimming", "duration": 60},
        {"user": "crashoverride", "activity": "Hiking", "duration": 90},
        {"user": "sleeptoken", "activity": "Yoga", "duration": 20}
    ],
    "leaderboard": [
        {"user": "thundergod", "points": 120},
        {"user": "metalgeek", "points": 110},
        {"user": "zerocool", "points": 100},
        {"user": "crashoverride", "points": 90},
        {"user": "sleeptoken", "points": 80}
    ],
    "workouts": [
        {"name": "Crossfit", "description": "Training for a crossfit competition"},
        {"name": "Running Training", "description": "Training for a marathon"},
        {"name": "Strength Training", "description": "Training for strength"},
        {"name": "Swimming Training", "description": "Training for a swimming competition"}
    ]
}