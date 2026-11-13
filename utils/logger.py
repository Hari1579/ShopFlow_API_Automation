import logging
import os

def get_logger():
    """Configures and returns a custom logger that writes to both console and a file."""
    logger = logging.getLogger("ShopFlow_API_Logger")
    
    # If the logger is already configured, don't add duplicate handlers
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        # Create a format for the logs: [2026-11-12 19:45:01] [INFO] - Message
        formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        
        # 1. Console Handler (so we can still see it in the terminal)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # 2. File Handler (so it saves to a file for CI/CD)
        # We save the log file in the root directory
        file_handler = logging.FileHandler("automation.log", mode='a')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
    return logger

# Create a global instance to be used across the framework
log = get_logger()