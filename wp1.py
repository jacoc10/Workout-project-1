import argparse

def retrieve_inputs():
    parser = argparse.ArgumentParser()
    parser.add_argument("input1")
    parser.add_argument("input2")

    args = parser.parse_args()

    original_file = args.input1
    encrypted_file = args.input2

    return(original_file, encrypted_file)

def read_file(original_file):
    characters = []
    with open(original_file, "rb") as f:
        for byte in f:
            characters.append(byte)

def write_file(content, encrypted_file):
    content.reverse()
    with open(encrypted_file, "w"):
        for byte in content:
            encrypted_file.write(byte, end="")

def main():
    original_file, encrypted_file = retrieve_inputs()
    write_file(read_file(original_file), encrypted_file)
if __name__ == "__main__":
    main()