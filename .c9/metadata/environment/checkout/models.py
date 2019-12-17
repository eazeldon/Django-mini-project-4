{"filter":false,"title":"models.py","tooltip":"/checkout/models.py","undoManager":{"mark":3,"position":3,"stack":[[{"start":{"row":0,"column":28},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":35},"action":"insert","lines":["from products.models import Product"],"id":3}],[{"start":{"row":3,"column":26},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":4,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["class Order(models.Model):","    full_name = models.CharField(max_length=50, blank=False)","    phone_number = models.CharField(max_length=20, blank=False)","    country = models.CharField(max_length=40, blank=False)","    postcode = models.CharField(max_length=20, blank=True)","    town_or_city = models.CharField(max_length=40, blank=False)","    street_address1 = models.CharField(max_length=40, blank=False)","    street_address2 = models.CharField(max_length=40, blank=False)","    county = models.CharField(max_length=40, blank=False)","    date = models.DateField()","","    def __str__(self):","        return \"{0}-{1}-{2}\".format(self.id, self.date, self.full_name)","","","class OrderLineItem(models.Model):","    order = models.ForeignKey(Order, null=False)","    product = models.ForeignKey(Product, null=False)","    quantity = models.IntegerField(blank=False)","","    def __str__(self):","        return \"{0} {1} @ {2}\".format(","            self.quantity, self.product.name, self.product.price)",""],"id":5}]]},"ace":{"folds":[],"scrolltop":85.5,"scrollleft":0,"selection":{"start":{"row":27,"column":0},"end":{"row":27,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":2,"state":"start","mode":"ace/mode/python"}},"timestamp":1575999294930,"hash":"0650e20d2b4e292c8aec6f1bd598847326c0404c"}