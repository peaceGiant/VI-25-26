from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    movies = dict()

    n = int(input())
    for _ in range(n):
        film_info = input()
        film, genre, time = film_info.split(' ')
        movies[film] = (float(time), genre)

    l_days = int(input())

    # Define the variables and domains here.
    variables = list(movies.keys())
    # (day, time, cinema)
    days = [f'Day {i}' for i in range(1, l_days + 1)]
    times = [t for t in range(12, 23 + 1)]
    cinemas = ['Cinema 1', 'Cinema 2']

    # for day in days:
    #     for time in times:
    #         for cinema in cinemas:
    #             domain.append((day, time, cinema))

    domain = [(day, time, cinema) for day in days for time in times for cinema in cinemas]

    problem.addVariables(variables, domain)

    # Define the constraints here.
    # Constraint 1. Films must not overlap.
    def constraint_1(ass1, ass2, film1_name, film2_name):
        d1, t1, c1 = ass1
        d2, t2, c2 = ass2
        dur1, _ = movies[film1_name]
        dur2, _ = movies[film2_name]

        if d1 != d2:
            return True

        if c1 != c2:
            return True

        if t1 < t2:
            if t1 + dur1 < t2:
                return True
            else:
                return False
        else:
            if t2 + dur2 < t1:
                return True
            else:
                return False

    for i, var1 in enumerate(variables):
        for var2 in variables[i + 1:]:
            problem.addConstraint(lambda v1, v2, fn1=var1, fn2=var2: constraint_1(v1, v2, fn1, fn2), [var1, var2])

    # Constraint 2. Check whether horror movies begin after 21:00
    horror_film_vars = [k for k, v in movies.items() if v[1].lower() == 'horror']

    def constraint_2(ass1):
        d, t, c = ass1

        return t >= 21

    for film in horror_film_vars:
        problem.addConstraint(constraint_2, [film])

    # Constraint 3. Movies with duration < 2 are assigned on the same day
    short_film_vars = [k for k, v in movies.items() if v[0] < 2]

    def constraint_3(*ass_vars):
        days = [d for (d, _, _) in ass_vars]
        return all(day == days[0] for day in days)
        # return len(set(days)) == 1

    problem.addConstraint(constraint_3, short_film_vars)

    result = problem.getSolution()

    # Print the solution in required format.
    if result is not None:
        for film_name, (day, time, cinema) in sorted(result.items(), key=lambda x: x[0]):
            print(f'{film_name}: {day} {time}:00 - {cinema}')
    else:
        print('No Solution!')