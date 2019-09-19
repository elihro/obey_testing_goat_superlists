from .base import FuncionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip
import time


class ItemValidationTest(FuncionalTest):

	def test_cannot_add_empty_list_items(self):
		# Edith goes to the home page and accidentally tries to submit
		# an empty list item. She hits Enter on the empty input box
		self.browser.get(self.live_server_url)
		inputbox = self.browser.find_element_by_id('id_text')
		inputbox.send_keys(Keys.ENTER)
		
		# The browser intercepts the request, and does not load the
		# list page
		self.wait_for(lambda: self.browser.find_element_by_css_selector (
			'#id_text:invalid'
		))
		
		# She starts typing some text for the new item and the error disappears
		inputbox = self.browser.find_element_by_id('id_text')
		inputbox.send_keys('Buy milk')
		self.wait_for(lambda: self.browser.find_element_by_css_selector(
			'#id_text:valid'
		))
		
		# And she can submit it successfully
		inputbox = self.browser.find_element_by_id('id_text')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy milk')
				
		# Perversely, she now decides to submit a second blank list item
		self.browser.find_element_by_id('id_text').send_keys(Keys.ENTER)
		
		# Again, the browser will not comply
		self.wait_for_row_in_list_table('1: Buy milk')
		self.wait_for(lambda: self.browser.find_element_by_css_selector(
			'#id_text:invalid'
		))
		
		# And she can correct it by filling some text in
		inputbox = self.browser.find_element_by_id('id_text')
		inputbox.send_keys('Make tea')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for(lambda: self.browser.find_element_by_css_selector(
			'#id_text:valid'
		))
		self.wait_for_row_in_list_table('1: Buy milk')
		self.wait_for_row_in_list_table('2: Make tea')
