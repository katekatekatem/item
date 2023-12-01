from django.db import models


CURRENCY_CHOICES = (('rub', 'rubles'), ('usd', 'dollars'))

DURATION_CHOICES = (
    ('forever', 'forever'),
    ('once', 'once'),
    ('repeating', 'repeating')
)

USD_TO_RUB = 90


class Item(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name[:20]


class Coupon(models.Model):
    amount_off = models.PositiveIntegerField()
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    duration = models.CharField(max_length=10, choices=DURATION_CHOICES)
    duration_in_months = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['amount_off']

    def __str__(self):
        return str(self.amount_off)


class Tax(models.Model):
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    display_name = models.CharField(max_length=30)
    inclusive = models.BooleanField()

    class Meta:
        ordering = ['display_name']

    def __str__(self):
        return str(self.display_name)


class Order(models.Model):

    items = models.ManyToManyField(Item, through='ItemOrder')
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE)

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
