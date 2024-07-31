import timeit

# Реалізація алгоритмів

# Boyer-Moore algorithm
def boyer_moore_search(text, pattern):
    def build_last_table(pattern):
        last = {}
        for i, char in enumerate(pattern):
            last[char] = i
        return last

    last = build_last_table(pattern)
    m = len(pattern)
    n = len(text)
    s = 0
    iterations = 0

    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        iterations += 1
        if j < 0:
            return (iterations, s)
        else:
            s += max(1, j - last.get(text[s + j], -1))
    return (iterations, -1)

# Knuth-Morris-Pratt algorithm
def knuth_morris_pratt_search(text, pattern):
    def compute_prefix_function(pattern):
        m = len(pattern)
        pi = [0] * m
        k = 0
        for q in range(1, m):
            while k > 0 and pattern[k] != pattern[q]:
                k = pi[k - 1]
            if pattern[k] == pattern[q]:
                k += 1
            pi[q] = k
        return pi

    m = len(pattern)
    n = len(text)
    pi = compute_prefix_function(pattern)
    q = 0
    iterations = 0

    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q += 1
        iterations += 1
        if q == m:
            return (iterations, i - m + 1)
    return (iterations, -1)

# Rabin-Karp algorithm
def rabin_karp_search(text, pattern, q=101):  # q is a prime number
    m = len(pattern)
    n = len(text)
    d = 256
    p = 0
    t = 0
    h = 1
    iterations = 0

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
                j += 1
            iterations += 1
            if j == m:
                return (iterations, i)
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
        iterations += 1

    return (iterations, -1)

# Читання вмісту файлів
with open('стаття 1.txt', 'r', encoding='cp1251') as file:
    text1 = file.read()

with open('стаття 2.txt', 'r', encoding='cp1251') as file:
    text2 = file.read()

# Визначення реальних та вигаданих підрядків
existing_substring1 = "Жадібний алгоритм"
fictional_substring1 = "недійсний пошук"
existing_substring2 = "Бінарні діаграми рішень"
fictional_substring2 = "неіснуючий елемент"

# Вимірювання часу виконання та кількості ітерацій
results = {}

for text, existing, fictional, text_id in [(text1, existing_substring1, fictional_substring1, 'стаття 1'),
                                       (text2, existing_substring2, fictional_substring2, 'стаття 2')]:
    results[text_id] = {}
    for substring, sub_id in [(existing, 'реальний'), (fictional, 'вигаданий')]:
        results[text_id][sub_id] = {}
        
        # Алгоритм Бойера-Мура
        time_boyer_moore = timeit.timeit(lambda: boyer_moore_search(text, substring), number=10)
        iterations_boyer_moore, _ = boyer_moore_search(text, substring)
        results[text_id][sub_id]['Бойера-Мура'] = (time_boyer_moore, iterations_boyer_moore)
        
        # Алгоритм Кнута-Морріса-Пратта
        time_kmp = timeit.timeit(lambda: knuth_morris_pratt_search(text, substring), number=10)
        iterations_kmp, _ = knuth_morris_pratt_search(text, substring)
        results[text_id][sub_id]['Кнута-Морріса-Пратта'] = (time_kmp, iterations_kmp)
        
        # Алгоритм Рабіна-Карпа
        time_rabin_karp = timeit.timeit(lambda: rabin_karp_search(text, substring), number=10)
        iterations_rabin_karp, _ = rabin_karp_search(text, substring)
        results[text_id][sub_id]['Рабіна-Карпа'] = (time_rabin_karp, iterations_rabin_karp)

# Виведення результатів
for text_id, data in results.items():
    print(f"Результати для {text_id}:")
    best_alg = None
    best_time = float('inf')
    for sub_id, alg_results in data.items():
        print(f"  Підрядок {sub_id}:")
        for alg, (time, iterations) in alg_results.items():
            print(f"    {alg}:")
            print(f"      Час виконання: {time:.6f} секунд")
            print(f"      Кількість ітерацій: {iterations}")
            if time < best_time:
                best_time = time
                best_alg = alg
    print(f"\n  Найшвидший алгоритм для {text_id}: {best_alg} (час виконання: {best_time:.6f} секунд)")
    print("\n")
