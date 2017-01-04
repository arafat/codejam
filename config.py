"""Project configurations.

Everything we need to configure at the project.
"""

import os

# Set project root directory.
# Use this env variable while defining relative urls in project.
os.environ['PROJECT_ROOT_DIR'] = os.path.dirname(os.path.abspath(__file__))

def GetProjectRootDir():
  """Gets root directory path for the project."""
  return os.environ['PROJECT_ROOT_DIR']
