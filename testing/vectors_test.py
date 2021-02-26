from PhysMath.intromath.vectors import vec2d

a = vec2d(3, 4)

print('x component = ', a.get_x())
print('y component = ', a.get_y())
print('vector form =', a.get_vec())
print('magnitude = ', a.mag())
print('radian angle (from positive x-axis) =', a.angleRad(), 'radians')
print('degree angel (from positive x-axis) =', a.angleDeg(), 'degrees')

b = vec2d(5, 6)
c = a + b
d = vec2d(9, 10)
f = a + b - d

print(a.get_vec(), '+', b.get_vec(), '=', c.get_vec())
print(a.get_vec(), '+', b.get_vec(), '-', d.get_vec(), '=', f.get_vec())


