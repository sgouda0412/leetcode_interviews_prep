def product_except_self(nums):
    length = len(nums)

    # Initialize output array with all 1s
    output = [1] * length

    # Calculate left products
    left_product = 1
    for i in range(length):
        output[i] = left_product
        left_product *= nums[i]

    # Calculate right products and multiply with left products
    right_product = 1
    for i in range(length - 1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]

    return output

if __name__ == "__main__":
# Example usage:
    nums = [1, 2, 3, 4] 
    result = product_except_self(nums)
    print(result)
