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
        {"user": "thundergod", "workout": "5k Run", "date": "2025-04-01"},
        {"user": "metalgeek", "workout": "10k Cycle", "date": "2025-04-02"},
        {"user": "zerocool", "workout": "1k Swim", "date": "2025-04-03"},
        {"user": "crashoverride", "workout": "Mountain Hike", "date": "2025-04-04"},
        {"user": "sleeptoken", "workout": "Morning Yoga", "date": "2025-04-05"}
    ]
}
