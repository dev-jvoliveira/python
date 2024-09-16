real = float(input('Quanto de dinheiro voce tem na carteira? R$:  '))
dolar = real / 5.56
euro = real / 6.19
print('Com R$: {:.2f} voce pode comprar US$: {:.2f}'.format(real, dolar))
print('Com R$: {:.2f} voce pode comprar EUR: {:.2f}'.format(real, euro))
    
