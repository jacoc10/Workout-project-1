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
    file_bytes = []
    with open(original_file, "rb") as f:
        for byte in f:
            file_bytes.append(byte.decode().strip())
    return(file_bytes)


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