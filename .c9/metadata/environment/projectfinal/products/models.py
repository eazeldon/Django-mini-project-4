{"filter":false,"title":"models.py","tooltip":"/projectfinal/products/models.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":3,"column":0},"end":{"row":10,"column":24},"action":"insert","lines":["class Product(models.Model):","    name = models.CharField(max_length=254, default='')","    description = models.TextField()","    price = models.DecimalField(max_digits=6, decimal_places=2)","    image = models.ImageField(upload_to='images')","","    def __str__(self):","        return self.name"],"id":2}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":24},"end":{"row":10,"column":24},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1575614642608,"hash":"e0b274e4a9a212f98c452e16d3b65848db0d56f5"}