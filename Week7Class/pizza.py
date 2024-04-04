sandwich_order = {
    'pastrmi', 'veggie', 'pastrmi',
    'grilled cheese', 'pastrmi', 
    'turkey', 'roast beef'
}

print('Deli has run out of pastrmi')

while 'pastrmi' in sandwich_order:
    sandwich_order.remove('pastrmi')

print(sandwich_order)

for sandwich in sandwich_order:
    print(f'Order up! {sandwich.capitalize} sandwich')