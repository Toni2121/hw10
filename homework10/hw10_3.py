def get_statistics(numbers: list[int]) -> dict:
    return {"sum": sum(numbers), "average": sum(numbers) / len(numbers), "length": len(numbers),\
            "biggest number": max(numbers), "smallest number": min(numbers)}



print(get_statistics([1, 2, 3, 4, 5]))