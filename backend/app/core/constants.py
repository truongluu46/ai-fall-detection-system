from enum import Enum


class UserRole(Enum):
    ADMIN = "admin"
    OPERATOR = "operator"
    REVIEWER = "reviewer"


class CameraSourceType(Enum):
    RTSP = "rtsp"
    VIDEO_FILE = "video_file"
    WEBCAM = "webcam"


class CameraStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    ERROR = "error"


class ProcessingRunStatus(Enum):
    QUEUED = "queued"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class FallEventStatus(Enum):
    NEW = "new"
    REVIEWED = "reviewed"
    FALSE_ALARM = "false_alarm"
    CONFIRMED = "confirmed"


class NotificationChannel(Enum):
    DASHBOARD = "dashboard"
    EMAIL = "email"
    TELEGRAM = "telegram"


class NotificationSendStatus(Enum):
    PENDING = "pending"
    SENT = "sent"
    FAILED = "failed"
