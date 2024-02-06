
# Zadanie 1


def common_segment(segment1, segment2):
    return max(segment1[0], segment2[0]), min(segment1[1], segment2[1])

# Zadanie 2


def message(text, width):
    indent = width-2
    print("*" * width)
    print(f"*{' ' * (indent)}*")
    print(f"*{text:^{indent}}*")
    print(f"*{' ' * (indent)}*")
    print("*" * width)

# Zadanie 3


def rectangle_fill(height, width):
    single_line = f"{'*' * width}\n"
    return (single_line*height)
