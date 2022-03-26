from math import atan2, sin, cos, pi

class Quaternion(object):
    def __init__(self, w, i, j, k):
        self.w = w
        self.i = i
        self.j = j
        self.k = k

    def imag_mag(self):
        return (self.i**2 + self.j**2 + self.k **2)**0.5

    def mag(self):
        return (self.w**2 + self.i**2 + self.j**2 + self.k **2)**0.5

    def to_axis_angle(self):
        Q = self.imag_mag()
        x, y, z = [n / Q for n in [self.i, self.j, self.k]]
        return [2 * atan2(Q, w), x, y, z]

    def to_list(self):
        return [self.w, self.i, self.j, self.k]

    @classmethod
    def from_axis_angle(cls, theta, x,y,z):
        half_theta = theta * 0.5
        axis_mag = (x**2 + y**2 + z**2)**0.5
        sht = sin(half_theta)
        w = cos(half_theta)
        i,j,k = [n/axis_mag * sht for n in [x,y,z]]
        out = cls(w,i,j,k)
        return out

    def normalize(self):
        mag = self.mag()
        self.w = self.w / mag
        self.i = self.i / mag
        self.j = self.j / mag
        self.k = self.k / mag

    def conjugate(self):
        return Quaternion(self.w, -self.i, -self.j, -self.k)

    def ham_prod(self, other): 
        w1, i1, j1, k1 = self.to_list()
        w2, i2, j2, k2 = other.to_list()

        wo = w1*w2 -  i1*i2 - j1*j2 - k1*k2
        io = w1*i2 +  i1*w2 + j1*k2 - k1*j2
        jo = w1*j2 -  i1*k2 + j1*w2 + k1*i2
        ko = w1*k2 +  i1*j2 - j1*i2 + k1*w2
        return Quaternion(wo, io, jo, ko)



def grid_gen():
    """
    Generate a non-scaled, non-translated grid of a half hexagon shape consisting of 30 points. 
    Grid places the topmost, leftmost grid point at 0,0. 
    """
    points = []
    y_scale = 1
    x_scale = 0.866025 # Triangles!
    for i in range(4, 9):
        x = (i - 4) * x_scale
        y_start = (i - 4) * y_scale * 0.5
        for j in range(i):
            y = y_start - (j * y_scale)
            points.append([x,y])
    return points

def reflect_y(pt, axis):
    """
    Reflect the x value of pt about the given x-value
    """
    delta = pt[0] - axis
    new_x = pt[0] - 2 * delta
    return [new_x, pt[1]]

def rotate(pt, rotation):
    # Make the point a Quaternion
    pt_q = Quaternion(0, pt[0], pt[1], 0)

    rotated = rotation.ham_prod(pt_q).ham_prod(rotation.conjugate())
    return [rotated.i, rotated.j]

def translate(pt, dx, dy):
    return [pt[0] + dx, pt[1] + dy]

def scale(pt, x_scale, y_scale):
    return [pt[0] * x_scale, pt[1] * y_scale]

def transform(pt, scales, theta, translation):
    Q = Quaternion.from_axis_angle(theta, 0,0,1)
    return translate(rotate(scale(pt, *scales), Q), *translation)

if __name__ == "__main__": 
    from matplotlib import pyplot as pl

    pts = grid_gen()
    refl_pts = list([reflect_y(x, 4) for x in pts])
    pts = pts + refl_pts

    theta = 15 * pi / 180.0
    plot_pts = [transform(n, [2,2], theta, [5,5]) for n in pts]

    args = zip(*plot_pts)
    pl.scatter(*args)
    pl.show()
