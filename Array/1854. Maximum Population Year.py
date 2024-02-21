from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        # find the earilest year of birth and the latest year of death
        sortedByBirth = sorted(logs, key=lambda x: x[0])
        sortedByDeath = sorted(logs, key=lambda x: x[1])

        firstYear = sortedByBirth[0][0]
        lastYear = sortedByDeath[-1][1]

        # iterate over years to find population of each year and store maximun population year
        maxPopulationYear = firstYear
        maxPopulation = 0
        for i in range(firstYear, lastYear + 1):
            currentYearPopulation = 0
            for log in logs:
                if i >= log[0] and i < log[1]:
                    currentYearPopulation += 1
            if currentYearPopulation > maxPopulation:
                maxPopulation = max(currentYearPopulation, maxPopulation)
                maxPopulationYear = i

        # return the maximun population year
        return maxPopulationYear
