class Entry:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent


class File(Entry):
    def __init__(self, name, parent, size):
        super().__init__(name, parent)
        self.size = size


class Directory(Entry):
    def __init__(self, name, parent=None, children=None):
        super().__init__(name, parent)
        self.children = children


def get_small_dir_sizes(dir, small_dir_sizes, MAX_SIZE):
    if (dir.children == None):
        return 0

    size = 0

    for entry in dir.children:
        if isinstance(entry, Directory):
            size += get_small_dir_sizes(entry, small_dir_sizes, MAX_SIZE)
            continue

        size += entry.size

    if (size <= MAX_SIZE):
        small_dir_sizes.append(size)

    return size


def get_dir_sizes(dir, dir_sizes):
    if (dir.children == None):
        print(dir.name)
        return 0

    size = 0

    for entry in dir.children:
        if isinstance(entry, Directory):
            size += get_dir_sizes(entry, dir_sizes)
            continue

        size += entry.size

    dir_sizes.append(size)

    return size


def build_file_system(lines) -> Directory:
    """Returns root directory
    """
    root = Directory('/')
    curr_dir = None
    curr_children = []

    for line in lines:
        # add children
        if (len(curr_children) > 0 and (line[0] == '$' or line == 'EOF')):
            curr_dir.children = curr_children
            curr_children = []

        if (line == 'EOF'):
            continue

        if ('$ cd' in line):
            *_, new_dir = line.split()
            if new_dir == '/':
                 curr_dir = root
            elif new_dir == "..":
                curr_dir = curr_dir.parent
            else:
                curr_dir = [entry for entry in curr_dir.children if (
                    entry.name == new_dir) and (isinstance(entry, Directory))][0]
            continue

        if ('$ ls' in line):
            continue

        words = line.split()

        if (words[0] == 'dir'):
            name = words[1]
            curr_children.append(Directory(name=name, parent=curr_dir))
            continue

        curr_children.append(
            File(name=words[1], size=int(words[0]), parent=curr_dir))

    return root


def solve_part1():
    MAX_SIZE = 100000

    with open('7/input.txt') as f:
        lines = [line.strip() for line in f.readlines()] + ['EOF']

    # Initialize Directory Tree
    root = build_file_system(lines)

    # get directories with size < MAX_LENGTH
    small_dir_sizes = []
    get_small_dir_sizes(root, small_dir_sizes, MAX_SIZE)

    small_dirs_sum = sum(small_dir_sizes)

    return small_dirs_sum


def solve_part2():
    TOTAL_DISK_SPACE = 70000000
    NEEDED_SPACE = 30000000

    with open('7/input.txt') as f:
        lines = [line.strip() for line in f.readlines()] + ['EOF']

    # Initialize Directory Tree
    root = build_file_system(lines)

    # get directories with size < MAX_LENGTH
    dir_sizes = []
    space_used = get_dir_sizes(root, dir_sizes)
    free_space = TOTAL_DISK_SPACE - space_used

    acceptable_dir_sizes = [
        size for size in dir_sizes if free_space + size >= NEEDED_SPACE]

    return min(acceptable_dir_sizes)


print(solve_part1())
print(solve_part2())
