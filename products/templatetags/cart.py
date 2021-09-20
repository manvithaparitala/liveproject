from django import template
#varibale(register)=module(template).class(library) which is used to store the filters and tags of the attributes
register = template.Library()

#if the item is in cart
#@ is a decorater which used to make new functionality with out modifying the existing one
@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    #variable(keys)
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False

#count the no of items adding to cart
@register.filter(name='count')
def count(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0

#used to add the total price of the items
@register.filter(name='price_total')
def price_total(product, cart):
    return product.price * count(product, cart)

#displaying the total price
@register.filter(name='total_cart')
def total_cart(products, cart):
    #intially with zero items
    ans = 0
    for p in products:
        #adding the items one by one and returns
        ans += price_total(p, cart) 
    return ans

#adding 100 rupees for final price just like shipping
@register.filter(name='total_100')
def total_100(products, cart):
    ans = 100 + total_cart(products, cart)
    return ans

#now if coupen applied 
@register.filter(name='coupon')
def coupon(offers, codes):
    c = 0
    #if coupen added in admin ie.,database
    for offer in offers:
        if codes in offer.code:
            c += 1
    if c == 0:
        return False
    else:
        return True

#if coupen applied the price getting decreased which is shown as discount by % --ex:PRO10 value is 30 and discount is 0.3
@register.filter(name='cvalue')
def cvalue(offers, codes):
    for offer in offers:
        if codes in offer.code:
            return offer.discount * 100

#productprice -(productprice * coupenfinalprice)
@register.filter(name='ctotal')
def ctotal(ptotal, dvalue):
    return ptotal - (ptotal * dvalue) / 100
