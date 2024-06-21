import selenium  
import requests

# Glolbal variables 
meals = ['Breakfast', 'Lunch', 'Dinner'] 
dining_halls = ['Thorne', 'Moulton Union', 'Moulton Express']

class Menu: 
   def __init__(self, date, meal): 
      self.date = date
      self.meal = meal
      
   @property 
   def date(self): 
      return self.date
   
   @property 
   def meal(self): 
      return self.meal 
   

   
   @date.setter
   def date(self, value): 
      if value != '2024-08-22': 
         return ValueError("Date Format must be in 'YYYY-MM-DD'")
      self.date = value
      
   @meal.setter 
   def meal(self, value): 
      if value not in meals: 
         return ValueError("Meal must be either Breakfast, Lunch, or Dinner")
      self.meal = value
      

      
   def __str__(self): 
      title = f"{self.date} {self.meal} Menu \n"
      Thorne = f"{dining_halls[0]}: \n {self.meal[0]} \n"
      Moulton = f"{dining_halls[1]}: \n {self.meal[1]} \n"
      Moulton_Express = f"{dining_halls[2]}: \n {self.meal[2]} \n"
   
      
   @staticmethod
   def menu(self, link): 
      try: 
         request = requests.Request(link)
      except: 
         return requests.HTTPError
      
      # Organize Page for meals and dining halls for specific date 
      
      
class web_scraper: 
   def __init__(self, link): 
      self.link = link
   
   @staticmethod
   def gather_data(self): 
      pass
   
   @staticmethod 
   def format_menu(self, menu):
      pass