from .base import FuncionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip
import time


class ItemValidationTest(FuncionalTest):

	@skip
	def test_cannot_add_empty_list_items(self):
		# Edith goes to the home page and accidentally tries to submit
		# an empty list item. She hits Enter on the empty input box
		self.browser.get(self.live_server_url)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys(Keys.ENTER)
		
		# The home page refreshes, and there is an error message saying
		# that list items cannot be blank
		time.sleep(1)
		
		
		# She tries again with some text for the item, which now works
		
		# Perversely, she now decides to submit a second blank list item
		
		# She receives a similiar warning on the list page
		
		# And she can correct it by filling some text in
		self.fail('write me!')
