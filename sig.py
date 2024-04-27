import sys

def generate_sequence(end_position):
    result = ""
    position = 1
    while len(result) < end_position:
        result += str(position) + " "
        position += len(str(position)) + 1
    return result.strip()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {filename}.py <end_position>")
    else:
        end_position = int(sys.argv[1])
        output = generate_sequence(end_position)
        print(output)
