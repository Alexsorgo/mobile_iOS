import requests
from appium.webdriver.common.touch_action import TouchAction

from configs import config


class Element(object):
    def __init__(self, driver):
        self.driver = driver

    def tap_btn(self, el_name):
        cnt = center(self.driver.find_element(*el_name))
        action = TouchAction(self.driver)
        action.press(x=(cnt['XCentr']), y=(cnt['YCentr'])).release().perform()

    def tap_btn_by_id(self, locator):
        cnt = center(self.driver.find_element_by_id(locator))
        action = TouchAction(self.driver)
        action.press(x=(cnt['XCentr']), y=(cnt['YCentr'])).release().perform()

    def click_btn(self, el_name):
        element = self.driver.find_element(*el_name)
        element.click()

    def set_text(self, el_name, txt):
        element = self.driver.find_element(*el_name)
        element.send_keys(txt)

    def set_text_clear(self, el_name, txt):
        element = self.driver.find_element(*el_name)
        element.clear()
        element.send_keys(txt)

    def tap_element(self, el):
        cnt = center(el)
        action = TouchAction(self.driver)
        action.press(x=(cnt['XCentr']), y=(cnt['YCentr'])).release().perform()


def center(el):
    XCentr = float(el.location['x']) + el.size['width'] / float(2)
    YCentr = float(el.location['y']) + el.size['height'] / float(2)
    return {'XCentr': int(XCentr), 'YCentr': int(YCentr)}


def proportion(x, y, newX, newY):
    fullX = float(414)
    fullY = float(736)
    propX = float(x / fullX)
    propY = float(y / fullY)
    newX = newX * propX
    newY = newY * propY
    return {'x': int(newX), 'y': int(newY)}


# send request for REST API
def sms_check(number):
    req = config.HOST + ":" + config.PORT + "/sessions?phone=380" + str(number)
    r = requests.get(req)
    text = r.content
    try:
        sms = next(i for i in eval(text) if i['type'] == 'reg')['sms_code']
    except SyntaxError:
        raise ValueError
    return sms


def gallery_photo(driver):
    driver.find_element_by_id('Моменты').click()
    action = TouchAction(driver)
    # moments = proportion(180, 100, driver.get_window_size()['width'], driver.get_window_size()['height'])
    # action.press(x=moments['x'], y=moments['y']).release().perform()
    photo_select = proportion(50, 642, driver.get_window_size()['width'], driver.get_window_size()['height'])
    action.press(x=photo_select['x'], y=photo_select['y']).release().perform()
