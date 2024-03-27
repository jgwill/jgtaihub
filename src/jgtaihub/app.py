#!/bin/python3

import os
from dotenv import load_dotenv
from ui import UI
from api import API
import requests
import sys
from PyQt5.QtWidgets import QApplication  # Import QApplication

def main():
  # Initialize API and UI
  api = API()
  app = QApplication(sys.argv)
  ui = UI(api)
  ui.run()

if __name__ == "__main__":
  main()

