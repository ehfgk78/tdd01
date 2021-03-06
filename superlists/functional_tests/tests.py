from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/home/learn/projects/crawler/driver/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

#     def test_can_start_a_list_for_one_user(self):
#         # 수지는 Web online에 꽤 쓸만한 To-do app이 있다는 얘기를 들었다. 그녀는 그 app의 홈페이지를 열어보았다.
#         # self.browser.get('http://localhost:8000')
#         self.browser.get(self.live_server_url)
#
#         # 수지는 홈페이지 상단 title이 'To-do'임을 확인하였다.
#         self.assertIn('To-Do', self.browser.title)
#         header_text = self.browser.find_element_by_tag_name('h1').text
#         self.assertIn('To-Do', header_text)
#
#         # 수지는 이 사이트에서 '해야할 일'을 바로 기입할 수 있었다.
#         inputbox = self.browser.find_element_by_id('id_new_item')
#         self.assertEqual(
#             inputbox.get_attribute('placeholder'), 'Enter a to-do item'
#         )
#         # 그녀는 입력 텍스트 창에 "Buy peacock feathers"(공작깃털구입)을 입력하였다. 그녀의 취미는 루어낚시이다.
#         inputbox.send_keys('Buy peacock feathers')
#
#         # 수지가 엔터를 누르자 페이지가 갱신되면서, "1: Buy peacock feathers"라는 항목이 to-do list에 나타난다.
#         inputbox.send_keys(Keys.ENTER)
#
#         self.wait_for_row_in_list_table('1: Buy peacock feathers')
#         # 페이지가 갱신되더라도 텍스트 입력창에 다른 할 일 항목을 기입할 수 있으므로, 수지는 "Use peacock feathers to make a fly"라고 입력하고 엔터를 친다.
#         inputbox = self.browser.find_element_by_id('id_new_item')
#         inputbox.send_keys('Use peacock feathers to make a fly')
#         inputbox.send_keys(Keys.ENTER)
#
#         # 그러자 페이지가 다시 갱신되고, to-do 목록에 위 2개의 항목이 입력되다.
#         self.wait_for_row_in_list_table('1: Buy peacock feathers')
#         self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
#
# # 수지는 이 사이트가 그녀가 입력한 to-do 목록을 기억하고 있는지 궁금하였다. 이 사이트는 그녀의 to-do목록을 위한 고유 URL을 생성하였고 이에 대한 설명문이 있다.
#
# # 수지는 위 고유 URL을 방문하여 그녀의 to-do목록을 본다.
#
# # 수지는 이에 만족하며 잠에 들었다.
#
#         # self.browser.quit()
#
#     def test_multiple_users_can_start_lists_at_different_urls(self):
#         # 수지는 새로운 to-do list를 시작한다.
#         self.browser.get(self.live_server_url)
#         inputbox = self.browser.find_element_by_id('id_new_item')
#         inputbox.send_keys('Buy peacock feathers')
#         inputbox.send_keys(Keys.ENTER)
#         self.wait_for_row_in_list_table('1: Buy peacock feathers')
#         # 수지는 그녀의 리스트에 유일한 URL이 있음을 확인한다.
#         soosie_list_url = self.browser.current_url
#         self.assertRegex(soosie_list_url, '/lists/.+')
#         # 새로운 사용자 길동이 이 사이트에 들어왔다.
#
#         # 우리는 수지의 정보가 cookies로 전달되지 않도록 새로운 session을 사용한다.
#         self.browser.quit()
#         self.browser = webdriver.Chrome('/home/learn/projects/crawler/driver/chromedriver')
#         # 길동은 홈페이지를 방문하자 수지의 리스트는 보이지 않는다.
#         self.browser.get(self.live_server_url)
#         page_next = self.browser.find_element_by_tag_name('body').text
#         self.assertNotIn('Buy peacock feathers', page_next)
#         self.assertNotIn('make a fly', page_next)
#         # 길동은 새로운 항목을 기입하면서 새로운 to-do list를 시작한다.
#         # 그는 수지보다 이 사이트에 관심이 덜하다
#         inputbox = self.browser.find_element_by_id('id_new_item')
#         inputbox.send_keys('Buy milk')
#         inputbox.send_keys(Keys.ENTER)
#         self.wait_for_row_in_list_table('1: Buy milk')
#         # 길동은 자신의 리스트에 대한 고유의 URL을 확인한다.
#         gilDong_list_url = self.browser.current_url
#         self.assertRegex(gilDong_list_url, '/lists/.+')
#         self.assertNotEqual(gilDong_list_url, soosie_list_url)
#         # 길동은 수지의 리스트를 볼 수 없다.
#         page_next = self.browser.find_element_by_tag_name('body').text
#         self.assertNotIn('Buy peacock feathers', page_next)
#         self.assertIn('Buy milk', page_next)
#         # 만족하고 수지와 길동은 잠에 든다.

    def test_layout_and_styling(self):
        # 수지는 홈페이지를 방문합니다.
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        # 수지는 중앙에 멋있게 위치한 입력상자를 본다.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )
        time.sleep(10)

        # 수지는 새 리스트를 시작하는데 또 입력상자가 가운데 위치한 것을 보았다.
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )
        time.sleep(10)

