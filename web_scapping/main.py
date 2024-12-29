import schedule
import time
import pyautogui
import keyboard
import logging
import json

# Logging configuration
logging.basicConfig(filename='task_automator.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def automate_task(config):
    try:
        logging.info('Automation started')
        pyautogui.alert('Automation started')
        
        # Conditional statement
        if config['condition']:
            pyautogui.alert('Condition met')
        
        # Loop
        for i in range(config['loop']):
            pyautogui.typewrite(f'Iteration {i+1}')
        
        # Custom function
        custom_function(config['message'])
        
        pyautogui.alert('Automation completed')
        logging.info('Automation completed')
    except Exception as e:
        logging.error(f'Automation error: {e}')

def custom_function(message):
    pyautogui.alert(message)

def schedule_task(config):
    schedule.every(config['interval']).minutes.do(lambda: automate_task(config))

def main():
    config_filename = 'task_config.json'
    config = load_config(config_filename)
    schedule_task(config)
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except Exception as e:
            logging.error(f'Scheduling error: {e}')

if __name__ == "__main__":
    main()