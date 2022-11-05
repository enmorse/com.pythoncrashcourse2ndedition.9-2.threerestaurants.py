class Restaurant:

    def __init__(self, restaurant_name, cuisine_tpe):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_tpe

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f'\nThe {self.restaurant_name} is open')


def main():
    restaurant = Restaurant("Steak, Eggs, & Bitches", "Steak & Eggs")
    restaurant_one = Restaurant("Healthy Dinning", "Health Food")
    restaurant_two = Restaurant("Bodybuilding Dinning",
                                "Meeting Your Macro Needs")

    # print(restaurant.describe_restaurant())
    # print(restaurant.open_restaurant())

    # restaurant.open_restaurant()

    restaurant.describe_restaurant()
    restaurant_one.describe_restaurant()
    restaurant_two.describe_restaurant()


if __name__ == '__main__':
    main()
