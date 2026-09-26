import os
from dataclasses import dataclass


@dataclass
class DesktopAgentConfig:
    polling_interval_seconds: int = 2
    max_event_buffer_size: int = 500
    log_level: str = "INFO"
    app_data_dir: str = os.path.join(os.path.expanduser("~"), ".workflowos")


DEFAULT_CONFIG = DesktopAgentConfig()
