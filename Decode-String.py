# this is leet code solution (394)
def decodeString(s):
    def helper(index):
        result = ""
        num = 0

        while index < len(s):
            char = s[index]

            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                index, sub_result = helper(index + 1)
                result += num * sub_result
                num = 0
            elif char == ']':
                return index, result
            else:
                result += char

            index += 1

        return result

    return helper(0)

# Example usage:
encoded_string = "3[a]2[bc]"
decoded_string = decodeString(encoded_string)
print(decoded_string)  # Output: "aaabcbc"
