CREATE TABLE student_stats (
    student_id TEXT PRIMARY KEY,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    academic_level TEXT NOT NULL,
    study_hours REAL NOT NULL,
    self_study_hours REAL NOT NULL,
    online_classes_hours REAL NOT NULL,
    social_media_hours REAL NOT NULL,
    gaming_hours REAL NOT NULL,
    sleep_hours REAL NOT NULL
);