from bs4 import BeautifulSoup as bs
import requests
class GithubUserScraping():
	"""docstring for GithubUserScraping"""
	BASE_URL = "https://github.com/"

	def __init__(self,cls, *arg):
		self.username = cls
		self.url = f"{self.BASE_URL}{self.username}"
		self.response = self._request(self.url)
		self.soup = bs(self.response.content,'html.parser')
	
	def get_profile_image(self):
		"""
			get_profile_image return string with src from img avatar
		"""
		profile_image = self.soup.find('img',{'alt':'Avatar'})['src']
		return profile_image
	
	def get_profile_bio(self):
		"""
			get_profile_bio return dict with follower,following adn starts from github user
		"""
		divs = self.soup.findAll('div',{'class':'flex-order-1 flex-md-order-none mt-2 mt-md-0'})
		profile_bio = {}
		for div in divs:
			links = div.findAll('a',{'class':'Link--secondary no-underline no-wrap'})
			for link in links:
				spans = link.findAll('span',{'class':'text-bold color-text-primary'})

				for span in spans:
					span_text = span.text.strip()
					title = "stars" if link.text.strip()[len(span_text):].strip(' \t\n\r') == '' \
								else link.text.strip()[len(span_text):].strip(' \t\n\r')
					profile_bio[title] = span_text
			
		return profile_bio

	def get_vcard_names(self):
		"""
			get_vcard_names return dict with name and username from github user
		"""
		h1 = self.soup.findAll('h1',{'class':'vcard-names'})
		names = {}
		titles = ['fullname','username']
		for element in h1:
			spans = element.findAll('span')
			for index,span in enumerate(spans):
				text = span.text.strip().strip(' \t\n\r')
				names[titles[index]] = text
		return names	
	
	def get_nav_body(self):
		"""
			get_nav_body return dict with number repositories, Project and Packages from github user
		"""
		nav = self.soup.find('nav',{'class':'UnderlineNav-body'})
		links = nav.find_all('a')
		user_nav_body = {}
		for element in links[1:len(links) - 1]:
			span = element.text.strip().strip('\t\n\r').split()
			user_nav_body[span[0]] = span[1]
		return user_nav_body	
	
	def last_contributions(self):
		"""
			last_contributions return string with last contribution sentence from github user
		"""
		h2 = self.soup.find('h2',{'class':'f4 text-normal mb-2'})
		contribution = h2.text.strip().split()
		return contribution[0]

	def get_status_code(self):
		"""
			get_status_code return status code
		"""
		return self.response.status_code
		
	def _request(self,url):
		"""
			_request return response
		"""
		return requests.get(url)

