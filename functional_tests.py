from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/home/learn/projects/crawler/driver/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def ckeck_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 수지는 Web online에 꽤 쓸만한 To-do app이 있다는 얘기를 들었다. 그녀는 그 app의 홈페이지를 열어보았다.
        self.browser.get('http://localhost:8000')

        # 수지는 홈페이지 상단 title이 'To-do'임을 확인하였다.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 수지는 이 사이트에서 '해야할 일'을 바로 기입할 수 있었다.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a to-do item'
        )
        # 그녀는 입력 텍스트 창에 "Buy peacock feathers"(공작깃털구입)을 입력하였다. 그녀의 취미는 루어낚시이다.
        inputbox.send_keys('Buy peacock feathers')
        time.sleep(1)
        # 수지가 엔터를 누르자 페이지가 갱신되면서, "1: Buy peacock feathers"라는 항목이 to-do list에 나타난다.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.ckeck_for_row_in_list_table('1: Buy peacock feathers')
        # 페이지가 갱신되더라도 텍스트 입력창에 다른 할 일 항목을 기입할 수 있으므로, 수지는 "Use peacock feathers to make a fly"라고 입력하고 엔터를 친다.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        # 그러자 페이지가 다시 갱신되고, to-do 목록에 위 2개의 항목이 입력되다.
        self.ckeck_for_row_in_list_table('1: Buy peacock feathers')
        self.ckeck_for_row_in_list_table('2: Use peacock feathers to make a fly')
        time.sleep(1)

# 수지는 이 사이트가 그녀가 입력한 to-do 목록을 기억하고 있는지 궁금하였다. 이 사이트는 그녀의 to-do목록을 위한 고유 URL을 생성하였고 이에 대한 설명문이 있다.
        self.fail('Finish the test!')
# 수지는 위 고유 URL을 방문하여 그녀의 to-do목록을 본다.

# 수지는 이에 만족하며 잠에 들었다.

        # self.browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')