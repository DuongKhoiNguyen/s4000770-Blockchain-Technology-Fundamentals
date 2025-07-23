import hashlib
import random
import string

def compute_hash(input_str):
    """Compute SHA-256 hash of a string."""
    return hashlib.sha256(input_str.encode()).hexdigest()

def avalanche_effect_demo():
    """Demonstrate the avalanche effect of SHA-256."""
    original = input("Enter a string to hash: ")
    modified = original[:-1] + ('X' if original[-1] != 'X' else 'Y')
    original_hash = compute_hash(original)
    modified_hash = compute_hash(modified)

    print(f"\nOriginal string: {original}")
    print(f"Original hash:   {original_hash}")
    print(f"\nModified string: {modified}")
    print(f"Modified hash:   {modified_hash}")
    print("\nNotice how a tiny change in input causes a big change in the hash!")

def preimage_attempt(target_hash, max_attempts=50000):
    """Try to find a pre-image for a target hash (brute-force)."""
    print(f"\nAttempting pre-image search for target hash:\n{target_hash}")
    for attempt in range(max_attempts):
        candidate = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        candidate_hash = compute_hash(candidate)
        if candidate_hash == target_hash:
            print(f"Pre-image found: {candidate} in {attempt + 1} attempts.")
            return
    print("No pre-image found (as expected, due to pre-image resistance).")

if __name__ == "__main__":
    print("--- Hash Function Demonstration ---")
    avalanche_effect_demo()
    known_string = "blockchain"
    target = compute_hash(known_string)
    preimage_attempt(target)
