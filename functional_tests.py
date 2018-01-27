from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/home/learn/projects/crawler/driver/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 수지는 Web online에 꽤 쓸만한 To-do app이 있다는 얘기를 들었다. 그녀는 그 app의 홈페이지를 열어보았다.
        self.browser.get('http://localhost:8000')

        # 수지는 홈페이지 상단 title이 'To-do'임을 확인하였다.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


# 수지는 이 사이트에서 '해야할 일'을 바로 기입할 수 있었다.
# 그녀는 입력 텍스트 창에 "Buy peacock feathers"(공작깃털구입)을 입력하였다. 그녀의 취미는 루어낚시이다.

# 수지가 엔터를 누르자 페이지가 갱신되면서, "1: Buy peacock feathers"라는 항목이 to-do list에 나타난다.

# 페이지가 갱신되더라도 텍스트 입력창에 다른 할 일 항목을 기입할 수 있으므로, 수지는 "Use peacock feathers to make a fly"라고 입력하고 엔터를 친다.

# 그러자 페이지가 다시 갱신되고, to-do 목록에 위 2개의 항목이 입력되다.

# 수지는 이 사이트가 그녀가 입력한 to-do 목록을 기억하고 있는지 궁금하였다. 이 사이트는 그녀의 to-do목록을 위한 고유 URL을 생성하였고 이에 대한 설명문이 있다.

# 수지는 위 고유 URL을 방문하여 그녀의 to-do목록을 본다.

# 수지는 이에 만족하며 잠에 들었다.

browser.quit()