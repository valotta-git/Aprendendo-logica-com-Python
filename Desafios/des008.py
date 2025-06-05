lar = float (input ('Largura da parede: '))
alt = float (input ('Altura da parede: '))
area = lar * alt
tinta = area / 2
print ('Sua parede tem a dimensão de {} x {}, a área equivale a {}m2\nA parede vai precisar de {:.3f} litros de tinta'.format (lar, alt, area, tinta))