import os
import allure


class ScreenshotHelper:

    @staticmethod
    def take_screenshot(driver, scenario_name):
        screenshot_path = f"./allure-screenshot/{scenario_name.replace(' ', '_')}.png"

        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        driver.save_screenshot(screenshot_path)

        with open(screenshot_path, "rb") as f:
            allure.attach(f.read(), name=f"Screenshot for {scenario_name}", attachment_type=allure.attachment_type.PNG)
