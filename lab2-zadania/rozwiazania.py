# Zadanie 1
def cube(num):
    return num**3

# Zadanie 2


def polynomial(a, b, c, x):
    return a*x*x + b*x + c

# Zadanie 3


def exercise_summary(name, num, time):
    return f"{name} wykonał(a) zadanie nr {num} w {time // 1000}.{time % 1000:03}s"

# Zadanie 4


def symofpoints(p1, p2):
    return (p1[0]+p2[0])/2, (p1[1]+p2[1])


# Zadanie 5
def bin_len(num):
    return len(bin(num)[2:])

# Zadanie 6


def tuple_average(nums):
    return f"numbers from {min(nums)} to {max(nums)} with an average of {(sum(nums)/len(nums))}"

# Zadanie 7


def table(width, height, length):

    def format_row(c1, c2):
        return f' {c1[0]:<{c1[1]}}|{c2[0]:>{c2[1]}} '

    def optimal_column_width(head, cols):
        cols_l = []
        for i in cols:
            cols_l.append(len(i))
        return max(len(head), (max(cols_l))) + 1

    col1 = "Wymiar", ("Szerokość", "Wysokość", "Długość")
    col2 = "Wartość", (f"{width:.3f}", f"{height:.3f}", f"{length:.3f}")
    col1_w = optimal_column_width(col1[0], col1[1])
    col2_w = optimal_column_width(col2[0], col2[1])

    print(format_row((col1[0], col1_w), (col2[0], col2_w)))
    print('----------------------')

    for i in range(3):
        print(format_row((col1[1][i], col1_w), (col2[1][i], col2_w)))

# Zadanie 8


def roots(a, b, c):
    delta = b**2 - (4 * a * c)
    if delta < 0:
        return "No roots"
    if delta == 0:
        return (-b-(delta**1/2))/2
    return (-b-(delta**1/2))/2, (-b+(delta**1/2))/2
