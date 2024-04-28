import math
from scipy.stats import chi2
from scipy.stats import fisher_exact

def calculate_fisher_exact_2x3(table):
    p_values = []
    for i in range(3):
        for j in range(i+1, 3):
            sub_table = [[table[0][i], table[0][j]], [table[1][i], table[1][j]]]
            _, p_value = fisher_exact(sub_table)
            p_values.append(p_value)
            
    combined_p_value = chi2.sf(-2 * sum(map(lambda x: math.log(x), p_values)), df=2*len(p_values))

    return combined_p_value

if __name__ == "__main__":
    contingency_table = [[9, 10, 6], [2, 4, 1]] 

    p_value = calculate_fisher_exact_2x3(contingency_table)

    print("Fisher exact test p-value for 2x3 table:", p_value)
