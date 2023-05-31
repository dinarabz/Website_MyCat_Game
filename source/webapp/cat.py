from random import randint


class Cat:
    name = 'Cat'
    age = randint(0, 13)
    health = 30
    happiness = 10
    satiety = 10
    sleep = 'off'

    @staticmethod
    def update_name(request):
        name = request.POST.get('name')
        if name:
            Cat.name = name

    @staticmethod
    def apply_action(request):
        action = request.POST.get('action')

        if action == 'play':
            Cat.play_pet()
        elif action == 'feed':
            Cat.feed_pet()
        elif action == 'sleep':
            Cat.sleep_pet()
        elif action == 'visit_vet':
            Cat.visit_vet()
        else:
            pass

        if Cat.happiness < 0:
            Cat.happiness = 0

        if Cat.satiety < 0:
            Cat.satiety = 0

        if Cat.health == 0:
            Cat.happiness = 0

    @classmethod
    def feed_pet(cls):
        if cls.sleep == 'on':
            return

        if cls.satiety > 100:
            cls.satiety = 100
            cls.happiness -= 30
            return

        cls.satiety += 15
        cls.happiness += 5

    @classmethod
    def play_pet(cls):
        cls.satiety -= 10

        if cls.sleep == 'on':
            cls.sleep = 'off'
            cls.happiness -= 5
        else:
            cls.happiness += 10

        chance = randint(1, 3)
        if chance == 3:
            cls.happiness = 0
            cls.health = 5
            return

    @classmethod
    def sleep_pet(cls):
        cls.sleep = 'on'
        cls.happiness += 10
        cls.satiety -= 5

    @classmethod
    def visit_vet(cls):
        cls.happiness -= 10
        cls.health += 15
        cls.satiety -= 10
