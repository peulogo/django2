from task1.models import Buyer, Game


buyer1 = Buyer.objects.create(name="Ilya", balance=1500.0, age=24)
buyer2 = Buyer.objects.create(name="Terminator2000", balance=42.0, age=52)
buyer3 = Buyer.objects.create(name="Ubivator432", balance=0.5, age=16)


game1 = Game.objects.create(
    title="Cyberpunk 2077",
    cost=31.0,
    size=46.2,
    description="Game of the year",
    age_limited=True
)

game2 = Game.objects.create(
    title="Mario",
    cost=5.0,
    size=0.5,
    description="Old Game",
    age_limited=False
)

game3 = Game.objects.create(
    title="Hitman",
    cost=12.0,
    size=36.6,
    description="Who kills Mark?",
    age_limited=True
)

Game.objects.get(id=1).buyer.set((buyer1, buyer2))
Game.objects.get(id=2).buyer.set((buyer2, buyer3))
Game.objects.get(id=3).buyer.set((buyer3, ))

