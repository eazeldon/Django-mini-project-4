{"filter":false,"title":"admin.py","tooltip":"/checkout/admin.py","undoManager":{"mark":3,"position":3,"stack":[[{"start":{"row":0,"column":32},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":40},"action":"insert","lines":["from .models import Order, OrderLineItem"],"id":3}],[{"start":{"row":3,"column":28},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":4,"column":0},"end":{"row":12,"column":38},"action":"insert","lines":["class OrderLineAdminInline(admin.TabularInline):","    model = OrderLineItem","","","class OrderAdmin(admin.ModelAdmin):","    inlines = (OrderLineAdminInline, )","","","admin.site.register(Order, OrderAdmin)"],"id":5}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":0},"end":{"row":13,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1575999732599,"hash":"0ad008882b20369ddbe95f9a035de2e5703ee833"}