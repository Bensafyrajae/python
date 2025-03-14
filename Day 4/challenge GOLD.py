import random


class Gene:
    def __init__(self):
        self.value = random.choice([0, 1])

    def mutate(self):
        self.value = 1 - self.value

    def __repr__(self):
        return str(self.value)


class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]

    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:
                gene.mutate()

    def __repr__(self):
        return "".join(map(str, self.genes))


class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]

    def mutate(self):
        for chromosome in self.chromosomes:
            if random.random() < 0.5:
                chromosome.mutate()

    def is_all_ones(self):
        return all(gene.value == 1 for chromosome in self.chromosomes for gene in chromosome.genes)

    def __repr__(self):
        return "\n".join(map(str, self.chromosomes))


class Organism:
    def __init__(self, mutation_prob):
        self.dna = DNA()
        self.mutation_prob = mutation_prob

    def mutate(self):
        if random.random() < self.mutation_prob:
            self.dna.mutate()


def simulate_evolution(mutation_prob):
    organism = Organism(mutation_prob)
    generations = 0

    while not organism.dna.is_all_ones():
        organism.mutate()
        generations += 1

    return generations


mutation_probability = 0.2
generations_needed = simulate_evolution(mutation_probability)

print(f"Evolution completed in {generations_needed} generations.")
