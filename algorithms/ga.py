import random

def fitness(kromosom, v, w, C):
    total_value = 0
    total_weight = 0

    for i, gen in enumerate(kromosom):
        if gen:
            total_value += v[i]
            total_weight += w[i]

    if total_weight > C:
        return 0

    return total_value

def bangkitkan_populasi(pop, n):
    populasi = []

    for _ in range(pop):
        kromosom = [
            random.randint(0, 1) for _ in range(n)
        ]
        populasi.append(kromosom)

    return populasi

def seleksi(populasi, v, w, C):
    individu = random.sample(populasi, min(3, len(populasi)))

    terbaik = individu[0]
    for p in individu:
        if fitness(p, v, w, C) > fitness(terbaik, v, w, C):
            terbaik = p

    return terbaik

def persilangan(parent1, parent2):
    point = random.randint(1, len(parent1)-1)

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    return child1, child2

def mutasi(kromosom):
    mutation_rate = 0.05
    for i in range(len(kromosom)):
        if random.random() < mutation_rate:
            kromosom[i] = 1 - kromosom[i]

    return kromosom

def knapsack_ga(C, n, v, w):
    pop = max(10, n)
    generasi = 100
    populasi = bangkitkan_populasi(pop, n)

    total_value = -1
    total_weight = -1

    for _ in range(generasi):
        populasi_baru = []

        while len(populasi_baru) < pop:
            parent1 = seleksi(populasi, v, w, C)
            parent2 = seleksi(populasi, v, w, C)

            child1, child2 = persilangan(parent1, parent2)

            child1 = mutasi(child1)
            child2 = mutasi(child2)

            populasi_baru.append(child1)
            populasi_baru.append(child2)

        populasi = populasi_baru[:pop]

        for kromosom in populasi:
            nilai = fitness(kromosom, v, w, C)
            if nilai > total_value:
                total_value = nilai
                total_weight = sum(w[i] for i in range(len(kromosom)) if kromosom[i] == 1)
    
    return total_value, total_weight