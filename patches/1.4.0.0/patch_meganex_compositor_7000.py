import hashlib
import sys

expected_hash = "aec18721ace89241333100573cf944307c5fe4559b796ef858f2e38419ab48a5"

input_file = "MeganeX_Compositor.exe"
output_file = "MeganeX_Compositor.7000.exe"

byte_diffs = { 
    # 0x36b0 is 14000 (7000*2) as an int. This determines the combined width of
    # the two render targets (left eye + right eye)
    0x4e353: bytes([0xb8, 0xb0, 0x36, 0x00, 0x00, 0x90, 0x48, 0x90]),

    # 0xdac0 is 7000 as a float. The two middle diffs are used as inputs to the
    # shader doing the downscale and warp.
    0x4e392: bytes([0xc0, 0xda]),
    0x4e39d: bytes([0xc0, 0xda]),

    # 0x1b58 is 7000 as an int, used to determine the render targets' height.
    0x4e3ac: bytes([0x58, 0x1b])
}

def compute_sha256(filename):
    sha256_hash = hashlib.sha256()
    try:
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"Error reading file for hash computation: {e}")
        sys.exit(1)

def main():
    # Validate we're patching the expected version of the compositor.
    file_hash = compute_sha256(input_file)
    if file_hash.lower() != expected_hash.lower():
        print("Error: File hash does not match the expected value.")
        print(f"Expected: {expected_hash}")
        print(f"Found:    {file_hash}")
        sys.exit(1)
    print("File verification successful.")

    # Apply the patches
    try:
        with open(input_file, "rb") as f:
            data = bytearray(f.read())

        for target_offset, byte_diff in byte_diffs.items():
            data[target_offset:target_offset + len(byte_diff)] = byte_diff

        with open(output_file, "wb") as f:
            f.write(data)

        print(f"Successfully created patched file '{output_file}'")
    except Exception as e:
        print(f"An error occurred: {e}")

main()