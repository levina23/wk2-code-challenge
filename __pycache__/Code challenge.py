class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.__class__.all_reviews.append(self)

    def get_rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.all_reviews

    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant


class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.__class__.all_customers.append(self)

    def get_given_name(self):
        return self.given_name

    def get_family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def reviewed_restaurants(self):
        reviewed_restaurants = []
        for review in Review.all():
            if review.get_customer() == self:
                reviewed_restaurants.append(review.get_restaurant())
        return list(set(reviewed_restaurants))

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        return new_review


class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.__class__.all_restaurants.append(self)

    def get_name(self):
        return self.name

    def __str__(self):  # Added the __str__ method to provide a more meaningful string representation
        return self.get_name()

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def reviews(self):
        restaurant_reviews = []
        for review in Review.all():
            if review.get_restaurant() == self:
                restaurant_reviews.append(review)
        return restaurant_reviews

    def customers(self):
        reviewing_customers = []
        for review in Review.all():
            if review.get_restaurant() == self:
                reviewing_customers.append(review.get_customer())
        return list(set(reviewing_customers))

    def average_star_rating(self):
        total_ratings = 0
        num_ratings = 0
        for review in self.reviews():
            total_ratings += review.get_rating()
            num_ratings += 1
        if num_ratings > 0:
            return total_ratings / num_ratings
        return 0

    @classmethod
    def find_by_name(cls, name):
        for restaurant in cls.all():
            if restaurant.get_name() == name:
                return restaurant
        return None

# Create sample instances for testing
customer1 = Customer("John", "Doe")
restaurant1 = Restaurant("Burger King")
review1 = Review(customer1, restaurant1, 4)

# Test the methods
print(customer1.get_given_name())
print(customer1.get_family_name())
print(customer1.full_name())
print(restaurant1.get_name())
print(review1.get_rating())
print([review.get_restaurant().get_name() for review in Review.all()])
print(review1.get_customer().full_name())
print(review1.get_restaurant().get_name())
print([review.get_rating() for review in restaurant1.reviews()])
print([customer.full_name() for customer in restaurant1.customers()])
print(restaurant1.average_star_rating())
print(Restaurant.find_by_name("Burger King"))
print(restaurant1)  # This should now display the restaurant name instead of the memory address

