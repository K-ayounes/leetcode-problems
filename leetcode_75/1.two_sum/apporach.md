# Solution


```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    solutions = {}

    for index, num in enumerate(nums):
        if num in solutions:
            return [index, solutions[num]]

        solutions[target - num] = index

    return [0]
```

# General Idea
> Loop over the numbers array and for each number calculate what other number does it need to reach the target. 
>
> Keep a dictionary of the required numbers to reach a solution as the keys, and the index of the number that needs them as the value.
>

# Detailed
- For each number in the array of numbers `nums` we calculate its complement number, the number required to reach the target from the current number.

- If number is `a` then the complement of `a` is `b=target - a`.

- We keep a dictonary of complements, where each complement points to its source, the `a` number.

- While looping, we check if the current number is in the dictionary of complements, if it is we have an answer, else we update the complements dictionary
