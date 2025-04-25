# fconfig/settings.py

# Path to the trained model
MODEL_PATH = "/path/to/spam_call_detection_model.pkl"

# Threshold for spam call detection (e.g., confidence score)
SPAM_THRESHOLD = 0.75

# List of features used by the model (adjust as per your model)
FEATURES = [
    'caller_id', 'call_duration', 'call_time', 'call_frequency', 'previous_spam_flag'
]

# Logging settings
LOGGING_ENABLED = True
LOG_FILE_PATH = "/path/to/logs/spam_detection.log"

# Database connection settings (if applicable)
DATABASE_URI = "sqlite:///spam_detection.db"

# Timeout settings for API requests or processing
CALL_TIMEOUT = 30  # in seconds
