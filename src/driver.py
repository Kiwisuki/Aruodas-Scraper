import logging
import time

import undetected_chromedriver as uc

from config.constants import CHROMERIVER_PATH, DATA_PATH, HEADLESS, SAVE_HTML
from src.utils import retry


class SmartDriver:
    """Driver that resets itself after a certain amount of actions or time passed."""

    def __init__(self, refresh_rate: int = 10, refresh_timer: int = 60):
        """Initialize the driver with a refresh rate and timer."""
        self.actions = 0
        self.last_refresh = time.time()
        self.refresh_rate = refresh_rate
        self.refresh_timer = refresh_timer
        self.driver = self.initialize_chromedriver()

    def get_options(self):
        """Get the options for the chromedriver."""
        options = uc.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--incognito')
        if HEADLESS:
            options.add_argument('--headless')
        return options

    def initialize_chromedriver(self):
        """Initialize the chromedriver."""
        self.last_refresh = time.time()
        return uc.Chrome(options=self.get_options(), executable_path=CHROMERIVER_PATH)

    def refresh(self):
        """Refresh the chromedriver."""
        self.driver.quit()
        self.driver = self.initialize_chromedriver()

    def increment(self):
        """Increments the actions and refreshes if needed."""
        self.actions += 1
        if (self.actions % self.refresh_rate == 0) or (
            time.time() - self.last_refresh > self.refresh_timer
        ):
            self.refresh()

    @retry()
    def get_html(self, url: str, delay: int = 2) -> str:
        """Get the html content from the url."""
        try:
            self.driver.get(url)
            time.sleep(delay)
        except Exception as exception:
            logging.error(
                f'Exception occured while getting html from {url}: {exception}, refreshing driver...'
            )
            self.refresh()
            raise exception
        html_content = self.driver.page_source
        if SAVE_HTML:
            with open(f'{DATA_PATH}/{time.time()}.html', 'w') as file:
                file.write(html_content)
        self.increment()
        return html_content
