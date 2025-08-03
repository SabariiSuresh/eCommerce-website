
class Cart:
    def __init__(self , request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self , product):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += 1
        else:
            self.cart[product_id]={'quantity' : 1}
        self.save()

    def remove(self , product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        self.session['cart']={}
        self.save()


    def save(self):
        self.session.modified = True


    def __iter__(self):
        from .models import Product
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            product_id = str(product.id)
            cart_item = self.cart[str(product_id)]
            cart_item = cart_item.copy()
            cart_item['product'] = product
            cart_item['total'] = product.price * cart_item['quantity']
            yield cart_item


    def get_total_price(self):
        from .models import Product      
        total = 0
        for item in self.__iter__():
            total += item['total']
        return total                                    

    
    def increase(self , product):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['quantity']+=1
            self.save()


    def decrease(self , product):
        product_id = str(product.id)
        if product_id in self.cart:
            if self.cart[product_id]['quantity']>1:
                self.cart[product_id]['quantity']-=1
            else:
                self.remove(product)
            self.save()               