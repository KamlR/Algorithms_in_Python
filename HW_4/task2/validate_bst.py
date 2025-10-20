def validate_bst(node, min_val=float('-inf'), max_val=float('+inf')):
    if node is None:
        return True

    if not (min_val < node.value < max_val):
        return False

    return (validate_bst(node.left, min_val, node.value) and
            validate_bst(node.right, node.value, max_val))

