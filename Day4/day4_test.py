import Day4.day4 as day

def test_day_4_part_one():
    assert day.part_one() == 1650

def test_day_4_part_two():
    assert day.part_two() == 1129

def test_day_4_part_two_two():
    assert day.part_two_two() == 1129

# def test_benchmark_part_one(benchmark):
#      benchmark(day.part_one)

# def test_benchmark_part_two(benchmark):
#     benchmark.pedantic(day.part_two, iterations=10, rounds=100)    

# def test_benchmark_part_two_two(benchmark):
#     benchmark.pedantic(day.part_two_two, iterations=10, rounds=100)        