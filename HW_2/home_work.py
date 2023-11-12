from random import choice
from abc import ABC, abstractmethod


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass

    def open_reward(self):
        self.game_item = self.create_item()
        self.game_item.open()


class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


class GoldReward(IGameItem):
    def open(self):
        print('Gold')


class GoldGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return GoldReward()


class GemReward(IGameItem):
    def open(self):
        print('Gem')


class GemGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return GemReward()


"""New items"""
class SilverReward(IGameItem):
    def open(self):
        print('Silver')


class SilverGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return SilverReward()


class GunReward(IGameItem):
    def open(self):
        print('Gun')


class GunGeneration(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return GunReward()


# ДЗ. Добавить новые предметы. Сундуки с новыми предметами.

if __name__ == '__main__':
    # gold_generator = GoldGenerator()
    # gold_generator.open_reward()
    lst = [GoldGenerator(), GemGenerator(), SilverGenerator(), GunGeneration()]
    for i in range(20):
        choice(lst).open_reward()
