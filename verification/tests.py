"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[4, 6, 2, 2, 6, 4, 4, 4]],
            "answer": [4, 4, 4, 4, 6, 6, 2, 2]
        },
        {
            "input": [[4, 6, 2, 2, 2, 6, 4, 4, 4]],
            "answer": [4, 4, 4, 4, 6, 6, 2, 2, 2]
        },
        {
            "input": [['bob','bob','carl','alex','bob']],
            "answer": ['bob','bob','bob','carl','alex']
        },
        {
            "input": [[17, 99, 42]],
            "answer": [17, 99, 42]
        },
        {
            "input": [[]],
            "answer": []
        },
        {
            "input": [[1]],
            "answer": [1]
        }
    ],
    "Extra": [
        {
            "input": [[6, 3]],
            "answer": [6, 3]
        },
        {
            "input": [[1,1,1,1]],
            "answer": [1,1,1,1]
        },
        {
            "input": [[1,2,2,1]],
            "answer": [1,1,2,2]
        }
    ]
}
