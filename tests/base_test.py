import time
import pytest
import pages



class TestFooter:
    def test_user_should_be_able_to_open_popup_select_subscription_plan(self,page):
        pages.index_page.open_index_page(page)
        time.sleep(10) # заставляет автотест 10 секунд просто ждать.
