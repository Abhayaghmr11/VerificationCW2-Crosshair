import math
import random
from typing import Optional, List

class SearchProblem:
    """
    A stub for demonstration.
    Your real class should have .x, .y, .score(), .get_neighbors() methods.
    """
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def score(self) -> float:
        # Example scoring function
        return -(self.x**2 + self.y**2)

    def get_neighbors(self) -> List["SearchProblem"]:
        # Example: produce 4 neighbors by small +/- adjustments
        step = 1.0
        return [
            SearchProblem(self.x + step, self.y),
            SearchProblem(self.x - step, self.y),
            SearchProblem(self.x, self.y + step),
            SearchProblem(self.x, self.y - step),
        ]
    

def simulated_annealing(
    search_prob: SearchProblem,
    find_max: bool = True,
    max_x: float = math.inf,
    min_x: float = -math.inf,
    max_y: float = math.inf,
    min_y: float = -math.inf,
    start_temp: float = 100,
    rate_of_decrease: float = 0.01,
    threshold_temp: float = 1,
) -> SearchProblem:

    assert min_x < max_x, "Precondition: The min_x must be strictly less than max_x."
    assert min_y < max_y, "Precondition: The min_y must be strictly less than max_y."
    assert 0 < rate_of_decrease < 1, "Precondition: rate_of_decrease must be between 0 and 1."
    assert start_temp > threshold_temp, "Precondition: start_temp must be strictly greater than threshold_temp so that temperature stays positive."
    assert threshold_temp > 0, "Precondition: threshold_temp must be strictly positive."

    # Ensure the initial search state is within bounds
    assert min_x <= search_prob.x <= max_x, "Precondition: initial state's x out of domain bounds."
    assert min_y <= search_prob.y <= max_y, "Precondition: initial state's y out of domain bounds."

    current_state = search_prob
    current_temp = start_temp
    best_state: Optional[SearchProblem] = None

    # --------------------------------------
    # Loop until the temperature is too low
    # --------------------------------------
    while True:
        # -------------
        #  INVARIANTS
        # -------------
        assert current_temp > 0, "Loop Invariant: temperature must remain positive during search."

        current_score = current_state.score()
        if best_state is None or (
            find_max and current_score > best_state.score()
        ) or (
            not find_max and current_score < best_state.score()
        ):
            best_state = current_state

        neighbors = current_state.get_neighbors()
        next_state: Optional[SearchProblem] = None

        while neighbors and next_state is None:
            index = random.randint(0, len(neighbors) - 1)
            picked_neighbor = neighbors.pop(index)
            # Skip neighbors out of domain
            if not (min_x <= picked_neighbor.x <= max_x and min_y <= picked_neighbor.y <= max_y):
                continue

            change = picked_neighbor.score() - current_score
            if not find_max:
                change = -change  # For minimizing, we invert the difference

            if change > 0:
                # Improves the solution (for max) or does not worsen it (for min)
                next_state = picked_neighbor
            else:
                # Accept with some probability
                probability = math.exp(change / current_temp)
                if random.random() < probability:
                    next_state = picked_neighbor

        # Reduce the temperature
        current_temp -= current_temp * rate_of_decrease

        # Termination condition
        # If temperature is below threshold or no suitable next_state
        if current_temp < threshold_temp or next_state is None:
            break

        current_state = next_state

    # ----------------------
    #  POSTCONDITION CHECK
    # ----------------------
    assert best_state is not None, "Postcondition: We must have identified at least one best_state."
    assert min_x <= best_state.x <= max_x, "Postcondition: best_state.x out of domain bounds."
    assert min_y <= best_state.y <= max_y, "Postcondition: best_state.y out of domain bounds."

    return best_state