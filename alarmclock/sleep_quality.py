from datetime import datetime, timedelta

class SleepQualityTracker:
    def __init__(self):
        self.sleep_start_time = None
        self.sleep_end_time = None

    def start_sleep_tracking(self):
        self.sleep_start_time = datetime.now()

    def end_sleep_tracking(self):
        self.sleep_end_time = datetime.now()

    def track_sleep_quality(self):
        sleep_duration = self.sleep_end_time - self.sleep_start_time
        sleep_quality_score = self.calculate_sleep_quality_score(sleep_duration)
        return sleep_quality_score

    def calculate_sleep_quality_score(self, sleep_duration):
        sleep_quality_score = 0
        if sleep_duration.total_seconds() >= 7 * 3600:  # 7+ hours
            sleep_quality_score += 30
        if sleep_duration.total_seconds() >= 5 * 3600:  # 5-7 hours
            sleep_quality_score += 20
        return sleep_quality_score