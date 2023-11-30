from django.db import models


CHOICES = (('rub', 'rub'), ('usd', 'usd'))

USD_TO_RUB = 90


class Item(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, choices=CHOICES)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name[:20]


class Order(models.Model):

    items = models.ManyToManyField('Item', through='ItemOrder')

    class Meta:
        ordering = ['pk']

    def get_currency(self):
        currencies = set(item.currency for item in self.items.all())
        if len(currencies) == 1:
            return currencies.pop()
        else:
            return False

    def get_total_price(self):
        if self.get_currency():
            return sum(item.price for item in self.items.all())


class ItemOrder(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.item} {self.order}'
