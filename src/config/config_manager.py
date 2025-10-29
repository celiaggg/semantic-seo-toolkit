"""Configuration manager for loading and managing application settings."""

import os
import yaml
from pathlib import Path
from typing import Any, Dict, Optional
from dotenv import load_dotenv
from pydantic import BaseModel, Field


class ConfigManager:
    """Manages application configuration from environment variables and YAML files."""
    
    def __init__(self, config_path: Optional[str] = None, env_path: Optional[str] = None):
        """Initialize the configuration manager.
        
        Args:
            config_path: Path to the YAML configuration file
            env_path: Path to the .env file
        """
        self.config_path = config_path or "config.yaml"
        self.env_path = env_path or ".env"
        
        # Load environment variables
        if os.path.exists(self.env_path):
            load_dotenv(self.env_path)
        
        # Load YAML configuration
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file."""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        
        with open(self.config_path, 'r') as file:
            return yaml.safe_load(file)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value using dot notation.
        
        Args:
            key: Configuration key (e.g., 'apis.openai.model')
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def get_env(self, key: str, default: Any = None) -> Any:
        """Get an environment variable value.
        
        Args:
            key: Environment variable name
            default: Default value if not found
            
        Returns:
            Environment variable value
        """
        return os.getenv(key, default)
    
    def get_api_key(self, service: str) -> str:
        """Get API key for a specific service.
        
        Args:
            service: Service name (e.g., 'openai', 'anthropic')
            
        Returns:
            API key
            
        Raises:
            ValueError: If API key not found
        """
        key = self.get_env(f"{service.upper()}_API_KEY")
        if not key:
            raise ValueError(f"API key for {service} not found. Please set {service.upper()}_API_KEY environment variable.")
        return key