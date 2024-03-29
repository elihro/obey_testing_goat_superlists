from .base import FuncionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip
import time


class ItemValidationTest(FuncionalTest):

	def get_error_element(self):
		return self.browser.find_element_by_css_selector('.has-error')

	def test_cannot_add_empty_list_items(self):
		# Edith goes to the home page and accidentally tries to submit
		# an empty list item. She hits Enter on the empty input box
		self.browser.get(self.live_server_url)
		self.get_item_input_box().send_keys(Keys.ENTER)
		
		# The browser intercepts the request, and does not load the
		# list page
		self.wait_for(lambda: self.browser.find_element_by_css_selector (
			'#id_text:invalid'
		))
		
		# She starts typing some text for the new item and the error disappears
		self.get_item_input_box().send_keys('Buy milk')
		self.wait_for(lambda: self.browser.find_element_by_css_selector(
			'#id_text:valid'
		))
		
		# And she can submit it successfully
		self.get_item_input_box().send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy milk')
				
		# Perversely, she now decides to submit a second blank list item
		self.get_item_input_box().send_keys(Keys.ENTER)
		
		# Again, the browser will not comply
		self.wait_for_row_in_list_table('1: Buy milk')
		self.wait_for(lambda: self.browser.find_element_by_css_selector(
			'#id_text:invalid'
		))
		
		# And she can correct it by filling some text in
		inputbox = self.get_item_input_box()
		inputbox.send_keys('Make tea')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for(lambda: self.browser.find_element_by_css_selector(
			'#id_text:valid'
		))
		self.wait_for_row_in_list_table('1: Buy milk')
		self.wait_for_row_in_list_table('2: Make tea')

	def test_cannot_add_duplicate_items(self):
		# Edith goes to the home page and starts a new list
		self.browser.get(self.live_server_url)
		self.get_item_input_box().send_keys('Buy wellies')
		self.get_item_input_box().send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy wellies')
		
		# She accidentally tries to enter a duplicate item
		self.get_item_input_box().send_keys('Buy wellies')
		self.get_item_input_box().send_keys(Keys.ENTER)
		
		# She sees a helpful error message
		self.wait_for(lambda: self.assertEqual (
			self.get_error_element().text,
			"You've already got this in your list"
		))
		
	
	def test_error_message_are_cleaned_on_input_when_keypress(self):
		# Edith starts a list and causes a validation error.
		self.browser.get(self.live_server_url)
		self.get_item_input_box().send_keys('Banter too thick')
		self.get_item_input_box().send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Banter too thick')
		self.get_item_input_box().send_keys('Banter too thick')
		self.get_item_input_box().send_keys(Keys.ENTER)
		
		self.wait_for(lambda: self.assertTrue(
			self.get_error_element().is_displayed()
		))
		
		# She starts typing in the input box to clear the error
		self.get_item_input_box().send_keys('a')
		
		# She is pleased to see that error message disappears
		self.wait_for(lambda: self.assertFalse(
			self.get_error_element().is_displayed()
		))

	def test_error_message_are_cleaned_on_input_when_click(self):
		# Edith starts a list and causes a validation error.
		self.browser.get(self.live_server_url)
		self.get_item_input_box().send_keys('Banter too thick')
		self.get_item_input_box().send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Banter too thick')
		self.get_item_input_box().send_keys('Banter too thick')
		self.get_item_input_box().send_keys(Keys.ENTER)
		
		self.wait_for(lambda: self.assertTrue(
			self.get_error_element().is_displayed()
		))
		
		# She clicks the input box to clear the error
		self.get_item_input_box().click()
		
		# She is pleased to see that error message disappears
		self.wait_for(lambda: self.assertFalse(
			self.get_error_element().is_displayed()
		))

