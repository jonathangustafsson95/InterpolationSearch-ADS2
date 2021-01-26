from Input import input_gen

n = 100


data = input_gen.big_element_last(n)
data1 = input_gen.best_case_distribution(n)
data2 = input_gen.normal_distribution(n)
data3 = input_gen.random_uniform_dist(n)


print(data)
print(data1)
print(data2)
print(data3)


