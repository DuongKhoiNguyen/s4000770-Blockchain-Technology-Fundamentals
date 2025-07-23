import hashlib

def hash_leaf(data):
    return hashlib.sha256(data.encode()).hexdigest()

def hash_node(left, right):
    combined = left + right
    return hashlib.sha256(combined.encode()).hexdigest()

def build_merkle_tree(data_list):
    """Build a Merkle Tree and return the root hash."""
    if not data_list:
        return ''
    current_level = [hash_leaf(item) for item in data_list]
    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i + 1] if i + 1 < len(current_level) else left
            next_level.append(hash_node(left, right))
        current_level = next_level
    return current_level[0]

def generate_merkle_proof(data_list, target_item):
    """Generate a Merkle proof for a target item."""
    proof = []
    idx = data_list.index(target_item)
    current_level = [hash_leaf(item) for item in data_list]
    while len(current_level) > 1:
        new_level = []
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i + 1] if i + 1 < len(current_level) else left
            if i == idx or i + 1 == idx:
                sibling = right if i == idx else left
                position = 'right' if i == idx else 'left'
                proof.append((sibling, position))
                idx = i // 2
            new_level.append(hash_node(left, right))
        current_level = new_level
    return proof

def verify_merkle_proof(leaf, proof, root):
    current_hash = hash_leaf(leaf)
    for sibling_hash, position in proof:
        if position == 'left':
            current_hash = hash_node(sibling_hash, current_hash)
        else:
            current_hash = hash_node(current_hash, sibling_hash)
    return current_hash == root

if __name__ == "__main__":
    transactions = ["tx1", "tx2", "tx3", "tx4"]
    root = build_merkle_tree(transactions)
    print("Merkle Root:", root)

    target = "tx3"
    proof = generate_merkle_proof(transactions, target)
    print(f"Proof for {target}:", proof)

    valid = verify_merkle_proof(target, proof, root)
    print("Proof valid?", valid)
