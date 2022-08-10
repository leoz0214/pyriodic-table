from pyriodic_table.periodictable import PeriodicTable


def elements_with_prime_atomic_number():
    periodic_table = PeriodicTable()
    primes = generate_primes_up_to_118()
    return [periodic_table.get_element_by_atomic_number(n) for n in primes]


def generate_primes_up_to_118():
    primes = [2]

    for i in range(3, 119):
        upper = int(i ** 0.5) + 1
        for prime in primes:
            if prime > upper:
                primes.append(i)
                break
            elif i % prime == 0:
                break
        else:
            primes.append(i)
    
    return primes


if __name__ == "__main__":
    print(elements_with_prime_atomic_number())

# Output:
"""
[helium, lithium, boron, nitrogen, sodium, aluminium, chlorine, potassium,
vanadium, copper, gallium, rubidium, niobium, technetium, silver, iodine,
praseodymium, promethium, holmium, lutetium, tantalum, gold, bismuth,
actinium, berkelium, mendelevium, lawrencium, bohrium, meitnerium, nihonium]
"""
# Correct!